from site import venv
import sys

def venv_check():
    return True if 'venv' in sys.executable else False

if __name__ == "__main__":
    print('Using venv:', venv_check())