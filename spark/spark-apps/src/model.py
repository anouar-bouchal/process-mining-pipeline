class Event():
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


class ProcessModel():
    def __init__(self, net, initial_marking, final_marking):
        self.net = net
        self.initial_marking = initial_marking
        self.final_marking = final_marking