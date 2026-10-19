# 数据目录说明

## GitHub 发布数据

```text
markdown_bundle/
├─ literature_5159/   # 5159 篇普通文献 Markdown
└─ patents_10/        # 10 篇专利 Markdown

graph/
├─ chunk_extractions/ # 9482 个切片级 GraphRAG JSON
└─ paper_graphs/      # 5169 个论文级图谱 JSON

structured/           # 175 个早期结构化分析文件
```

Markdown 文件名和论文级图谱文件名的前 16 位为稳定文档 ID。发布集中的 5169 个文档 ID与 `paper_graphs` 完全对应。

## 本地运行数据（不提交普通 Git）

```text
index/literature.db   # SQLite FTS 全文索引，约 1.37 GB
graph/graph.db        # SQLite 知识图谱，约 742 MB
markdown/             # 原始工作集，包含未进入最终发布集的文件
archive/              # 历史归档
auth/                 # 本地账户数据
uploads/              # 用户上传文件
ocr-temp/             # OCR 临时文件
```

这些目录或文件已在 `.gitignore` 中排除。若要提供现成数据库，可单独上传为 GitHub Release 附件或使用 Git LFS，不要直接放进普通 Git 历史。

## 完整性检查

```powershell
python scripts\verify_github_dataset.py
```

校验内容包括：

- 普通文献为 5159 篇；
- 专利为 10 篇；
- 总 Markdown 为 5169 篇；
- 论文级图谱为 5169 个；
- Markdown 与论文级图谱文档 ID 完全一致；
- 切片级 GraphRAG JSON 为 9482 个，且全部属于发布集文档；
- `CN102719713A` 已归入专利集合。

## 数据许可

本目录可能包含受版权或数据库许可约束的文献内容。公开发布前必须确认你拥有相应的存储和再分发权。不能确认时，请仅发布代码、元数据、文档 ID 和生成脚本。
