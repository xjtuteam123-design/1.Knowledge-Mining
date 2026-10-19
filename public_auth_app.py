"""Custom public sign-in and registration UI for the mounted Gradio app."""

from __future__ import annotations

import html
from urllib.parse import parse_qs

import gradio as gr
import uvicorn
from fastapi import FastAPI, Request
from starlette.middleware.gzip import GZipMiddleware
from fastapi.responses import HTMLResponse, RedirectResponse

from account_store import (
    authenticate_account,
    create_web_session,
    delete_web_session,
    record_authenticated_access,
    register_account,
    web_session_username,
)


SESSION_COOKIE = "rag_public_session"
SESSION_MAX_AGE = 7 * 24 * 60 * 60


def _request_details(request: Request) -> tuple[str, str]:
    headers = {str(key).lower(): str(value) for key, value in request.headers.items()}
    forwarded_ip = (
        headers.get("cf-connecting-ip")
        or headers.get("true-client-ip")
        or headers.get("x-real-ip")
        or headers.get("x-forwarded-for", "").split(",", 1)[0].strip()
    )
    direct_ip = getattr(getattr(request, "client", None), "host", "")
    return (forwarded_ip or direct_ip or "unknown")[:128], headers.get("user-agent", "")


def _secure_cookie(request: Request) -> bool:
    forwarded_proto = request.headers.get("x-forwarded-proto", "").split(",", 1)[0]
    host = request.headers.get("x-forwarded-host") or request.headers.get("host", "")
    hostname = host.split(":", 1)[0].casefold()
    return (
        forwarded_proto.casefold() == "https"
        or request.url.scheme == "https"
        or hostname not in {"127.0.0.1", "localhost", ""}
    )


def _set_session_cookie(response: RedirectResponse, request: Request, token: str) -> None:
    response.set_cookie(
        SESSION_COOKIE,
        token,
        max_age=SESSION_MAX_AGE,
        httponly=True,
        secure=_secure_cookie(request),
        samesite="lax",
        path="/",
    )


async def _read_form(request: Request) -> dict[str, str]:
    body = await request.body()
    if len(body) > 16_384:
        return {}
    parsed = parse_qs(body.decode("utf-8", errors="replace"), keep_blank_values=True)
    return {key: values[-1] if values else "" for key, values in parsed.items()}


def render_auth_page(message: str = "", active_tab: str = "login") -> str:
    """Return the standalone, responsive authentication page."""
    safe_message = html.escape(message)
    is_register = active_tab == "register"
    message_html = (
        f'<div class="notice" role="alert">{safe_message}</div>' if safe_message else ""
    )
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="color-scheme" content="dark">
  <title>Sign in · Refractory Literature GraphRAG</title>
  <style>
    * {{ box-sizing: border-box; }}
    :root {{
      --bg: #090b12; --panel: rgba(20, 23, 34, .92); --line: #30364a;
      --text: #f4f5fb; --muted: #9aa3b8; --purple: #8b5cf6;
      --purple2: #6d5ce7; --cyan: #22d3ee; --danger: #fca5a5;
    }}
    body {{
      margin: 0; min-height: 100vh; color: var(--text);
      font: 15px/1.5 Inter, ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif;
      background:
        radial-gradient(circle at 18% 16%, rgba(109, 92, 231, .22), transparent 30rem),
        radial-gradient(circle at 84% 82%, rgba(34, 211, 238, .12), transparent 27rem), var(--bg);
      display: grid; place-items: center; padding: 28px;
    }}
    .shell {{ width: min(960px, 100%); display: grid; grid-template-columns: 1.05fr .95fr;
      border: 1px solid rgba(139, 148, 177, .22); border-radius: 26px; overflow: hidden;
      background: rgba(11, 13, 21, .78); box-shadow: 0 30px 90px rgba(0, 0, 0, .5);
      backdrop-filter: blur(18px); }}
    .intro {{ position: relative; min-height: 610px; padding: 58px 52px; overflow: hidden;
      background: linear-gradient(145deg, rgba(139, 92, 246, .18), rgba(13, 17, 28, .65)); }}
    .brand {{ display: flex; gap: 13px; align-items: center; font-weight: 750; letter-spacing: -.02em; }}
    .mark {{ width: 42px; height: 42px; border-radius: 13px; display: grid; place-items: center;
      background: linear-gradient(135deg, var(--purple), var(--cyan)); box-shadow: 0 8px 28px rgba(109, 92, 231, .35); }}
    .mark svg {{ width: 25px; height: 25px; }}
    h1 {{ margin: 94px 0 18px; font-size: clamp(2.15rem, 5vw, 3.55rem); line-height: 1.02;
      letter-spacing: -.055em; max-width: 560px; }}
    .intro p {{ max-width: 500px; color: #b8bfd0; font-size: 1.04rem; }}
    .features {{ margin-top: 48px; display: grid; gap: 15px; color: #d6d9e5; }}
    .feature {{ display: flex; align-items: center; gap: 12px; }}
    .dot {{ width: 8px; height: 8px; border-radius: 50%; background: var(--cyan); box-shadow: 0 0 14px var(--cyan); }}
    .network {{ position: absolute; width: 300px; height: 300px; right: -85px; bottom: -85px; opacity: .34; }}
    .auth {{ padding: 54px 46px; background: var(--panel); display: flex; align-items: center; }}
    .auth-inner {{ width: 100%; max-width: 365px; margin: auto; }}
    .auth h2 {{ margin: 0 0 8px; font-size: 1.85rem; letter-spacing: -.035em; }}
    .sub {{ margin: 0 0 27px; color: var(--muted); }}
    .tabs {{ display: grid; grid-template-columns: 1fr 1fr; gap: 5px; padding: 5px; margin-bottom: 25px;
      border: 1px solid var(--line); border-radius: 13px; background: #10131c; }}
    .tab {{ appearance: none; border: 0; border-radius: 9px; padding: 10px; color: var(--muted);
      background: transparent; cursor: pointer; font: inherit; font-weight: 700; }}
    .tab.active {{ color: white; background: #29243f; box-shadow: 0 3px 12px rgba(0,0,0,.25); }}
    form {{ display: none; }} form.active {{ display: block; }}
    label {{ display: block; margin: 15px 0 7px; color: #d8dbe5; font-size: .88rem; font-weight: 650; }}
    input {{ width: 100%; border: 1px solid var(--line); border-radius: 12px; padding: 13px 14px;
      color: white; background: #0e1119; outline: none; font: inherit; transition: .18s; }}
    input:focus {{ border-color: var(--purple); box-shadow: 0 0 0 3px rgba(139,92,246,.16); }}
    .submit {{ width: 100%; border: 0; border-radius: 12px; margin-top: 23px; padding: 13px 18px;
      color: white; background: linear-gradient(100deg, var(--purple2), #8b5cf6); cursor: pointer;
      font: inherit; font-weight: 750; box-shadow: 0 10px 28px rgba(109,92,231,.28); }}
    .submit:hover {{ filter: brightness(1.08); transform: translateY(-1px); }}
    .rules {{ margin-top: 14px; color: #7f899f; font-size: .78rem; }}
    .notice {{ margin-bottom: 18px; padding: 11px 13px; border: 1px solid rgba(252,165,165,.3);
      border-radius: 10px; color: #ffd0d0; background: rgba(127,29,29,.16); font-size: .87rem; }}
    .privacy {{ margin-top: 23px; color: #6f788c; text-align: center; font-size: .75rem; }}
    @media (max-width: 760px) {{
      body {{ padding: 14px; }} .shell {{ grid-template-columns: 1fr; }}
      .intro {{ min-height: auto; padding: 32px 28px; }} .intro h1 {{ margin-top: 42px; }}
      .features, .network {{ display: none; }} .auth {{ padding: 36px 25px 40px; }}
    }}
  </style>
</head>
<body>
  <main class="shell">
    <section class="intro">
      <div class="brand">
        <span class="mark" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="1.7"><circle cx="6" cy="7" r="2.2"/><circle cx="17.5" cy="5" r="2.2"/><circle cx="18" cy="17" r="2.2"/><circle cx="7" cy="18" r="2.2"/><path d="M8 7l7.3-1.5M7.3 9l-.1 6.8M9 17.5l6.8-.5M17.7 7.2l.2 7.6M8 8.4l8 7.2"/></svg></span>
        Refractory Literature GraphRAG
      </div>
      <h1>Materials knowledge, connected.</h1>
      <p>Explore literature, alloy compositions, processing routes, phases, mechanisms, and measured properties through retrieval and an interactive knowledge graph.</p>
      <div class="features">
        <div class="feature"><span class="dot"></span>Evidence-grounded literature answers</div>
        <div class="feature"><span class="dot"></span>Interactive 2D and 3D knowledge graphs</div>
        <div class="feature"><span class="dot"></span>Page-level PDF references</div>
      </div>
      <svg class="network" viewBox="0 0 300 300" fill="none" stroke="#a78bfa"><path d="M20 196L94 101l67 64 78-112M94 101l31 142 36-78 106 50M20 196l105 47 114-190M161 165l78-112"/><g fill="#22d3ee" stroke="none"><circle cx="20" cy="196" r="6"/><circle cx="94" cy="101" r="8"/><circle cx="125" cy="243" r="6"/><circle cx="161" cy="165" r="9"/><circle cx="239" cy="53" r="7"/><circle cx="267" cy="215" r="6"/></g></svg>
    </section>
    <section class="auth">
      <div class="auth-inner">
        <h2>Welcome</h2>
        <p class="sub">Sign in or create an account to continue.</p>
        {message_html}
        <div class="tabs" role="tablist">
          <button type="button" class="tab {'active' if not is_register else ''}" data-tab="login">Sign In</button>
          <button type="button" class="tab {'active' if is_register else ''}" data-tab="register">Create Account</button>
        </div>
        <form id="login" class="{'active' if not is_register else ''}" method="post" action="/auth/login">
          <label for="login-user">Username</label>
          <input id="login-user" name="username" autocomplete="username" required minlength="3" maxlength="32">
          <label for="login-pass">Password</label>
          <input id="login-pass" type="password" name="password" autocomplete="current-password" required minlength="8" maxlength="256">
          <button class="submit" type="submit">Sign In</button>
        </form>
        <form id="register" class="{'active' if is_register else ''}" method="post" action="/auth/register">
          <label for="register-user">Choose a username</label>
          <input id="register-user" name="username" autocomplete="username" required minlength="3" maxlength="32" pattern="[A-Za-z0-9_.-]+">
          <label for="register-pass">Create a password</label>
          <input id="register-pass" type="password" name="password" autocomplete="new-password" required minlength="8" maxlength="256">
          <label for="confirm-pass">Confirm password</label>
          <input id="confirm-pass" type="password" name="confirm_password" autocomplete="new-password" required minlength="8" maxlength="256">
          <button class="submit" type="submit">Create Account</button>
          <div class="rules">Username: 3–32 letters, numbers, dots, underscores, or hyphens. Password: at least 8 characters.</div>
        </form>
        <div class="privacy">Passwords are salted and hashed. Plaintext passwords are never stored.</div>
      </div>
    </section>
  </main>
  <script>
    const tabs = document.querySelectorAll('.tab');
    tabs.forEach(tab => tab.addEventListener('click', () => {{
      tabs.forEach(item => item.classList.toggle('active', item === tab));
      document.querySelectorAll('form').forEach(form => form.classList.toggle('active', form.id === tab.dataset.tab));
      const first = document.querySelector(`#${{tab.dataset.tab}} input`); if (first) first.focus();
    }}));
  </script>
</body>
</html>"""


def create_public_application(blocks: gr.Blocks) -> FastAPI:
    web_app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)
    # Public traffic passes through a tunnel. Compress Gradio configuration,
    # graph HTML and API responses before they cross that slower link.
    web_app.add_middleware(GZipMiddleware, minimum_size=1000, compresslevel=5)

    def current_user(request: Request) -> str | None:
        return web_session_username(request.cookies.get(SESSION_COOKIE))

    @web_app.get("/", response_class=HTMLResponse)
    async def auth_home(request: Request):
        if current_user(request):
            return RedirectResponse("/app/", status_code=303)
        return HTMLResponse(render_auth_page())

    @web_app.post("/auth/login")
    async def login(request: Request):
        form = await _read_form(request)
        username = form.get("username", "").strip()
        if not authenticate_account(username, form.get("password", "")):
            return HTMLResponse(
                render_auth_page("Incorrect username or password.", "login"),
                status_code=401,
            )
        token = create_web_session(username, SESSION_MAX_AGE)
        ip_address, user_agent = _request_details(request)
        record_authenticated_access(username, ip_address, user_agent)
        response = RedirectResponse("/app/", status_code=303)
        _set_session_cookie(response, request, token)
        return response

    @web_app.post("/auth/register")
    async def register(request: Request):
        form = await _read_form(request)
        username = form.get("username", "").strip()
        password = form.get("password", "")
        if password != form.get("confirm_password", ""):
            return HTMLResponse(
                render_auth_page("Passwords do not match.", "register"),
                status_code=400,
            )
        created, message = register_account(username, password)
        if not created:
            return HTMLResponse(render_auth_page(message, "register"), status_code=400)
        token = create_web_session(username, SESSION_MAX_AGE)
        ip_address, user_agent = _request_details(request)
        record_authenticated_access(username, ip_address, user_agent)
        response = RedirectResponse("/app/", status_code=303)
        _set_session_cookie(response, request, token)
        return response

    @web_app.post("/auth/logout")
    async def logout(request: Request):
        token = request.cookies.get(SESSION_COOKIE)
        delete_web_session(token)
        response = RedirectResponse("/", status_code=303)
        response.delete_cookie(SESSION_COOKIE, path="/")
        return response

    @web_app.get("/health")
    async def health():
        return {"status": "ok"}

    return gr.mount_gradio_app(
        web_app,
        blocks,
        path="/app",
        auth_dependency=current_user,
        show_api=False,
    )


def run_public_server(blocks: gr.Blocks, server_port: int) -> None:
    blocks.queue(default_concurrency_limit=4)
    web_app = create_public_application(blocks)
    uvicorn.run(
        web_app,
        host="127.0.0.1",
        port=int(server_port),
        log_level="warning",
        access_log=False,
        proxy_headers=True,
        forwarded_allow_ips="127.0.0.1",
    )
