# Elysium - Home Server

Elysium is a FastAPI-based home server application that provides various services including server health monitoring, email automation, AI chat capabilities, background task processing.

## Technology Stack

### Backend
- **Framework**: FastAPI
- **Task Queue**: Celery with Redis
- **AI**: LangChain (Groq, Ollama), LangGraph, Qwen
- **Email**: aiosmtplib
- **Async HTTP**: httpx (via FastAPI standard)
- **Audio**: faster-whisper, pyaudio, sounddevice, webrtcvad-wheels
- **System Monitoring**: psutil
- **Utilities**: numpy, rich, requests
- **Package Manager**: uv

---

## Project Architecture

```
Elysium/
├── main.py                     # FastAPI application entry point
├── server_logging.py          # Server-wide logging configuration
├── elysium_tui.py             # Server Terminal User Interface
├── pyproject.toml             # Project metadata and dependencies
├── requirements.txt           # Python dependencies
│
├── api/
│   └── v1/                    # API Version 1
│       ├── __init__.py        # Router aggregation
│       │
│       ├── server_status/     # Server health endpoints
│       │   └── server_health.py
│       │
│       ├── Hyper_status/      # Hyper server monitoring
│       │   └── hyper_stats.py
│       │
│       ├── email/             # Email endpoints
│       │   └── email.py
│       │
│       ├── ai/               # AI chat endpoints
│       │   └── ai_chat.py
│       │
│       ├── Test_workers/     # Celery worker testing
│       │   └── workers_test.py
│       │
│       └── websocket/        # WebSocket endpoints
│           └── laptop_price.py
│
├── services/
│   ├── Email/                 # Email service
│   │   ├── __init__.py
│   │   └── email_service.py  # Async email sending via SMTP
│   │
│   ├── Server_Dir_check/      # Server directory integrity
│   │   └── server_file_integrety.py  # Creates required log directories
│   │
│   ├── Voice_To_Text/         # Audio transcription
│   │   └── transcriber.py     # Voice-to-text processing
│   │
│   └── elysium_server/        # Server management
│       └── restart.py         # Server restart logic
│
├── Elysium_Celery/            # Celery task configuration
│   ├── config.py              # Celery broker/backend setup
│   └── tasks.py               # Background tasks (email, test)
│
├── Elysium_Config/            # Configuration management
│   ├── Email/
│   │   └── email_config.py    # SMTP credentials from .env
│   └── Ai/
│       ├── config_groq.py     # Groq API key configuration
│       └── config_google.py   # Google AI configuration
│
├── AI/                        # AI integration
│   ├── Cloud/
│   │   └── Groq/
│   │       └── groq_ai.py     # LangChain Groq agent
│   ├── Local/
│   │   └── qwen.py            # Local AI implementation using Qwen
│   └── Tools/
│       ├── email.py           # AI tool for sending emails
│       └── file_ops.py        # AI tool for file system operations
│
├── Tools/                     # Utility tools
│   ├── Hyper/
│   │   ├── __init__.py
│   │   └── hyper_health.py    # Hyper server status checker
│   │
│   ├── Progress_bar/
│   │   └── smooth_bar.py      # Animated progress bar
│   │
│   └── elysium/
│       └── elysium.py         # Logging setup
│
├── Database/
│   └── Schema/
│       └── Email/
│           └── email_schema.py  # Pydantic email model
│
├── Elysium_Cli/              # C-based CLI tool
│   ├── main.c                # CLI entry point
│   ├── Makefile              # Build configuration
│   ├── commands/             # CLI commands
│   │   ├── help/             # Help command
│   │   └── system_info/      # System info command
│   ├── internal/             # Core modules
│   │   ├── core/             # Core logic
│   │   └── parse/            # Input parsing
│   ├── test                  # Test files
│   └── Readme.md             # CLI README
│
├── Modules/                   # C Extensions
│   ├── hellomodule.c          # Example C extension
│   └── setup.py               # Build script for modules
│
├── Sentinel/                    # File integrity monitoring
│   ├── watcher.py               # SHA-256 file watcher & backup
│   ├── dir.json                 # Directory config
│   └── ignore.json              # Files/dirs to ignore
│
└── assets/
    ├── Elysium/               # Server branding assets
    │   ├── __init__.py
    │   ├── start_up.py       # Startup/shutdown routines
    │   ├── branding.txt      # ASCII art logo
    │   ├── shutting.txt      # Shutdown message
    │   └── restarting.txt    # Restart message
    ├── Watcher/
    │   └── eye.txt            # Sentinel branding
    └── Workers/
        └── worker.txt         # Celery worker branding
```

---

## Directory & File Purpose

### Root Level

| File | Purpose |
|------|---------|
| `main.py` | FastAPI app initialization with CORS middleware, lifespan context manager, and router inclusion |
| `server_logging.py` | Global logger instance for the server |
| `elysium_tui.py` | Terminal-based user interface for server management |
| `pyproject.toml` | Project metadata (name: elysium, version: 0.1.0) |
| `requirements.txt` | Frozen dependency list (generated by uv from pyproject.toml) |

### `api/v1/` - API Endpoints

| File | Endpoint | Description |
|------|----------|-------------|
| `server_health.py` | `GET /api/v1/health` | Returns server health status |
| `hyper_stats.py` | `GET /api/v1/hyper/status/` | Checks if Hyper server is active |
| `email.py` | `POST /api/v1/send/email` | Queues email sending via Celery |
| `ai_chat.py` | `POST /api/v1/chat/Agent` | Chat with AI agent using Groq |
| `workers_test.py` | `POST /api/v1/start/test/worker` | Test Celery worker |
| `laptop_price.py` | WebSocket `/api/v1/ws/` | Real-time price updates (dummy) |

### `services/` - Core Services

| File | Purpose |
|------|---------|
| `email_service.py` | Async SMTP email sending using `aiosmtplib` |
| `server_file_integrety.py` | Checks/creates `Logs/Hyper` and `Logs/Elysium` directories on startup |
| `transcriber.py` | Voice-to-text transcription service |
| `restart.py` | Logic for server process restart |

### `Elysium_Celery/` - Background Tasks

| File | Purpose |
|------|---------|
| `config.py` | Celery config with Redis broker/backend (localhost:6379) |
| `tasks.py` | Celery tasks: `idk_man` (test), `sending_mail` (async email) |

### `Elysium_Config/` - Configuration

| File | Purpose |
|------|---------|
| `email_config.py` | Loads SMTP_HOST, SMTP_PORT, SMTP_USER, SMTP_PASS from `.env` |
| `config_groq.py` | Loads Groq API key from `.env` |
| `config_google.py` | Loads Google AI configuration from `.env` |

### `AI/` - Artificial Intelligence

| File | Purpose |
|------|---------|
| `groq_ai.py` | LangChain agent using ChatGroq with email tool |
| `qwen.py` | Local AI implementation using Qwen model |
| `email.py` | LangChain `@tool` decorator for AI-driven email sending |
| `file_ops.py` | LangChain `@tool` for AI-driven file operations |

### `Tools/` - Utilities

| File | Purpose |
|------|---------|
| `hyper_health.py` | Checks Hyper server status via HTTP request |
| `smooth_bar.py` | Animated console progress bar |
| `elysium.py` | Server logging configuration |

### `Database/Schema/` - Data Models

| File | Purpose |
|------|---------|
| `email_schema.py` | Pydantic model: `Email_Schema` with subject, receiver, content |

### `Sentinel/` - File Integrity Monitor

| File | Purpose |
|------|---------|
| `watcher.py` | Standalone CLI tool: hashes project files, creates backup in `Elysium_back_up/`, watches for changes every 5s |
| `dir.json` | Directory configuration (placeholder) |
| `ignore.json` | Files/directories to skip: `.git`, `.gitignore`, `Elysium_back_up`, `__pycache__`, `Logs` |

### `Elysium_Cli/` - C-based CLI Tool

| File | Purpose |
|------|---------|
| `main.c` | CLI entry point |
| `Makefile` | Build configuration for the C CLI |
| `commands/help/` | Help command implementation |
| `commands/system_info/` | System information command |
| `internal/core/` | Core CLI logic |
| `internal/parse/` | Input parsing modules |
| `test` | Test files |
| `Readme.md` | CLI-specific documentation |

### `Modules/` - C Extensions

| File | Purpose |
|------|---------|
| `hellomodule.c` | Example C extension for Python |
| `setup.py` | Script to compile and install C modules |

### `assets/Elysium/` - Branding

| File | Purpose |
|------|---------|
| `start_up.py` | `wakey_wakey()` prints logo on startup, `sleppy_sleppy()` on shutdown |
| `branding.txt` | Elysium ASCII art logo |
| `shutdown.txt` | Shutdown message |
| `restarting.txt` | Restart message |

---

## Code Flow

1. **Startup** (`main.py`):
   - `Lifespan` context manager runs `check_sys_dir()` then `wakey_wakey()`
   - Creates required log directories
   - Prints branding logo

2. **API Requests**:
   - All routes prefixed with `/api/v1`
   - CORS enabled for all origins

3. **Email Flow**:
   - POST to `/api/v1/send/email` → Celery task `sending_mail.delay()`
   - Celery worker executes `prepare_email()` via `aiosmtplib`

4. **AI Chat Flow**:
   - POST to `/api/v1/chat/Agent` → LangChain agent (Groq/Qwen)
   - Agent can use `send_email` and `file_ops` tools

5. **WebSocket**:
   - `/api/v1/ws/` endpoint sends dummy laptop prices every 10 seconds

6. **Shutdown**:
   - `sleppy_sleppy()` prints shutdown message

---

## Running the Server

### Backend

```bash
# Start Redis (required for Celery)
redis-server

# For Arch Linux, use Valkey instead of Redis:
valkey-server

# Start Celery worker
uv run celery -A Elysium_Celery.config worker --loglevel=info

# Start FastAPI server
uv run uvicorn main:elysium_server --reload

# Run file integrity watcher
uv run Sentinel/watcher.py

# Run the TUI
uv run elysium_tui.py
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

## Frontend-Backend Communication

The system uses REST API and WebSockets for communication.

| Frontend Endpoint | Backend Endpoint | Description |
|------------------|------------------|-------------|
| `GET /api/v1/health` | `GET /api/v1/health` | Server health status |
| `POST /api/v1/chat/Agent` | `POST /api/v1/chat/Agent` | AI Chat with Groq/Qwen |
| `POST /api/v1/send/email` | `POST /api/v1/send/email` | Send email via Celery |

Default backend URL: `http://localhost:8000`
