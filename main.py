import sys


def main() -> None:
    print()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(130)  # 130 stands for "Script terminated by Control-C"