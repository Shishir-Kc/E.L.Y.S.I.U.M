# E.L.Y.S.I.U.M - Home Server

E.L.Y.S.I.U.M is a modular, AI-augmented home server and CLI toolkit built with FastAPI, LangChain, and Python. It provides server health monitoring, email automation, AI agent configuration, NVIDIA LLM integration, and a Python CLI interface.

## Technology Stack

### Active Dependencies
- **Core**: pydantic, python-dotenv, requests
- **AI & Agents**: openai
- **Encryption**: cryptography
- **TUI**: textual
- **Package Manager**: uv

### Planned/Aspirational
- **Framework**: FastAPI (standard), Typer, Textual (TUI)
- **AI & Agents**: LangChain, LangChain-Groq, LangChain-Ollama, LangGraph
- **Task Queue**: Celery with Redis
- **Email**: aiosmtplib
- **Audio**: pyaudio, sounddevice, webrtcvad-wheels
- **System Monitoring**: psutil
- **Utilities**: numpy, rich, tqdm

---

## Project Architecture

```
E.L.Y.S.I.U.M/
├── .python-version            # Python version specification (3.12)
├── .gitignore                 # Git ignore rules
├── uv.lock                    # uv dependency lockfile
├── pyproject.toml             # Project metadata and dependencies
├── requirements.txt           # Pinned Python dependencies (20 packages)
├── install.sh                 # Project installation script

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
│   │   ├── help/
│   │   │   └── help.py        # Help command (stub)
│   │   └── system_info/
│   │       └── sys_info.py    # System info command (stub)
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
│   ├── updater.py             # Updater class — E.L.Y.S.I.U.M version check & auto-update (stub)
│   ├── config.json            # Base system metadata JSON (+ additionals config URL)
│   └── path_config.json       # Predefined local path settings (+ additionals paths)
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
| `pyproject.toml` | Project metadata (name: elysium, version: 0.0.1) |
| `requirements.txt` | Pinned Python dependencies (20 packages) |
| `uv.lock` | uv dependency lockfile |
| `install.sh` | Installation and environment setup script |
| `.python-version` | Specifies Python version (3.12) |
| `.gitignore` | Git ignore rules |

### `ElysiumConfig/` - Configuration

| File | Purpose |
|------|---------|
| `__init__.py` | Validates `~/.config/E.L.Y.S.I.U.M/` exists on import via `path_config.check_for_eLysium_path()`; raises `ConfigFileMissing` if not found |
| `model_config.py` | Manages AI model settings, API key injection (with Fernet encryption), config download from GitHub |
| `additionals.py` | Additionals plug-and-play system: downloads/updates config from `Elysium_additionals` repo, version checks, auto-updates on missing config |
| `updater.py` | `Updater` class for E.L.Y.S.I.U.M version checking and auto-updating. Designed so the agent can self-update at will or when prompted by the user; `check_update` is intended to run every instance (currently a stub) |
| `config.json` | Base system metadata (version: 0.0.1, status: development, version_name: omega-mini, stable: False) plus `elysium_additionals_config` with download URL |
| `path_config.py` | Core path management, path listing, additionals path config, and GitHub config downloader |
| `path_config.json` | Predefined directory path mappings (Root, Log, Skill, Memory, Config) and additionals paths (Root, Memory, Config) |

### `ElysiumCli/` - CLI Tool

| File | Purpose |
|------|---------|
| `main.py` | CLI entry point |
| `internal/core/core.py` | Core CLI REPL loop (`:>` prompt) and command routing (`-chat`, `help`, `-download_config`, `-insert_api`) |
| `internal/__init__.py` | Exports `ConfigNotFound`, `InvalidArgsFound` exceptions |
| `internal/Errors/errors.py` | CLI-specific exceptions (`ConfigNotFound`, `InvalidArgsFound`) |
| `Config/cli_config.py` | CLI-specific configuration management with Pydantic validation, encryption, argparse flags (`-make`, `-over_ride`, `-add_config`) |
| `commands/help/help.py` | Help command implementation |
| `commands/system_info/sys_info.py` | System info command (stub) |

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
| `Errors/errors.py` | Server-level exceptions (`ProviderNotGiven`, `ModelNameNotGiven`, `ApiKeyNotGiven`, `ConfigFileMissing`, `ProviderNotFound`, `DirectoryNotGiven`, `KeysNotFound`, `AdditionalsNotFound`) |

---

## Code Flow

1. **CLI Startup** (`ElysiumCli/main.py`):
   - Loads `internal/core/core.py` logic (directly imports `NvidiaAgent`, `Load_Agent` from `Agents.nvidia` and `Elysium_Model_Config` from `ElysiumConfig.model_config`)
   - Reads user input via `input()` prompt (`:>`)
   - Routes commands: `help` → available commands list, `-chat` → NvidiaAgent interactive loop, `-download_config` → download model config, `-insert_api` → insert API key interactively
   - Exit with `e`

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

4. **AI Agent Flow** (`Agents/__init__.py`):
   - `Load_Agent` class (defined in `Agents/__init__.py`, re-exported via `Agents/nvidia.py`) initializes `Elysium_Model_Config` on instantiation
   - `model_roulet(priority_provider="")` returns a random model/provider pair, with optional priority provider
   - `model_key(provider, model)` retrieves and decrypts the API key via `getkey()` + `decrypt()`

5. **NvidiaAgent Flow** (`Agents/nvidia.py`):
   - `NvidiaAgent.__init__(agent)` calls `model_roulet(priority_provider="nvidia")` to select a random NVIDIA model
   - Creates an `OpenAI` client configured with `base_url="https://integrate.api.nvidia.com/v1"`
   - `chat(prompt)` calls the OpenAI Responses API with `reasoning={'effort': 'high'}` and returns `response.output_text`

6. **Encryption Flow** (`Security/encryption/crypto.py`):
   - `generate_key(module, provider_name, model_name)` creates a Fernet key, stores it in `~/.config/E.L.Y.S.I.U.M/Config/Security/encryption/keys.json`
   - Duplicate provider+model detection updates existing keys rather than creating duplicates
   - `encrypt(item, key)` / `decrypt(item, key)` wrap Fernet symmetric encryption
   - `getkey(provider_name, model_name)` looks up key from `keys.json` by provider+model; raises `KeysNotFound` if missing
   - Used by `model_config.py` and `cli_config.py` to encrypt stored API keys

7. **Worker Flow** (`Workers/worker.py`):
   - On import, auto-creates `~/.config/E.L.Y.S.I.U.M/Config/worker/` and `Logs/worker/` directories
   - `worker` class (placeholder) designed for threaded background task execution
   - `workers_preview.json` defines startup behavior (id, execution_time, repeat)

8. **Updater Flow** (`ElysiumConfig/updater.py`):
   - `Updater` class handles E.L.Y.S.I.U.M version checking and updating
   - Designed to be callable by the AI agent for autonomous self-updates, or triggered by user prompts
   - `check_update` method is intended to run on every instance to detect new versions
   - Currently a stub (`__init__` only); implementation pending

9. **Additionals Flow** (`ElysiumConfig/additionals.py`):

   **Overview** — The Additionals system is a plug-and-play skill/tool downloader that lets E.L.Y.S.I.U.M learn new capabilities at runtime. Additionals are defined in a separate [`Elysium_additionals`](https://github.com/Shishir-Kc/Elysium_additionals) repo.

   **Import-time Initialization** (runs automatically when the module is first imported):
   - `load_additiosnals_config()` reads `ElysiumConfig/config.json` to get `elysium_additionals_config.download_url`
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
   | `download(update, additional)` | Core downloader. If `update=True`, validates additional is installed first. Downloads main files + all dependencies into `<Additionals>/<name>/`. Records in `settings.json`. Returns response |
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

### CLI
```bash
# Run the CLI directly
python ElysiumCli/main.py
```

**Commands:**
- `help` - Display available commands
- `-chat` - Start an interactive chat with an NVIDIA LLM via NvidiaAgent
- `-download_config` - Download model configuration (prompts for URL)
- `-insert_api` - Insert/update an API key for a provider/model

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

Standalone script (double-dash flags):
```bash
# Download model config from GitHub (or custom URL)
python ElysiumConfig/model_config.py --download_config

# Ensure model config exists (downloads if missing)
python ElysiumConfig/model_config.py --make

# Insert/update an API key for a provider/model
python ElysiumConfig/model_config.py --insert_api
```

From CLI REPL (single-dash commands):
```bash
# Same operations available inside the CLI
:> -download_config
:> -insert_api
```

### Backend / Worker

> **Note**: Celery and FastAPI server modules are not yet implemented. Dependencies are listed in `pyproject.toml` for future use.

```bash
# Start Redis (required for Celery, when implemented)
redis-server

# Start Celery worker (when Elysium_Celery module is created)
uv run celery -A Elysium_Celery.config worker --loglevel=info

# Start FastAPI server (when server module is created)
uv run uvicorn main:elysium_server --reload
```

---

## Default Configurations

- **CLI Entry**: `ElysiumCli/main.py`
- **General Config**: `ElysiumConfig/config.json`
- **Model Config**: dynamically resolved to `~/.config/E.L.Y.S.I.U.M/Config/Model/model_config.json` via `path_config.py`
- **CLI Config**: dynamically resolved to `~/.config/E.L.Y.S.I.U.M/Config/cli/config.json` via `cli_config.py`
- **Encryption Keys**: stored at `~/.config/E.L.Y.S.I.U.M/Config/Security/encryption/keys.json`
- **Worker Config**: stored at `~/.config/E.L.Y.S.I.U.M/Config/worker/`
- **Worker Preview**: `Workers/workers_preview.json` (startup config)
- **Additionals Config**: `~/.config/E.L.Y.S.I.U.M/Additionals/config.json` — auto-downloaded from `Elysium_additionals` repo on import (if missing)
- **Additionals Settings**: `~/.config/E.L.Y.S.I.U.M/Additionals/settings.json` — tracks which additionals have been installed
- **Additionals Root**: `~/.config/E.L.Y.S.I.U.M/Additionals/` — parent directory for all per-additional subdirectories
- **Per-additional Directories**: `~/.config/E.L.Y.S.I.U.M/Additionals/<name>/` — contains downloaded skill/tool files for each additional
- **Package Manager**: uv
