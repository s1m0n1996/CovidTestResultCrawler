from datetime import time


def convert_string_to_time(time_str: str):
    """

    :param time_str: must be in format: hh:mm -> 08:00
    :return:
    """
    split_time = time_str.split(":")

    return time(int(split_time[0]), int(split_time[1]))
