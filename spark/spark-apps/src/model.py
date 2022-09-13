class Event:
    def __init__(
        self,
        case_concept_name,
        case_task_de,
        case_event_type,
        case_user,
        time_timestamp,
        case_task_type,
        case_task_name,
        concept_name,
    ):
        self.case_concept_name = case_concept_name
        self.case_task_de = case_task_de
        self.case_event_type = case_event_type
        self.case_user = case_user
        self.time_timestamp = time_timestamp
        self.case_task_type = case_event_type
        self.case_task_name = case_task_name
        self.concept_name = concept_name


class EventLogs():
    def __init__(self, sdf):
        self.sdf = sdf
        self.df = None
        self.adf = None

    def get_spark_dataframe():
        return self.sdf

    def get_dataframe():
        if not self.df:
            return sdf.toPandas()
        return self.df

    def get_adapted_dataframe():
        if not self.adf:
            self.adf = self._adapt_columns()
        return self.adf

    def _adapt_columns(self):
        df = copy(self.get_dataframe())
        df.columns = [
                "case:concept:name",
                "case:task:de",
                "case:event:type",
                "case:user",
                "time:timestamp",
                "case:task:type",
                "case:task:name",
                "concept:name",
            ]
        return df


class ProcessModel:
    def __init__(self, net, initial_marking, final_marking):
        self.net = net
        self.initial_marking = initial_marking
        self.final_marking = final_marking
