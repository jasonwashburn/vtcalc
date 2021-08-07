import datetime as dt
import argparse


def get_valid_time_from_offset(model_run: dt.datetime, offset: int) -> dt.datetime:
    """Calculates the valid time from the model run time and the offset.

    Args:
        model_run (dt.datetime): A datetime object representing the model run
        offset (int): The number of hours to offset the model run time by

    Returns:
        datetime.datetime: A datetime object representing the valid time
    """
    if offset < 3600:
        valid_time = model_run + dt.timedelta(hours=offset)
    else:
        valid_time = model_run + dt.timedelta(seconds=offset)
    return valid_time


def parse_model_run_from_string(model_run_str: str) -> dt.datetime:
    """Parses a model run string into a datetime object.

    Args:
        model_run_str (str): A string representing the model run time in the format YYYYMMDDHH[z,Z]

    Returns:
        datetime.datetime: A datetime object representing the model run time
    """
    model_run_str = model_run_str.lower().replace("z", "")
    if model_run_str[0] == "1":
        try:
            model_run = dt.datetime.utcfromtimestamp(int(model_run_str))
        except ValueError as e:
            print(e)
            print("Invalid model run time. Please use the format YYYYMMDDHH[z,Z]")
            exit(1)

    else:
        try:
            model_run = dt.datetime.strptime(model_run_str, "%Y%m%d%H")
        except ValueError as e:
            print(e)
            print("Invalid model run time. Please use the format YYYYMMDDHH[z,Z]")
            exit(1)

    return model_run


def production_hours_chart(model_run_str: str) -> None:
    """Generates a chart of production hours for the last 8 model runs"""
    model_run = parse_model_run_from_string(model_run_str)
    valid_time = get_valid_time_from_offset(model_run, 0)
    valid_time_str = valid_time.strftime("%Y%m%d%H")
    print("Valid time: {}".format(valid_time_str))
    print("")

    # Get the last 8 model runs
    model_runs = [model_run - dt.timedelta(hours=i * 6) for i in range(8)]

    # Print the model run times
    print("Model Run\t\t+36\t\t+39\t\t+42\n")
    for model_run in model_runs:
        production_hours = []
        for production_hour in [36, 39, 42]:
            production_hours.append(
                (model_run + dt.timedelta(hours=production_hour)).strftime(
                    "%Y-%m-%d %Hz"
                )
            )
        print(
            model_run.strftime("%Y-%m-%d %Hz")
            + ": \t"
            + "\t ".join(production_hours)
            + "\n"
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Calculate a valid time from a model run and offset."
    )
    parser.add_argument(
        "model_run", help="Model Run: (Format: YYYYMMDDHH[z,Z] or in Epoch Seconds"
    )
    parser.add_argument(
        "offset",
        type=int,
        help="Number of hours to offset (Format: [+,-]HH) or epoch seconds ([+,-]ssss) (must be greater than 3600)",
    )
    args = parser.parse_args()
    model_run = parse_model_run_from_string(args.model_run)
    valid_time = get_valid_time_from_offset(model_run, args.offset)

    print(
        f"Model Run: {model_run.strftime('%Y-%m-%d %Hz')} \t Epoch: {model_run.timestamp():0.0f}\t Offset: {args.offset}"
    )
    print(
        f"Valid Time: {valid_time.strftime('%Y-%m-%d %Hz')}\t Epoch: {valid_time.timestamp():0.0f}"
    )
