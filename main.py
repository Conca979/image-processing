import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src'))

from image_transparent.transparent import main as run_cli

if __name__ == "__main__":
    run_cli()