# Elysium_Cli

A simple C-based command-line interface application for the Elysium project.

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
make build
```

This compiles all source files in `commands/` and `internal/` directories.

## Running

```bash
./test
```

## Project Structure

```
Elysium_Cli/
├── main.c                    # Entry point
├── internal/
│   ├── core/                 # Core CLI logic
│   └── parse/                # Input parsing
├── commands/
│   ├── help/                 # Help command
│   └── system_info/          # System info command
└── Makefile                  # Build configuration
```

## Future Plans

- **AI Integration**: Replace hardcoded command logic with "functiongemma" AI model for intelligent command processing
- **Enhanced Parser**: Develop more complex parsing capabilities
- **More Commands**: Expand available CLI commands

## Flow 
![flow](https://raw.githubusercontent.com/Shishir-Kc/Assets/refs/heads/main/Elysium_cli/flow.png)

## License

[To be determined]
