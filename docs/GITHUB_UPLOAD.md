# GitHub 上传指南

## 推荐发布结构

普通 Git 仓库中提交：

- Python、BAT、PowerShell 源码；
- `README.md`、`data/README.md` 和其他说明文档；
- `data/markdown_bundle/` 中的 5169 篇发布用 Markdown；
- `data/graph/chunk_extractions/` 中的切片 JSON；
- `data/graph/paper_graphs/` 中的论文级图谱 JSON；
- `data/structured/` 中的小型结构化文件；
- 测试和无密钥配置模板。

不要提交：

- `config.json` 和任何 API Key；
- `data/index/literature.db` 与 `data/graph/graph.db`；
- 账户、聊天记录、上传文件、日志、缓存和 `node_modules`；
- 原始工作集 `data/markdown/`，因为发布集已经位于 `data/markdown_bundle/`。

GitHub 普通 Git 会阻止超过 100 MiB 的单个文件，浏览器上传还限制为每个文件 25 MiB、每次最多 100 个文件。因此本项目不适合通过网页逐个上传，建议使用 GitHub Desktop 或 Git 命令行。

官方说明：

- https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github
- https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-git-large-file-storage

## 上传前检查

```powershell
python scripts\verify_github_dataset.py
python -m unittest discover -s tests -v
```

确认 `config.json` 不在待提交文件中。

## 使用 Git 命令行

当前电脑如果还没有 Git，请先安装 Git for Windows，或者直接安装 GitHub Desktop。安装后在项目目录运行：

```powershell
git init
git add .
git status
git commit -m "Initial release: code and 5169-document GraphRAG dataset"
git branch -M main
git remote add origin https://github.com/YOUR_ACCOUNT/YOUR_REPOSITORY.git
git push -u origin main
```

第一次提交前必须查看 `git status`，确认没有 `config.json`、SQLite 数据库、聊天记录和日志。

## SQLite 数据库的发布方式

如果希望用户克隆后无需重建即可运行，可以在 GitHub 仓库创建 Release，并将下面两个文件作为附件上传：

```text
data/index/literature.db
data/graph/graph.db
```

Release 页面应提示用户下载后放回同名目录。没有这两个数据库时，仓库中的 Markdown 和 JSON 数据仍然完整，但应用无法直接获得完整全文索引和聚合图查询能力。

也可以使用 Git LFS。不要先把大数据库提交进普通 Git，再改用 LFS；这样大文件仍会留在 Git 历史中。

## 公开发布前的版权检查

5159 篇论文 Markdown 可能包含受版权保护的全文。若没有明确的公开再分发授权，请选择私有仓库，或从公开版本中移除 `data/markdown_bundle/`，只保留文档 ID、书目信息、图谱结构和重建脚本。
