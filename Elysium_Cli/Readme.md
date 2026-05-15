# Elysium_Cli

A Python-based command-line interface application for the Elysium project, designed to be AI-powered and agentic.

## Current State

Elysium_Cli is in early development stage, providing a basic interactive CLI framework.

## Features

### Current Commands
- `/help` - Display available commands
- `/system_info` - Show operating system information (Windows/Mac/Linux)

### How It Works
1. Run the CLI - it starts an interactive prompt (`>`)
2. Type commands with `/` prefix (e.g., `/help`)
3. The parser processes input and routes to appropriate command handler

## Building

```bash
python main.py
```

## Running

```bash
python main.py
```

## Project Structure

```
Elysium_Cli/
├── main.py                 # Entry point
├── internal/
│   ├── core/               # Core CLI logic & command routing
│   └── parse/              # Input parsing (C legacy, to be replaced)
├── commands/
│   ├── help/               # Help command
│   └── system_info/         # System info command
└── external/               # External integrations
```

## Future Plans

- **AI Integration**: Replace hardcoded command logic with "functiongemma" AI model for intelligent command processing
- **Enhanced Parser**: Develop more complex parsing capabilities
- **More Commands**: Expand available CLI commands

## Flow 
![flow](https://raw.githubusercontent.com/Shishir-Kc/Assets/refs/heads/main/Elysium_cli/flow.png)

## License

[To be determined]
