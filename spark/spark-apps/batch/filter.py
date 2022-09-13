import os
import sys
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__), 
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)

from src import EventLogs, EventRepository
import pm4py
import pytz
import pandas as pd
from pyspark import SparkContext
from pyspark.sql import SparkSession


class Filter:
    def __init__(self, log, filter_type=None):
        self.log = log
        self.filter_type = filter_type

    def apply_filter(self, **kwargs):
        if self.filter_type:
            return self.filter_type(self.log, **kwargs)
        else:
            return get_most_recent(self.log)


def get_most_recent(log):
    return log


def filter_time_range(log, **kwargs):
    _check_required_args("start_timestamp", "end_timestamp", **kwargs)
    mode = "events"
    if "mode" in kwargs.keys():
        mode = kwargs["mode"]
    return pm4py.filter_time_range(
        log, kwargs["start_timestamp"], kwargs["end_timestamp"], mode=mode
    )


def filter_case_performance(log, **kwargs):
    _check_required_args("min_duration", "max_duration", **kwargs)
    return pm4py.filter_case_performance(
        log, kwargs["min_duration"], kwargs["max_duration"]
    )


def filter_start_activities(log, **kwargs):
    _check_required_args("start_activities", **kwargs)
    return pm4py.filter_start_activities(log, kwargs["start_activities"])


def filter_end_activities(log, **kwargs):
    _check_required_args("end_activities", **kwargs)
    return pm4py.filter_end_activities(log, kwargs["end_activities"])


def filter_case_size(log, **kwargs):
    _check_required_args("min_events", "max_events", **kwargs)
    return filter_case_size(log, kwargs["min_events"], kwargs["max_events"])


def _check_required_args(*args, **kwargs):
    if not set(args) <= set(kwargs.keys()):
        raise ValueError("must provide all required arguments : ", args)


if __name__ == "__main__":

    event_repository = EventRepository()
    event_logs = EventLogs(event_repository.get_all_events())
    logs = event_logs.get_adapted_dataframe()
    logs["time:timestamp"] = logs["time:timestamp"].apply(
        lambda t: t.replace(tzinfo=pytz.utc)
    )

    filtered_log = Filter(logs, filter_type=filter_time_range).apply_filter(
        start_timestamp="2009-10-13 00:00:00", end_timestamp="2012-01-18 23:59:59"
    )
    print(filtered_log)
