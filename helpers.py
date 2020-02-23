import time


def sleep(minutes=None, seconds=None, print_=False):
    if not minutes and not seconds:
        raise ValueError("Can not sleep for 0 time")

    minutes = 0 if minutes is None else minutes
    seconds = 0 if seconds is None else seconds

    sec_to_sleep = minutes * 60 + seconds

    if print_:
        print(f"Going to sleep for {sec_to_sleep} seconds")

    time.sleep(sec_to_sleep)
