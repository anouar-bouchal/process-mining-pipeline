import os
import sys
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__), 
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)

from src import EventLogs, EventRepository
import pm4py
from pyspark.sql import SparkSession


class Discoverer:
    def __init__(self, log, algotithm=None):

        self.log = log
        self.algorithm = algotithm

    def discover(self):
        if self.algorithm:
            return self.algorithm(self.log)
        else:
            return heuristic_miner(self.log)


def alpha_miner(log):
    return pm4py.discover_petri_net_alpha(log)


def inductive_miner(log):
    return pm4py.discover_petri_net_inductive(log)


def heuristic_miner(log):
    return pm4py.discover_petri_net_heuristics(log, dependency_threshold=0.99)


if __name__ == "__main__":

    event_repository = EventRepository()
    event_logs = EventLogs(event_repository.get_all_events())
    logs = event_logs.get_adapted_dataframe()

    alpha_model = Discoverer(logs, alpha_miner).discover()
    inductive_model = Discoverer(logs, inductive_miner).discover()
    heuristic_model = Discoverer(logs, heuristic_miner).discover()

    print(alpha_model, inductive_model, heuristic_model)
