# Stormy

Personal modular AI assistant with Flask web interface.

## Quick start (Windows)

1. Double-click `run.bat`
2. Open http://127.0.0.1:5000 in your browser

## Structure

- `stormy/`           → main Python package
- `stormy/core/`      → AI logic modules (agents, memory, tools, personality…)
- `stormy/api/`       → Flask routes & endpoints
- `web/`              → frontend (HTML + JS)

## Next steps

- Connect real LLM in `ai_engine.py`
- Expand `/api/chat` endpoint
- Add authentication / sessions if needed
