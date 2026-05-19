# Elysium - Home Server

Elysium is a modular, AI-augmented home server and CLI toolkit built with FastAPI, LangChain, and Python. It provides server health monitoring, email automation, AI agent configuration, and a Python CLI interface.

## Technology Stack

### Core
- **Framework**: FastAPI (standard), Typer, Textual (TUI)
- **AI & Agents**: LangChain, LangChain-Groq, LangChain-Ollama, LangGraph
- **Task Queue**: Celery with Redis
- **Email**: aiosmtplib
- **Audio**: pyaudio, sounddevice, webrtcvad-wheels
- **System Monitoring**: psutil
- **Utilities**: numpy, rich, requests
- **Package Manager**: uv

---

## Project Architecture

```
Elysium/
├── .python-version            # Python version specification (3.12)
├── .gitignore                 # Git ignore rules
├── uv.lock                    # uv dependency lockfile
├── pyproject.toml             # Project metadata and dependencies
├── requirements.txt           # Python dependencies
├── install.sh                 # Project installation script
├── .env                       # Environment variables
│
├── Agents/                    # AI Agent implementations
│   ├── __init__.py
│   └── agent.py               # Core agent logic
│
├── Elysium_Cli/               # Python CLI tool
│   ├── main.py                # CLI entry point
│   ├── Readme.md              # CLI documentation
│   ├── Config/                # CLI configuration
│   │   ├── __init__.py
│   │   ├── config.py          # Config management logic
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
│       └── tui/               # TUI module (placeholder)
│
├── Elysium_Config/            # Configuration management
│   ├── __init__.py
│   ├── model_config.py        # AI model configuration manager
│   ├── model_config.json      # Active model settings JSON
│   ├── model_config.log       # Model configuration log
│   ├── Ai/
│   │   ├── config_groq.py     # Groq API key configuration
│   │   └── config_google.py   # Google AI configuration
│   └── Email/
│       └── email_config.py    # SMTP credentials from .env
│
├── Errors/                    # Centralized error handling
│   └── errors.py              # Custom server exceptions
│
└── Logs/                      # Runtime logs
    ├── Elysium/               # Elysium CLI logs (empty)
    └── Hyper/
        └── Hyper_status.log   # Hyper server status logs
```

---

## Directory & File Purpose

### Root Level

| File | Purpose |
|------|---------|
| `pyproject.toml` | Project metadata (name: elysium, version: 0.1.0) |
| `requirements.txt` | Frozen dependency list |
| `uv.lock` | Frozen dependency lockfile |
| `install.sh` | Installation and environment setup script |
| `.python-version` | Specifies Python version (3.12) |
| `.gitignore` | Git ignore rules |
| `.env` | Environment variables for SMTP, AI APIs, etc. |

### `Elysium_Cli/` - CLI Tool

| File | Purpose |
|------|---------|
| `main.py` | CLI entry point |
| `internal/core/core.py` | Core CLI business logic (Python) |
| `internal/parse/` | Legacy C parsing files (unused) |
| `Config/config.py` | CLI specific configuration management |
| `commands/help/help.py` | Help command implementation |
| `commands/system_info/sys_info.py` | System info command |

### `Elysium_Config/` - Configuration

| File | Purpose |
|------|---------|
| `model_config.py` | Manages active AI model settings, API key injection, and config downloads |
| `model_config.json` | Active model settings in JSON format |
| `config_groq.py` | Loads Groq API key from `.env` |
| `config_google.py` | Loads Google AI configuration from `.env` |
| `email_config.py` | Loads SMTP credentials from `.env` |

### `Agents/` - AI Agents

| File | Purpose |
|------|---------|
| `agent.py` | Core implementation of AI agents and their capabilities |

### `Errors/` - Error Handling

| File | Purpose |
|------|---------|
| `errors.py` | Server-level exceptions (ProviderNotGiven, ModelNameNotGiven, ApiKeyNotGiven, etc.) |
| `Elysium_Cli/internal/Errors/errors.py` | CLI-specific exceptions (ConfigNotFound, InvalidArgsFound) |

---

## Code Flow

1. **CLI Startup** (`Elysium_Cli/main.py`):
   - Loads `internal/core/core.py` logic
   - Reads user input via `input()` prompt (`E.L > `)
   - Routes commands to `help` or `system_info`

2. **Model Configuration** (`Elysium_Config/model_config.py`):
   - Validates `model_config.json` existence
   - Downloads default config from GitHub if missing
   - Injects API keys for specified providers/models

3. **AI Agent Flow**:
   - `Agents/agent.py` initializes with `Elysium_Config` settings
   - Supports Groq and Ollama providers via LangChain

4. **Email Flow**:
   - Uses `aiosmtplib` for async SMTP delivery
   - Credentials loaded from `.env` via `email_config.py`

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

> **Note**: `uv run elysium-tui` is listed in the README but `[project.scripts]` in `pyproject.toml` is currently empty.

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
SMTP_HOST=smtp.example.com
SMTP_PORT=587
SMTP_USER=your_email@example.com
SMTP_PASS=your_password
GROQ=your_groq_api_key
GOOGLE_API_KEY=your_google_api_key
```

---

## Default Configurations

- **CLI Entry**: `Elysium_Cli/main.py`
- **Model Config**: `Elysium_Config/model_config.json`
- **Logs Directories**: `Logs/Hyper/`, `Logs/Elysium/`
- **Package Manager**: `uv`
