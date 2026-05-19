# Elysium - Home Server

Elysium is a FastAPI-based home server application that provides various services including server health monitoring, email automation, AI chat capabilities, and background task processing.

## Technology Stack

### Backend
- **Framework**: FastAPI
- **Task Queue**: Celery with Redis
- **AI**: LangChain (Groq, Ollama), LangGraph
- **Email**: aiosmtplib
- **Async HTTP**: httpx
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
├── Dockerfile                 # Docker container configuration
├── .dockerignore              # Docker ignore rules
├── .python-version            # Python version specification
├── uv.lock                    # uv dependency lockfile
├── pyproject.toml             # Project metadata and dependencies
├── requirements.txt           # Python dependencies
├── install.sh                 # Project installation script
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
│   └── elysium_server/        # Server management
│       ├── __init__.py
│       └── restart.py         # Server restart logic
│
├── Elysium_Celery/            # Celery task configuration
│   ├── __init__.py
│   ├── config.py              # Celery broker/backend setup
│   └── tasks.py               # Background tasks (email, test)
│
├── Elysium_Config/            # Configuration management
│   ├── Email/
│   │   └── email_config.py    # SMTP credentials from .env
│   │
│   ├── Ai/
│   │   ├── config_groq.py     # Groq API key configuration
│   │   └── config_google.py   # Google AI configuration
│   │
│   ├── __init__.py
│   ├── model_config.py        # Model configuration management
│   ├── model_config.json      # Active model settings JSON
│   └── model_config.log       # Model configuration log
│
├── Agents/                    # AI Agent implementations
│   ├── __init__.py
│   └── agent.py               # Core agent logic
│
├── Errors/                    # Centralized error handling
│   ├── __init__.py
│   └── errors.py              # Custom server exceptions
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
├── Elysium_Cli/              # Python/C Hybrid CLI tool
│   ├── main.py                # CLI entry point
│   ├── Readme.md              # CLI README
│   ├── Config/                # CLI configuration
│   │   ├── __init__.py
│   │   ├── config.py
│   │   └── config.json
│   │
│   ├── commands/             # CLI commands
│   │   ├── help/             # Help command
│   │   │   └── help.py
│   │   └── system_info/      # System info command
│   │       └── sys_info.py
│   │
│   ├── internal/             # Core modules
│   │   ├── core/             # Core Python logic
│   │   │   └── core.py
│   │   ├── parse/            # C-based input parsing
│   │   │   ├── parse.c
│   │   │   └── parse.h
│   │   ├── tui/              # TUI implementation
│   │   │   └── __init__.py
│   │   └── Errors/           # CLI error handling
│   │       └── errors.py
│   │
│   └── external/             # External resources
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
| `Dockerfile` | Docker image build instructions |
| `.dockerignore` | Excludes unnecessary files from Docker context |
| `.python-version` | Specifies Python version for pyenv/ui |
| `uv.lock` | Frozen dependency lockfile |
| `pyproject.toml` | Project metadata (name: elysium, version: 0.1.0) |
| `requirements.txt` | Frozen dependency list |
| `install.sh` | Installation and environment setup script |

### `api/v1/` - API Endpoints

| File | Endpoint | Description |
|------|----------|-------------|
| `server_health.py` | `GET /api/v1/health` | Returns server health status |
| `hyper_stats.py` | `GET /api/v1/hyper/status/` | Checks if Hyper server is active |
| `email.py` | `POST /api/v1/send/email` | Queues email sending via Celery |
| `ai_chat.py` | `POST /api/v1/chat/Agent` | Chat with AI agent |
| `workers_test.py` | `POST /api/v1/start/test/worker` | Test Celery worker |
| `laptop_price.py` | WebSocket `/api/v1/ws/` | Real-time price updates (dummy) |

### `services/` - Core Services

| File | Purpose |
|------|---------|
| `email_service.py` | Async SMTP email sending using `aiosmtplib` |
| `server_file_integrety.py` | Checks/creates `Logs/Hyper` and `Logs/Elysium` directories on startup |
| `restart.py` | Logic for server process restart |

### `Elysium_Celery/` - Background Tasks

| File | Purpose |
|------|---------|
| `config.py` | Celery config with Redis broker/backend (localhost:6379) |
| `tasks.py` | Celery tasks: `idk_man` (test), `sending_mail` (async email) |

### `Elysium_Config/` - Configuration

| File | Purpose |
|------|---------|
| `email_config.py` | Loads SMTP credentials from `.env` |
| `config_groq.py` | Loads Groq API key from `.env` |
| `config_google.py` | Loads Google AI configuration from `.env` |
| `model_config.py` | Manages active AI model settings |
| `model_config.json` | Active model settings in JSON format |
| `model_config.log` | Model configuration activity log |

### `Agents/` - AI Agents

| File | Purpose |
|------|---------|
| `agent.py` | Core implementation of AI agents and their capabilities |

### `Errors/` - Error Handling

| File | Purpose |
|------|---------|
| `errors.py` | Centralized custom exception classes for the server |

### `Tools/` - Utilities

| File | Purpose |
|------|---------|
| `hyper_health.py` | Checks Hyper server status via HTTP request |
| `smooth_bar.py` | Animated console progress bar |
| `elysium.py` | Server logging configuration |

### `Elysium_Cli/` - Hybrid CLI Tool

| File | Purpose |
|------|---------|
| `main.py` | CLI entry point |
| `internal/core/core.py` | Core CLI business logic (Python) |
| `internal/parse/parse.c` | Input parsing logic (C source) |
| `internal/parse/parse.h` | Input parsing logic (C header) |
| `internal/tui/__init__.py` | Terminal User Interface implementation |
| `Config/config.py` | CLI specific configuration management |
| `commands/help/help.py` | Help command implementation |
| `commands/system_info/sys_info.py` | System info command |

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
   - POST to `/api/v1/chat/Agent` → Agent implementation in `Agents/agent.py`
   - Uses configuration from `Elysium_Config/`

5. **WebSocket**:
   - `/api/v1/ws/` endpoint sends dummy laptop prices every 10 seconds

6. **Shutdown**:
   - `sleppy_sleppy()` prints shutdown message

---

## Running the Server

### Setup
```bash
chmod +x install.sh
./install.sh
```

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
| `POST /api/v1/chat/Agent` | `POST /api/v1/chat/Agent` | AI Chat with Agent |
| `POST /api/v1/send/email` | `POST /api/v1/send/email` | Send email via Celery |

Default backend URL: `http://localhost:8000`
