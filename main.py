from menu import init

import sys

def main():
    init()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nBye... :D")
        # TODO : salvataggi vari
        raise SystemExit(0)
