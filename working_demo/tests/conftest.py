from pathlib import Path
import sys

# Make the application package importable when pytest is launched from
# the repository root (as GitHub Actions does).
APP_DIR = Path(__file__).resolve().parents[1]
if str(APP_DIR) not in sys.path:
    sys.path.insert(0, str(APP_DIR))
