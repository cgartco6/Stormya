# Old (probably what broke before)
from stormy.core.ai_engine import AIEngine

# Still correct now — or even better with the __init__.py magic:
from stormy.core import AIEngine
from stormy import AIEngine           # if exposed in top-level __init__.py
