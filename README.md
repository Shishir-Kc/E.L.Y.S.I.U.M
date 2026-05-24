# Elysium - Home Server

Elysium is a modular, AI-augmented home server and CLI toolkit built with FastAPI, LangChain, and Python. It provides server health monitoring, email automation, AI agent configuration, and a Python CLI interface.

## Technology Stack

### Active Dependencies
- **Core**: pydantic, python-dotenv, requests
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
│   └── agent.py               # Agent logic (placeholder)
│
├── Elysium_Cli/               # Python CLI tool
│   ├── main.py                # CLI entry point
│   ├── Readme.md              # CLI documentation
│   ├── Elysium/               # Empty directory placeholder
│   ├── Config/                # CLI configuration
│   │   ├── __init__.py
│   │   ├── cli_config.py      # Config management logic
│   │   ├── config.json        # Default CLI settings
│   │   └── config.log         # CLI activity log
│   ├── commands/              # CLI commands
│   │   ├── help/
│   │   │   └── help.py        # Help command
│   │   └── system_info/
│   │       └── sys_info.py    # System info command
│   ├── external/              # External integrations (placeholder)
│   └── internal/              # Core modules
│       ├── __init__.py
│       ├── core/
│       │   └── core.py        # CLI business logic
│       ├── Errors/
│       │   └── errors.py      # CLI custom exceptions
│       ├── parse/             # Input parsing (legacy C files, unused)
│       │   ├── parse.c
│       │   └── parse.h
│       └── tui/               # TUI module (stale .pyc cache, source missing)
│
├── Elysium_Config/            # Configuration management
│   ├── __init__.py            # Auto-validates ~/.config/Elysium/ on import
│   ├── model_config.py        # AI model configuration manager
│   ├── config.json            # Base system metadata JSON
│   ├── path_config.py         # Path mapping config loader
│   └── path_config.json       # Predefined local path settings
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
| `__init__.py` | Auto-validates `~/.config/Elysium/` exists on import |
| `model_config.py` | Manages AI model settings, API key injection, config downloads |
| `config.json` | Base system metadata (version: 0.0.1, status: development) |
| `path_config.py` | Core path management and GitHub config downloader |
| `path_config.json` | Predefined directory path mapping configurations |

### `Elysium_Cli/` - CLI Tool

| File | Purpose |
|------|---------|
| `main.py` | CLI entry point |
| `internal/core/core.py` | Core CLI business logic (Python) |
| `internal/parse/` | Legacy C parsing files (unused) |
| `Config/cli_config.py` | CLI-specific configuration management |
| `commands/help/help.py` | Help command implementation |
| `commands/system_info/sys_info.py` | System info command (triggered via "stats") |

### `Agents/` - AI Agents

| File | Purpose |
|------|---------|
| `__init__.py` | `Load_Agent` class that initializes with Elysium_Model_Config |
| `agent.py` | Agent logic (placeholder - currently empty) |

### `Errors/` - Error Handling

| File | Purpose |
|------|---------|
| `Errors/errors.py` | Server-level exceptions (ProviderNotGiven, ModelNameNotGiven, ApiKeyNotGiven, etc.) |
| `Elysium_Cli/internal/Errors/errors.py` | CLI-specific exceptions (ConfigNotFound, InvalidArgsFound) |

---

## Code Flow

1. **CLI Startup** (`Elysium_Cli/main.py`):
   - Loads `internal/core/core.py` logic
   - Reads user input via `input()` prompt (`E.L > `)
   - Routes commands: `help` → help.py, `stats` → sys_info.py

2. **Configuration Initialization** (`Elysium_Config/__init__.py`):
   - Validates `~/.config/Elysium/` exists on import
   - Raises `ConfigFileMissing` if not found

3. **Model Configuration** (`Elysium_Config/model_config.py`):
   - Resolves paths dynamically using `path_config.py` (pointing to `~/.config/Elysium/`)
   - Validates `model_config.json` existence under dynamic config path
   - Downloads default config from GitHub if missing
   - Injects API keys for specified providers/models

4. **AI Agent Flow** (`Agents/__init__.py`):
   - `Load_Agent` class initializes `Elysium_Model_Config` on instantiation
   - Supports Groq and Ollama providers via LangChain

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
- **Model Config**: dynamically resolved to `~/.config/Elysium/Config/Model/model_config.json` via `path_config.py`
- **Package Manager**: uv