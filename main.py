import sys
import argparse


def parse_args() -> argparse.Namespace:
    """ Parses command-line arguments.
    
    Returns:
        argparse.Namespace: An object containing the parsed command-line arguments.
    """
    parser = argparse.ArgumentParser(
        description="A simple, minimalistic terminal-based Pomodoro timer.")
    parser.add_argument(
        "pomodoro", type=int, help="Duration of work sessions in minutes.")
    parser.add_argument(
        "short_break", type=int, help="Duration of short break sessions in minutes.")
    parser.add_argument(
        "long_break", type=int, help="Duration of long break sessions in minutes.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(130)  # 130 stands for "Script terminated by Control-C"
