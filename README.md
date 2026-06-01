# Elysium - Home Server

Elysium is a modular, AI-augmented home server and CLI toolkit built with FastAPI, LangChain, and Python. It provides server health monitoring, email automation, AI agent configuration, and a Python CLI interface.

## Technology Stack

### Active Dependencies
- **Core**: pydantic, python-dotenv, requests
- **Encryption**: cryptography
- **Package Manager**: uv

### Planned/Aspirational
- **Framework**: FastAPI (standard), Typer, Textual (TUI)
- **AI & Agents**: LangChain, LangChain-Groq, LangChain-Ollama, LangGraph
- **Task Queue**: Celery with Redis
- **Email**: aiosmtplib
- **Audio**: pyaudio, sounddevice, webrtcvad-wheels
- **System Monitoring**: psutil
- **Utilities**: numpy, rich

---

## Project Architecture

```
Elysium/
├── .python-version            # Python version specification (3.12)
├── .gitignore                 # Git ignore rules
├── uv.lock                    # uv dependency lockfile
├── pyproject.toml             # Project metadata and dependencies
├── requirements.txt           # Python dependencies (aspirational)
├── install.sh                 # Project installation script
├── .env                       # Environment variables
│
├── Agents/                    # AI Agent implementations
│   ├── __init__.py            # Load_Agent class (config initialization)
│   └── agent.py               # Agents class (deep, web, worker, council agents)
│
├── Elysium_Cli/               # Python CLI tool
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
│       ├── Errors/
│       │   └── errors.py      # CLI custom exceptions
│       ├── parse/             # Input parsing (legacy C files, unused)
│       │   ├── parse.c
│       │   └── parse.h
│       └── tui/               # TUI module (stale .pyc cache, source missing)
│
├── Elysium_Config/            # Configuration management
│   ├── __init__.py            # Validates ~/.config/E.L.Y.S.I.U.M/ existence on import
│   ├── model_config.py        # AI model configuration manager (with encryption)
│   ├── config.json            # Base system metadata JSON
│   ├── path_config.py         # Path mapping config loader & GitHub downloader
│   └── path_config.json       # Predefined local path settings
│
├── Security/                  # Security & encryption modules
│   └── encryption/
│       ├── __init__.py
│       └── crypto.py          # Fernet key generation, encrypt, decrypt
│
├── Workers/                   # Background worker framework
│   ├── __init__.py
│   └── worker.py              # Worker class with threading & config/log paths
│
└── Errors/                    # Centralized error handling
    └── errors.py              # Custom server exceptions
```

---

## Directory & File Purpose

### Root Level

| File | Purpose |
|------|---------|
| `pyproject.toml` | Project metadata (name: elysium, version: 0.1.0) |
| `requirements.txt` | Aspirational dependency list (81 packages) |
| `uv.lock` | uv dependency lockfile |
| `install.sh` | Installation and environment setup script |
| `.python-version` | Specifies Python version (3.12) |
| `.gitignore` | Git ignore rules |
| `.env` | Environment variables for SMTP, AI APIs, etc. |

### `Elysium_Config/` - Configuration

| File | Purpose |
|------|---------|
| `__init__.py` | Validates `~/.config/E.L.Y.S.I.U.M/` exists on import; raises `ConfigFileMissing` if not found |
| `model_config.py` | Manages AI model settings, API key injection (with Fernet encryption), config download from GitHub |
| `config.json` | Base system metadata (version: 0.0.1, status: development, version_name: omega) |
| `path_config.py` | Core path management, path listing, and GitHub config downloader |
| `path_config.json` | Predefined directory path mapping configurations (Root, Log, Skill, Memory, Config) |

### `Elysium_Cli/` - CLI Tool

| File | Purpose |
|------|---------|
| `main.py` | CLI entry point |
| `internal/core/core.py` | Core CLI REPL loop and command routing (`help` → help.py, `stats` → sys_info.py) |
| `internal/__init__.py` | Exports `ConfigNotFound`, `InvalidArgsFound` exceptions |
| `internal/Errors/errors.py` | CLI-specific exceptions (`ConfigNotFound`, `InvalidArgsFound`) |
| `internal/parse/` | Legacy C parsing files (unused) |
| `Config/cli_config.py` | CLI-specific configuration management with Pydantic validation, encryption, argparse flags (`-make`, `-over_ride`, `-add_config`) |
| `commands/help/help.py` | Help command implementation |
| `commands/system_info/sys_info.py` | System info command (triggered via "stats") |

### `Agents/` - AI Agents

| File | Purpose |
|------|---------|
| `__init__.py` | `Load_Agent` class that initializes with `Elysium_Model_Config` |
| `agent.py` | `Agents` class with methods: `deep_agent`, `web_agent`, `worker_agent`, `agents_council`, `loop` |

### `Security/` - Security Modules

| File | Purpose |
|------|---------|
| `encryption/__init__.py` | Package init |
| `encryption/crypto.py` | Fernet key generation (`generate_key`), encryption (`encrypt`), decryption (`decrypt`) with JSON key store and duplicate module detection |

### `Workers/` - Background Workers

| File | Purpose |
|------|---------|
| `__init__.py` | Package init |
| `worker.py` | `worker` class (placeholder) with auto-created config/log paths under `~/.config/E.L.Y.S.I.U.M/` |

### `Errors/` - Error Handling

| File | Purpose |
|------|---------|
| `Errors/errors.py` | Server-level exceptions (`ProviderNotGiven`, `ModelNameNotGiven`, `ApiKeyNotGiven`, `ConfigFileMissing`, `ProviderNotFound`, `DirectoryNotGiven`) |

---

## Code Flow

1. **CLI Startup** (`Elysium_Cli/main.py`):
   - Loads `internal/core/core.py` logic
   - Reads user input via `input()` prompt (`E.L > `)
   - Routes commands: `help` → help.py, `stats` → sys_info.py

2. **Configuration Initialization** (`Elysium_Config/__init__.py`):
   - Validates `~/.config/E.L.Y.S.I.U.M/` exists on import
   - Raises `ConfigFileMissing` if not found

3. **Model Configuration** (`Elysium_Config/model_config.py`):
   - Resolves paths dynamically using `path_config.py` (pointing to `~/.config/E.L.Y.S.I.U.M/`)
   - Validates `model_config.json` existence under dynamic config path
   - Downloads default config from GitHub if missing
   - Injects API keys for specified providers/models, encrypted via `Security.encryption.crypto`

4. **AI Agent Flow** (`Agents/__init__.py`):
   - `Load_Agent` class initializes `Elysium_Model_Config` on instantiation
   - Supports Groq and Ollama providers via LangChain

5. **Encryption Flow** (`Security/encryption/crypto.py`):
   - `generate_key(module)` creates a Fernet key, stores it in `~/.config/E.L.Y.S.I.U.M/Config/Security/encryption/keys.json`
   - Duplicate module detection updates existing keys rather than creating duplicates
   - `encrypt(item, key)` / `decrypt(item, key)` wrap Fernet symmetric encryption
   - Used by `model_config.py` and `cli_config.py` to encrypt stored API keys

6. **Worker Flow** (`Workers/worker.py`):
   - On import, auto-creates `~/.config/E.L.Y.S.I.U.M/Config/worker/` and `Logs/worker/` directories
   - `worker` class (placeholder) designed for threaded background task execution

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
python Elysium_Cli/main.py
```

**Commands:**
- `help` - Display help
- `stats` - Show system information

> **Note**: `[project.scripts]` in `pyproject.toml` is currently empty. No `uv run` shortcut available yet.

### CLI Configuration Flags
```bash
# Create default config
python Elysium_Cli/Config/cli_config.py -make

# Override existing config with defaults
python Elysium_Cli/Config/cli_config.py -over_ride

# Add/edit config values interactively
python Elysium_Cli/Config/cli_config.py -add_config
```

### Model Configuration Flags
```bash
# Download model config from GitHub (or custom URL)
python Elysium_Config/model_config.py -download_config

# Ensure model config exists (downloads if missing)
python Elysium_Config/model_config.py -make

# Insert/update an API key for a provider/model
python Elysium_Config/model_config.py -insert_api
```

### Backend / Worker

> **Note**: Celery and FastAPI server modules are not yet implemented. Dependencies are listed in `requirements.txt` for future use.

```bash
# Start Redis (required for Celery, when implemented)
redis-server

# Start Celery worker (when Elysium_Celery module is created)
uv run celery -A Elysium_Celery.config worker --loglevel=info

# Start FastAPI server (when server module is created)
uv run uvicorn main:elysium_server --reload
```

---

## Environment Variables (.env)

```
GROQ_API=your_groq_api_key
GEMINI_API_KEY=your_gemini_api_key
SMTP_HOST=smtp.example.com
SMTP_PORT=587
SMTP_USER=your_email@example.com
SMTP_PASS=your_password
```

---

## Default Configurations

- **CLI Entry**: `Elysium_Cli/main.py`
- **General Config**: `Elysium_Config/config.json`
- **Model Config**: dynamically resolved to `~/.config/E.L.Y.S.I.U.M/Config/Model/model_config.json` via `path_config.py`
- **CLI Config**: dynamically resolved to `~/.config/E.L.Y.S.I.U.M/Config/cli/config.json` via `cli_config.py`
- **Encryption Keys**: stored at `~/.config/E.L.Y.S.I.U.M/Config/Security/encryption/keys.json`
- **Worker Config**: stored at `~/.config/E.L.Y.S.I.U.M/Config/worker/`
- **Package Manager**: uv