# E.L.Y.S.I.U.M - Home Server

E.L.Y.S.I.U.M is a modular, AI-augmented home server and CLI toolkit built with FastAPI, LangChain, and Python. It provides server health monitoring, email automation, AI agent configuration, NVIDIA LLM integration, and a Python CLI interface.

## Technology Stack

### Active Dependencies
- **Core**: pydantic>=2.12.5, python-dotenv>=1.2.2, requests>=2.32.5
- **AI & Agents**: openai>=2.41.1
- **Encryption**: cryptography>=49.0.0
- **Framework**: fastapi[standard]>=0.139.0
- **System Monitoring**: psutil>=7.2.2
- **Package Manager**: uv

### Planned/Aspirational
- **Framework**: Typer, Textual (TUI)
- **AI & Agents**: LangChain, LangChain-Groq, LangChain-Ollama, LangGraph
- **Task Queue**: Celery with Redis
- **Email**: aiosmtplib
- **Audio**: pyaudio, sounddevice, webrtcvad-wheels
- **Utilities**: numpy, rich, tqdm

---

## Project Architecture

```
E.L.Y.S.I.U.M/
├── .python-version            # Python version specification (3.12)
├── .gitignore                 # Git ignore rules
├── uv.lock                    # uv dependency lockfile
├── pyproject.toml             # Project metadata and dependencies (uv)
├── install.sh                 # Project installation script
├── main.py                    # Top-level entry point (currently empty/placeholder)

│
├── Server/                    # FastAPI web server
│   ├── __init__.py            # Package init
│   ├── main.py                # FastAPI app (lifespan, SSE, WebSocket)
│   └── routes/                # Route blueprints (placeholder)
│
├── Agents/                    # AI Agent implementations
│   ├── __init__.py            # Load_Agent class (config initialization, model roulette)
│   ├── agent.py               # Agents class (deep, web, worker, council stubs)
│   └── nvidia.py              # NvidiaAgent class (NVIDIA LLM via OpenAI SDK)
│
├── ElysiumCli/                # Python CLI tool
│   ├── main.py                # CLI entry point
│   ├── Readme.md              # CLI documentation
│   ├── Config/                # CLI configuration
│   │   ├── __init__.py
│   │   ├── cli_config.py      # Config management with Pydantic & encryption
│   │   ├── config.json        # Default CLI settings
│   │   └── config.log         # CLI activity log
│   ├── commands/              # CLI commands
│   │   ├── __init__.py        # Package init
│   │   └── elysium_info.py    # Version/status/info/update commands
│   ├── external/              # External integrations (placeholder)
│   └── internal/              # Core modules
│       ├── __init__.py        # Exports custom exceptions
│       ├── core/
│       │   └── core.py        # CLI REPL loop & command routing
│       └── Errors/
│           └── errors.py      # CLI custom exceptions
│
├── ElysiumConfig/             # Configuration management
│   ├── __init__.py            # Validates ~/.config/E.L.Y.S.I.U.M/ existence on import
│   ├── model_config.py        # AI model configuration manager (with encryption)
│   ├── path_config.py         # Path mapping config loader & GitHub downloader
│   ├── additionals.py         # Additionals plug-and-play skill/tool downloader & updater
│   ├── updater.py             # Updater class — E.L.Y.S.I.U.M version check (local vs cloud config)
│   ├── config.json            # Base system metadata JSON (+ additionals config URL)
│   └── path_config.json       # Predefined local path settings (+ additionals paths)
│
├── Linux/                     # Linux-native system utilities
│   ├── __init__.py            # Package init
│   ├── system.py              # Linux class — storage/RAM/cache inspection (psutil)
│   └── todo.txt               # Planning notes for future Linux-native features
│
├── Security/                  # Security & encryption modules
│   └── encryption/
│       ├── __init__.py
│       └── crypto.py          # Fernet key generation, encrypt, decrypt, getkey
│
├── Workers/                   # Background worker framework
│   ├── __init__.py
│   ├── worker.py              # Worker class with threading & config/log paths
│   └── workers_preview.json   # Worker startup configuration
│
└── Errors/                    # Centralized error handling
    └── errors.py              # Custom server exceptions
```

---

## Directory & File Purpose

### Root Level

| File | Purpose |
|------|---------|
| `pyproject.toml` | Project metadata (name: elysium, version: 0.0.7) |
| `uv.lock` | uv dependency lockfile |
| `install.sh` | Installation and environment setup script |
| `main.py` | Top-level entry point (currently empty, reserved for future use) |
| `.python-version` | Specifies Python version (3.12) |
| `.gitignore` | Git ignore rules |

### `Server/` - FastAPI Web Server

| File | Purpose |
|------|---------|
| `__init__.py` | Package init |
| `main.py` | FastAPI application with `lifespan` handler, `GET /` health check, `GET /read` SSE log streaming endpoint, `WebSocket /ws` echo endpoint |
| `routes/` | Route blueprint directory (currently empty, placeholder for future API routes) |

### `ElysiumConfig/` - Configuration

| File | Purpose |
|------|---------|
| `__init__.py` | Validates `~/.config/E.L.Y.S.I.U.M/` exists on import via `path_config.check_for_eLysium_path()`; raises `ConfigFileMissing` if not found |
| `model_config.py` | Manages AI model settings, API key injection (with Fernet encryption), config download from GitHub |
| `additionals.py` | Additionals plug-and-play system: downloads/updates config from `Elysium_additionals` repo, version checks, auto-updates on missing config |
| `updater.py` | `Updater` class — compares local `config.json` against the cloud copy fetched from the `url` field. `_read_local_config()` reads `~/.E.L.Y.S.I.U.M/ElysiumConfig/config.json`; `_get_cloud_config()` downloads the cloud config; `check_update()` compares versions and returns an `updates` dict; `update_elysium()` orchestrates the full update (delete old, clone repo, `uv sync`). A module-level `Updater()` runs `update_elysium()` on import. Designed so the agent can self-update at will or when the user prompts it |
| `config.json` | Base system metadata (version: 0.0.7, status: development, version_name: omega-cooper, stable: "False", `url` pointing to the raw cloud `config.json`, `repo` pointing to the GitHub repo, `last_development_changes`) plus `elysium_additionals_config` with download URL |
| `path_config.py` | Core path management, path listing, additionals path config, and GitHub config downloader |
| `path_config.json` | Predefined directory path mappings (Root, Log, Skill, Memory, Config) and additionals paths (Root, Memory, Config) |

### `ElysiumCli/` - CLI Tool

| File | Purpose |
|------|---------|
| `main.py` | CLI entry point — argparse program named `romeo` with subcommands (version, status, dev, version_name, is_stable, info, check_version, update) |
| `internal/core/core.py` | Legacy CLI REPL loop (`:>` prompt) and command routing (currently unused by `main.py`) |
| `internal/__init__.py` | Exports `ConfigNotFound`, `InvalidArgsFound` exceptions |
| `internal/Errors/errors.py` | CLI-specific exceptions (`ConfigNotFound`, `InvalidArgsFound`) |
| `Config/cli_config.py` | CLI-specific configuration management with Pydantic validation, encryption, argparse flags (`-make`, `-over_ride`, `-add_config`) |
| `Config/config.log` | CLI activity log |
| `commands/__init__.py` | Package init |
| `commands/elysium_info.py` | Version/status/info/update command implementations (reads `config.json`, calls `Updater`) |

### `Agents/` - AI Agents

| File | Purpose |
|------|---------|
| `__init__.py` | `Load_Agent` class: initializes with `Elysium_Model_Config`, provides `model_roulet(priority_provider)` for random model selection and `model_key(provider, model)` for API key retrieval |
| `agent.py` | `Agents` class stub with methods: `deep_agent`, `web_agent`, `worker_agent`, `agents_council`, `loop` |
| `nvidia.py` | `NvidiaAgent` class: uses `OpenAI` SDK with `base_url="https://integrate.api.nvidia.com/v1"`, supports chat with `reasoning={'effort': 'high'}` |

### `Security/` - Security Modules

| File | Purpose |
|------|---------|
| `encryption/__init__.py` | Package init |
| `encryption/crypto.py` | Fernet key generation (`generate_key`), encryption (`encrypt`), decryption (`decrypt`), key retrieval (`getkey`) with JSON key store and duplicate detection by provider+model |

### `Workers/` - Background Workers

| File | Purpose |
|------|---------|
| `__init__.py` | Package init |
| `worker.py` | `worker` class (placeholder) with auto-created config/log paths under `~/.config/E.L.Y.S.I.U.M/` |
| `workers_preview.json` | Worker startup configuration (id, execution_time, repeat) |

### `Errors/` - Error Handling

| File | Purpose |
|------|---------|
| `Errors/errors.py` | Server-level exceptions (`ProviderNotGiven`, `ModelNameNotGiven`, `ApiKeyNotGiven`, `ConfigFileMissing`, `ProviderNotFound`, `DirectoryNotGiven`, `KeysNotFound`, `AdditionalsNotFound`, `AdditionalsNotInstalled`) |

### `Linux/` - Linux-Native

| File | Purpose |
|------|---------|
| `__init__.py` | Package init for the `Linux/` namespace reserved for Linux-native functionality |
| `system.py` | `Linux` class — system metrics via `psutil`/`subprocess`/`shutil`: `_get_storage()`, `_get_system_ram()`, `_get_cache_storage()`, `_get_cahe_storage_usage()`, `get_apps()`, `get_cache()` |
| `todo.txt` | Planning notes for future Linux-native features (mobile→laptop input sync, sha256 verification, expanded ROMEO CLI, worker/task scheduling, autonomous idle checks, CLI open flag) |

---

## Code Flow

1. **CLI Startup** (`ElysiumCli/main.py`):
   - Builds an `argparse` parser with subcommands via `build_parser()`
   - Imports from `ElysiumCli.commands.elysium_info` for all subcommand implementations
   - Supports 8 subcommands: `version`, `status`, `dev`, `version_name`, `is_stable`, `info`, `check_version`, `update`
   - Also supports a `-test` debug flag
   - The legacy REPL (`internal/core/core.py` with `:>` prompt, `-chat`, `-download_config`, `-insert_api`) is no longer wired to the entry point

2. **Configuration Initialization** (`ElysiumConfig/__init__.py`):
   - Validates `~/.config/E.L.Y.S.I.U.M/` exists on import
   - Raises `ConfigFileMissing` if not found

3. **Model Configuration** (`ElysiumConfig/model_config.py`):
   - Resolves paths dynamically using `path_config.py` (pointing to `~/.config/E.L.Y.S.I.U.M/`)
   - Validates `model_config.json` existence under dynamic config path
   - Downloads default config from GitHub if missing
   - Injects API keys for specified providers/models, encrypted via `Security.encryption.crypto`
   - `insert_api_key(provider_name, model_name, api_key)` generates encryption key and stores encrypted API key
   - `load_model(required_provider, required_model)` returns decrypted API key with provider/model info

4. **FastAPI Server Flow** (`Server/main.py`):
   - `lifespan` context manager logs server boot on startup
   - `GET /` returns `{"status": 200}` health check (uses `status.HTTP_200_OK`)
   - `GET /read` streams log file via SSE (`text/event-stream`) using `StreamingResponse` + `logstream()` generator; sources from `~/test/server.log`
   - `WebSocket /ws` accepts connections and echoes received text with `"Echo = {data}"` prefix
   - `routes/` directory reserved for future API route blueprints

5. **AI Agent Flow** (`Agents/__init__.py`):
   - `Load_Agent` class (defined in `Agents/__init__.py`, re-exported via `Agents/nvidia.py`) initializes `Elysium_Model_Config` on instantiation
   - `model_roulet(priority_provider="")` returns a random model/provider pair, with optional priority provider
   - `model_key(provider, model)` retrieves and decrypts the API key via `getkey()` + `decrypt()`

6. **NvidiaAgent Flow** (`Agents/nvidia.py`):
   - `NvidiaAgent.__init__(agent)` calls `model_roulet(priority_provider="nvidia")` to select a random NVIDIA model
   - Creates an `OpenAI` client configured with `base_url="https://integrate.api.nvidia.com/v1"`
   - `chat(prompt)` calls the OpenAI Responses API with `reasoning={'effort': 'high'}` and returns `response.output_text`

7. **Encryption Flow** (`Security/encryption/crypto.py`):
   - `generate_key(module, provider_name, model_name)` creates a Fernet key, stores it in `~/.config/E.L.Y.S.I.U.M/Config/Security/encryption/keys.json`
   - Duplicate provider+model detection updates existing keys rather than creating duplicates
   - `encrypt(item, key)` / `decrypt(item, key)` wrap Fernet symmetric encryption
   - `getkey(provider_name, model_name)` looks up key from `keys.json` by provider+model; raises `KeysNotFound` if missing
   - Used by `model_config.py` and `cli_config.py` to encrypt stored API keys

8. **Worker Flow** (`Workers/worker.py`):
   - On import, auto-creates `~/.config/E.L.Y.S.I.U.M/Config/worker/` and `Logs/worker/` directories
   - `worker` class with stub methods: `check_config`, `add_config`, `stats`, `load_config`
   - `workers_preview.json` defines startup behavior (id, execution_time, repeat)
   - **Note**: Contains stale imports (`Elysium_Config` instead of `ElysiumConfig`) — currently non-functional without fixes

9. **Updater Flow** (`ElysiumConfig/updater.py`):
   - `Updater.__init__()` sets `LOCALCONFIG` to `~/.E.L.Y.S.I.U.M/ElysiumConfig/config.json` and eagerly fetches `CLOUDCONFIG` via `_get_cloud_config()`
   - `_read_local_config()` loads the local `config.json`
   - `_get_cloud_config()` reads the `elysium.url` field from the local config and `requests.get()`s the cloud `config.json`; returns `{}` on any error (logged at DEBUG)
   - `check_update()` compares `LocalMetadata['version']` against `CloudMetadata['version']`; if the cloud version is newer, it logs "Update is Available" (and "Major Update is Available!" when the `version_name` also changed) and returns an `updates` dict containing `version`, `version_name`, `stable`, `url`, `repo`, and `latest_changes`; otherwise logs "No update available" and returns `{}`
   - An `update_elysium()` method orchestrates the full update: checks for updates, deletes the old `~/.E.L.Y.S.I.U.M/` directory, clones the latest from GitHub, and runs `uv sync` to reinstall dependencies
   - A module-level `updater = Updater(); updater.update_elysium()` runs at import time, so an auto-update fires on every instance the module is loaded
   - Designed so the AI agent can call `Updater` for autonomous self-updates, or be triggered by user prompts

10. **Additionals Flow** (`ElysiumConfig/additionals.py`):

   **Overview** — The Additionals system is a plug-and-play skill/tool downloader that lets E.L.Y.S.I.U.M learn new capabilities at runtime. Additionals are defined in a separate [`Elysium_additionals`](https://github.com/Shishir-Kc/Elysium_additionals) repo.

   **Import-time Initialization** (runs automatically when the module is first imported):
   - `load_additionals_config()` reads `ElysiumConfig/config.json` to get `elysium_additionals_config.download_url`
   - `show_elysium_paths(all=True)` resolves additionals paths from `path_config.json`
   - `ADDITIONALSROOTPATH` set to `~/.config/E.L.Y.S.I.U.M/Additionals/`
   - If `Additionals/config.json` is missing locally, auto-downloads it from the GitHub repo
   - Module-level `additionals = Additionals()` singleton is created

   **Workflow Diagram:**
   ```
   GitHub Elysium_additionals repo
            │
            ▼
   download_additionals_config()   ──►  ~/.../Additionals/config.json
            │                                     │
            ▼                                     ▼
   Additionals.check_update()     compares     Local additionals config
            │                       versions     (each entry has a version field)
            ▼
   Returns dict of available updates
            │
            ▼
   Additionals.download(additional="SuperMemory")
      1. _update_config() — merges cloud version into local config
      2. Creates additional directory from `path` field
      3. Downloads main additional files via download_config()
      4. Iterates `dependency` list — downloads each dependency
      5. _write_downloaded_additionals() — logs to settings.json
   ```

   **`Additionals` Class Methods:**

   | Method | Description |
   |--------|-------------|
   | `additionals()` | Returns `dict` of all additionals from local `config.json` |
   | `check_update()` | Downloads cloud config, compares each `version` field against local. Returns `{"status": "Up_to_date"}` or `{name: cloud_config}` for outdated entries (skips uninstalled additionals) |
   | `download(update, additional)` | Core downloader. If `update=True`, validates additional is installed first. Downloads main files + all dependencies into `<Additionals>/<name>/`. Records in `settings.json`. Returns response. When `download=False`, returns cloud config data without writing to disk |
   | `update()` | Calls `check_update()`, then iterates outdated additionals calling `download(update=True)` for each |
   | `_read_downloaded_additionals()` | Reads `settings.json` → `list` of installed additional names |
   | `_write_downloaded_additionals(additional)` | Appends a name to `settings.json` |
   | `_update_config(additional)` | Merges cloud version of a single additional into local config |

   **Config File Structure:**
   - `~/.config/E.L.Y.S.I.U.M/Additionals/config.json` — Main additionals registry (each entry: `version`, `path`, `download_url`, `dependency` map)
   - `~/.config/E.L.Y.S.I.U.M/Additionals/settings.json` — Simple JSON array of installed additional names
   - `<Additionals>/<name>/` — Per-additional directory with downloaded skill/tool files

   **AI Agent Integration:** The module is designed so EL (the AI) can call `Additionals.download()` / `Additionals.update()` as tools, enabling autonomous decision-making about when to acquire new skills.

   **Error Handling:**
   - `ConfigFileMissing` — raised if `elysium_additionals_config` is missing from base config
   - `AdditionalsNotFound` — raised if requested additional name is not in the registry
   - `AdditionalsNotInstalled` — raised when `update=True` but additional hasn't been downloaded yet
   - Network errors from `download_config()` on timeouts or HTTP failures

---

## Running the Server / CLI

### Setup
```bash
chmod +x install.sh
./install.sh
```

The installation script creates a `romeo` CLI launcher at `~/.local/bin/romeo` and adds `~/.local/bin` to your `PATH` via `.bashrc`. It also provides an interactive upgrade workflow (Reinstall/Upgrade/Quit).

### CLI
```bash
# Run the CLI directly
python ElysiumCli/main.py <subcommand>
```

**Subcommands:**
| Command | Description |
|---------|-------------|
| `version` | Display current version from `config.json` |
| `status` | Display development status |
| `dev` | Display last development changes date |
| `version_name` | Display version name (e.g. omega-cooper) |
| `is_stable` | Check if current version is stable |
| `info` | Print all metadata (version, name, stable, dev changes) |
| `check_version` | Check cloud for available updates |
| `update` | Perform a full self-update (delete old, clone repo, `uv sync`) |

**Debug flag:**
- `-test` — Prints "etst" (debug/test flag)

> **Note**: `[project.scripts]` in `pyproject.toml` is currently empty. No `uv run` shortcut available yet.

### CLI Configuration Flags
```bash
# Create default config
python ElysiumCli/Config/cli_config.py -make

# Override existing config with defaults
python ElysiumCli/Config/cli_config.py -over_ride

# Add/edit config values interactively
python ElysiumCli/Config/cli_config.py -add_config
```

### Model Configuration Flags

```bash
# Download model config from GitHub (or custom URL)
python ElysiumConfig/model_config.py --download_config

# Ensure model config exists (downloads if missing)
python ElysiumConfig/model_config.py --make

# Insert/update an API key for a provider/model
python ElysiumConfig/model_config.py --insert_api
```

### FastAPI Server

```bash
# Start the FastAPI server (auto-reload enabled for development)
uv run uvicorn Server.main:server --reload
```

**Endpoints:**
- `GET /` — Health check (returns `{"status": 200}`)
- `GET /read` — SSE log streaming endpoint
- `WebSocket /ws` — Echo WebSocket

### Worker

> **Note**: Celery worker module is not yet implemented. Dependencies are listed in `pyproject.toml` for future use.

```bash
# Start Redis (required for Celery, when implemented)
redis-server

# Start Celery worker (when Elysium_Celery module is created)
uv run celery -A Elysium_Celery.config worker --loglevel=info
```

---

## Default Configurations

- **CLI Entry**: `ElysiumCli/main.py`
- **General Config**: `ElysiumConfig/config.json`
- **Model Config**: dynamically resolved to `~/.config/E.L.Y.S.I.U.M/Config/Model/model_config.json` via `path_config.py`
- **Server Entry**: `Server/main.py`
- **Server Routes**: `Server/routes/` (placeholder for future API blueprints)
- **CLI Config**: dynamically resolved to `~/.config/E.L.Y.S.I.U.M/Config/cli/config.json` via `cli_config.py`
- **Encryption Keys**: stored at `~/.config/E.L.Y.S.I.U.M/Config/Security/encryption/keys.json`
- **Worker Config**: stored at `~/.config/E.L.Y.S.I.U.M/Config/worker/`
- **Worker Preview**: `Workers/workers_preview.json` (startup config)
- **Additionals Config**: `~/.config/E.L.Y.S.I.U.M/Additionals/config.json` — auto-downloaded from `Elysium_additionals` repo on import (if missing)
- **Additionals Settings**: `~/.config/E.L.Y.S.I.U.M/Additionals/settings.json` — tracks which additionals have been installed
- **Additionals Root**: `~/.config/E.L.Y.S.I.U.M/Additionals/` — parent directory for all per-additional subdirectories
- **Per-additional Directories**: `~/.config/E.L.Y.S.I.U.M/Additionals/<name>/` — contains downloaded skill/tool files for each additional
- **Package Manager**: uv
