import pm4py
from pyspark import SparkContext
from pyspark.sql import SparkSession


class Model:
    def __init__(self, net, initial_marking, final_marking):
        self.net = net
        self.initial_marking = initial_marking
        self.final_marking = final_marking


class ConformanceChecker:
    def __init__(self, log, model, algorithm=None):
        self.log = log
        self.model = model

    def check(self, algorithm):
        if self.algorithm:
            return self.algorithm(self.log, self.model)
        else:
            return


def conformance_diagnostics_token_based_replay(log, model):
    return pm4py.conformance_diagnostics_token_based_replay(
        log, model.net, model.initial_marking, model.final_marking
    )


def conformance_diagnostics_alignments(log, model):
    return pm4py.conformance_diagnostics_alignments(
        log, model.net, model.initial_marking, model.final_marking
    )


def conformance_diagnostics_footprint(log):
    from pm4py.algo.discovery.footprints import algorithm as footprints_discovery

    fp_log = footprints_discovery.apply(
        log, variant=footprints_discovery.Variants.ENTIRE_EVENT_LOG
    )
    fp_net = footprints_discovery.apply(
        model.net, model.initial_marking, model.final_marking
    )
    return fp_log, fp_model
