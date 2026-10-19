# Refractory Literature RAG

A local RAG and GraphRAG system for literature on refractory metals, refractory alloys, and high-temperature materials. The project provides full-text retrieval, knowledge-graph retrieval, traceable evidence citations, interactive graph visualization, and resumable batch extraction workflows.

## Dataset

The curated dataset contains 5,169 documents:

| Dataset | Count | Directory |
| --- | ---: | --- |
| Literature in Markdown format | 5,159 | `data/markdown_bundle/literature_5159/` |
| Patents in Markdown format | 10 | `data/markdown_bundle/patents_10/` |
| GraphRAG chunk extraction files | 9,482 | `data/graph/chunk_extractions/` |
| Paper-level graph files | 5,169 | `data/graph/paper_graphs/` |

All 10 patent files belong to patent `CN102719713A`. The 5,169 document IDs map one-to-one to the 5,169 paper-level graph JSON files. GraphRAG extraction failures are excluded from the published dataset and retained only in the original local workspace.

Verify the published dataset with:

```powershell
python scripts\verify_github_dataset.py
```

See [data/README.md](data/README.md) for detailed dataset documentation.

## Features

- SQLite FTS full-text search with a dynamic relevance threshold instead of a fixed small Top-K cutoff.
- Joint retrieval across GraphRAG entities, processes, organizations, properties, and evidence relationships.
- Citation coverage checks requiring every deduplicated retrieved reference to be cited in the answer.
- `DeepSeek-V4.1-Flash-1017` as the displayed answer model, using the API model ID `deepseek-flash`.
- Up to 4,000 output tokens per answer.
- Interactive 2D and 3D knowledge graphs with node filtering, neighborhood expansion, and source-evidence inspection.
- Resumable document chunking and graph extraction, including retry and progress-monitoring utilities.

## Project Structure

```text
refractory-literature-rag/
|-- app.py                         # Gradio interface and question-answering workflow
|-- rag_store.py                   # Full-text indexing, retrieval, citations, and feedback data
|-- graph_store.py                 # Graph database, graph retrieval, and visualization
|-- prompts.py                     # Question-answering and citation prompts
|-- graph_prompts.py               # GraphRAG extraction prompts
|-- account_store.py               # Optional local account support
|-- config.example.json            # Configuration template without credentials
|-- requirements.txt               # Python dependencies
|-- package.json                   # Dependencies for the 3D graph front end
|-- start_app.bat                  # Windows local startup script
|-- scripts/                       # Build, extraction, retry, deduplication, and validation tools
|-- tests/                         # Unit tests
|-- data/
|   |-- markdown_bundle/           # The 5,169 published Markdown documents
|   |-- graph/chunk_extractions/   # Chunk-level GraphRAG JSON files
|   `-- graph/paper_graphs/        # Merged paper-level graph JSON files
`-- docs/GITHUB_UPLOAD.md          # GitHub upload instructions
```

## Installation

Python 3.11 to 3.13 is recommended. Python 3.14 may also work, although some third-party packages can emit compatibility warnings.

```powershell
cd C:\path\to\refractory-literature-rag
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
npm.cmd install
Copy-Item config.example.json config.json
```

Edit the local `config.json` file and add your API key. This file is excluded by `.gitignore` and must not be committed.

```json
{
  "model": "deepseek-flash",
  "model_display_name": "DeepSeek-V4.1-Flash-1017",
  "base_url": "https://api.deepseek.com",
  "api_key": "YOUR_DEEPSEEK_API_KEY",
  "max_tokens": 4000
}
```

## Running the Application

Full retrieval requires two runtime databases. Download `literature.db` and `graph.db` from the project's GitHub Releases, then place them in `data/index/` and `data/graph/`, respectively. The interface can start without these databases, but the complete 5,169-document retrieval capability will not be available.

On Windows, run:

```powershell
.\start_app.bat
```

The application starts with port 7860 and automatically tries subsequent ports if that port is occupied.

You can also start it directly:

```powershell
python app.py
```

## GraphRAG Batch Processing

Check extraction progress:

```powershell
.\check_graphrag_progress.bat
```

Continue processing documents that have not started or previously failed:

```powershell
.\continue_graphrag_unstarted.bat
```

Key scripts:

- `scripts/extract_graphrag.py`: document chunking and graph extraction.
- `scripts/run_graphrag_resilient.py`: fault-tolerant batch processing, checkpointing, and retry handling.
- `scripts/graph_batch_progress.py`: extraction progress statistics.
- `scripts/rebuild_graph_from_json.py`: rebuilds the graph database from paper-level JSON files.
- `scripts/remove_duplicate_files.py`: safely removes duplicate source files based on a generated report.
- `scripts/verify_github_dataset.py`: validates published file counts and document-ID mappings.

See [GRAPH_NAMING_RULES.md](GRAPH_NAMING_RULES.md) for entity naming and graph conventions.

## Large Files and GitHub

The two runtime SQLite databases should not be committed to standard Git history:

- `data/index/literature.db`: approximately 1.37 GB.
- `data/graph/graph.db`: approximately 742 MB.

Both are excluded by `.gitignore`. Distribute ready-to-use databases as GitHub Release assets, Git LFS objects, or through an external dataset host. The regular repository contains the Markdown documents, chunk-level JSON files, and paper-level graph JSON files.

See [docs/GITHUB_UPLOAD.md](docs/GITHUB_UPLOAD.md) for the complete upload procedure.

## Testing

```powershell
python -m unittest discover -s tests -v
python -m py_compile app.py rag_store.py graph_store.py
python scripts\verify_github_dataset.py
```

## Data and Licensing

The source code, article text, patent text, and model-generated structured data may be subject to different license terms. Before publishing a repository, verify redistribution rights for every source document. If those rights cannot be confirmed, use a private repository or publish only the code, document IDs, metadata, and reproducible processing scripts.

Never commit API keys, account databases, chat histories, or access logs.
