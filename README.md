# Elysium - Home Server

Elysium is a modular, AI-augmented home server and CLI toolkit built with FastAPI, LangChain, and Python. It provides server health monitoring, email automation, AI agent configuration, and a hybrid Python/C CLI interface.

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
├── Dockerfile                 # Docker container configuration
├── .dockerignore              # Docker ignore rules
├── .python-version            # Python version specification
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
├── Elysium_Cli/               # Hybrid Python/C CLI tool
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
│   └── internal/              # Core modules
│       ├── __init__.py
│       ├── core/
│       │   └── core.py        # CLI business logic
│       ├── Errors/
│       │   └── errors.py      # CLI custom exceptions
│       └── parse/             # C-based input parsing
│           ├── parse.c
│           └── parse.h
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
| `Dockerfile` | Docker image build instructions |
| `.dockerignore` | Excludes unnecessary files from Docker context |
| `.python-version` | Specifies Python version for pyenv/uv |
| `.env` | Environment variables for SMTP, AI APIs, etc. |

### `Elysium_Cli/` - Hybrid CLI Tool

| File | Purpose |
|------|---------|
| `main.py` | CLI entry point |
| `internal/core/core.py` | Core CLI business logic (Python) |
| `internal/parse/parse.c` | Input parsing logic (C source) |
| `internal/parse/parse.h` | Input parsing logic (C header) |
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
| `errors.py` | Centralized custom exception classes for the server and CLI |

---

## Code Flow

1. **CLI Startup** (`Elysium_Cli/main.py`):
   - Loads `internal/core/core.py` logic
   - Parses user input via C-based `parse` module
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

# Or use the uv script entry
uv run elysium-tui
```

### Backend / Worker
```bash
# Start Redis (required for Celery)
redis-server

# Start Celery worker
uv run celery -A Elysium_Celery.config worker --loglevel=info

# Start FastAPI server (if applicable)
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

## Docker Deployment

```bash
# Build the Docker image
docker build -t elysium .

# Run the container
docker run -d -p 8000:8000 --env-file .env --name elysium_server elysium

# Stop and remove the container
docker stop elysium_server && docker rm elysium_server
```

---

## Default Configurations

- **CLI Entry**: `Elysium_Cli/main.py`
- **Model Config**: `Elysium_Config/model_config.json`
- **Logs Directory**: `Logs/Hyper/`
- **Package Manager**: `uv`
