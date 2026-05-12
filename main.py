import sys
import argparse
import subprocess
from datetime import datetime, timedelta


def send_notification(title: str, message: str, expire_time: int) -> None:
    """ Sends a desktop notification using the notify-send command.

    Args:
        title (str): The title of the notification.
        message (str): The message body of the notification.
        expire_time (int): The duration in seconds for which the notification should be displayed.
    """
    # The os.system() function in Python is deprecated due to
    # security risks, such as susceptibility to shell injection.
    subprocess.run(
        ["notify-send", f"--expire-time={expire_time * 1000}", "--app-name=pymodoro", f"{title}", f"{message}"])


def positive_int(value: str) -> int:
    """ Validates that the provided value is a positive integer.

    Args:
        value (str): The value to validate.

    Returns:
        int: The validated positive integer.
    """
    try:
        int_value = int(value)
        if int_value <= 0:
            raise argparse.ArgumentTypeError(
                f"{value} must be a positive integer.")
        return int_value
    except ValueError:
        raise argparse.ArgumentTypeError(f"{value} must be an integer.")


def parse_args() -> argparse.Namespace:
    """ Parses command-line arguments.

    Returns:
        argparse.Namespace: An object containing the parsed command-line arguments.
    """
    parser = argparse.ArgumentParser(
        description="A simple, minimalistic terminal-based Pomodoro timer.")
    parser.add_argument(
        "pomodoro", type=positive_int, help="Duration of work sessions in minutes.")
    parser.add_argument(
        "short_break", type=positive_int, help="Duration of short break sessions in minutes.")
    parser.add_argument(
        "long_break", type=positive_int, help="Duration of long break sessions in minutes.")
    parser.add_argument(
        "-t", "--expire-time", type=positive_int, default=10,
        help="Duration of the notifications expire time in seconds.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    pomodoro_duration = args.pomodoro * 60
    short_break_duration = args.short_break * 60
    long_break_duration = args.long_break * 60
    expire_time = args.expire_time
    pomodoro_start = datetime.now()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(130)  # 130 stands for "Script terminated by Control-C"
