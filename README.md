# Refractory Literature RAG

面向难熔金属、难熔合金和高温材料文献的本地 RAG/GraphRAG 系统。项目提供全文检索、知识图谱关系检索、可追溯证据引用、交互式图谱展示以及断点续跑的批量抽取流程。

## 当前数据集

整理后的有效数据集共 5169 篇：

| 数据 | 数量 | 目录 |
| --- | ---: | --- |
| 普通文献 Markdown | 5159 | `data/markdown_bundle/literature_5159/` |
| 专利 Markdown | 10 | `data/markdown_bundle/patents_10/` |
| GraphRAG 切片抽取 JSON | 9482 | `data/graph/chunk_extractions/` |
| 论文级图谱 JSON | 5169 | `data/graph/paper_graphs/` |

第 10 篇专利为 `CN102719713A`。5169 个文档 ID 与 5169 个论文级图谱 JSON 一一对应。9 个 GraphRAG 失败项没有进入发布数据集，原始工作目录仍保留在本机。

```powershell
python scripts\verify_github_dataset.py
```

详细数据说明见 [data/README.md](data/README.md)。

## 主要功能

- SQLite FTS 全文检索与动态相关性阈值，不固定截取少量 Top-K。
- GraphRAG 实体、工艺、组织、性能和证据关系联合检索。
- 回答引用覆盖检查：检索到的去重参考文献均要求在答案中引用。
- 回答模型显示为 `DeepSeek-V4.1-Flash-1017`，API 模型 ID 为 `deepseek-flash`。
- 单次回答最大输出为 4000 tokens。
- 2D/3D 交互式知识图谱、节点筛选、邻域扩展和原文证据查看。
- 文献切片和图谱抽取支持断点续跑、失败重试和进度检查。

## 项目结构

```text
refractory-literature-rag/
├─ app.py                         # Gradio 主界面与问答流程
├─ rag_store.py                   # 全文索引、检索、引用和反馈数据
├─ graph_store.py                 # 图数据库、图检索和可视化
├─ prompts.py                     # 问答与引用提示词
├─ graph_prompts.py               # GraphRAG 抽取提示词
├─ account_store.py               # 可选的本地账户功能
├─ config.example.json            # 无密钥的配置模板
├─ requirements.txt               # Python 依赖
├─ package.json                   # 3D 图谱前端依赖
├─ start_app.bat                  # Windows 本地启动脚本
├─ scripts/                       # 构建、抽取、重试、去重和校验脚本
├─ tests/                         # 单元测试
├─ data/
│  ├─ markdown_bundle/            # GitHub 发布用的 5169 篇 Markdown
│  ├─ graph/chunk_extractions/    # 切片级 GraphRAG JSON
│  ├─ graph/paper_graphs/         # 合并后的论文级图谱 JSON
│  └─ structured/                 # 早期结构化分析数据
└─ docs/GITHUB_UPLOAD.md          # GitHub 上传说明
```

## 安装

建议使用 Python 3.11–3.13。当前机器使用 Python 3.14，也可以运行，但部分第三方依赖可能显示兼容性警告。

```powershell
cd C:\path\to\refractory-literature-rag
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
npm.cmd install
Copy-Item config.example.json config.json
```

编辑本地 `config.json`，填入自己的 API Key。`config.json` 已被 `.gitignore` 排除，不会上传到 GitHub：

```json
{
  "model": "deepseek-flash",
  "model_display_name": "DeepSeek-V4.1-Flash-1017",
  "base_url": "https://api.deepseek.com",
  "api_key": "YOUR_DEEPSEEK_API_KEY",
  "max_tokens": 4000
}
```

## 启动

完整检索需要两个运行时数据库。当前工作机已经具备这些数据库；新的 GitHub 克隆需先从项目 Release 下载 `literature.db` 和 `graph.db`，分别放入 `data/index/` 与 `data/graph/`。数据库未安装时，界面仍可启动，但不会拥有完整的 5169 篇检索能力。

Windows：

```powershell
.\start_app.bat
```

程序默认从端口 7860 开始寻找可用端口；如果 7860 已被占用，会自动使用 7861、7862 等端口。

也可以直接运行：

```powershell
python app.py
```

## GraphRAG 批量处理

查看进度：

```powershell
.\check_graphrag_progress.bat
```

继续处理未开始或失败的文献：

```powershell
.\continue_graphrag_unstarted.bat
```

主要脚本：

- `scripts/extract_graphrag.py`：文献切片和图谱抽取。
- `scripts/run_graphrag_resilient.py`：批量容错、断点续跑和失败重试。
- `scripts/graph_batch_progress.py`：处理进度统计。
- `scripts/rebuild_graph_from_json.py`：从论文级 JSON 重建图数据库。
- `scripts/remove_duplicate_files.py`：按报告安全清理重复源文件。
- `scripts/verify_github_dataset.py`：检查 GitHub 数据包数量和 ID 对应关系。

实体命名和图谱规范见 [GRAPH_NAMING_RULES.md](GRAPH_NAMING_RULES.md)。

## 大文件与 GitHub

两个运行时 SQLite 文件不应直接加入普通 Git 历史：

- `data/index/literature.db`：约 1.37 GB。
- `data/graph/graph.db`：约 742 MB。

它们已被 `.gitignore` 排除。需要分发开箱即用数据库时，请作为 GitHub Release 附件、Git LFS 对象或外部数据集发布。普通仓库保留 Markdown、切片 JSON 和论文级图谱 JSON。

完整上传步骤见 [docs/GITHUB_UPLOAD.md](docs/GITHUB_UPLOAD.md)。

## 测试

```powershell
python -m unittest discover -s tests -v
python -m py_compile app.py rag_store.py graph_store.py
python scripts\verify_github_dataset.py
```

## 数据和版权说明

代码、论文全文、专利文本和模型生成的结构化数据可能具有不同的许可条件。公开仓库前请逐项确认原始文献的再分发权限；无法确认时建议使用私有仓库，或只发布代码、文档 ID、元数据和可重建脚本。API Key、账户数据库、聊天记录和访问日志不得提交。
