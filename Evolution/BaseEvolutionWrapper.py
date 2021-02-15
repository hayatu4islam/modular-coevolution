from Evolution.BaseEvolutionaryGenerator import BaseEvolutionaryGenerator

import abc
import os


class BaseEvolutionWrapper(metaclass=abc.ABCMeta):
    def __init__(self, data_collector=None, log_subfolder="", log_filenames=None):
        if log_filenames is None:
            log_filenames = list()
        self.log_filenames = log_filenames

        self.evaluation_ID_counter = 0
        self.evaluation_table = dict()
        self.remaining_evolution_evaluations = list()

        self.generation = 0

        if log_subfolder != "" and not log_subfolder.startswith("/"):
            log_subfolder = "/" + log_subfolder
        self.log_path = "Logs" + log_subfolder

        if not os.path.exists(self.log_path):
            os.makedirs(self.log_path)

        self.log_files = self.open_log_files(truncate=True)
        self.data_collector = data_collector

        self.start_generation()

    @abc.abstractmethod
    def next_generation(self):
        pass

    @abc.abstractmethod
    def start_generation(self):
        pass

    @abc.abstractmethod
    def get_evaluation_members(self, evaluation_ID):
        pass

    @abc.abstractmethod
    def get_remaining_evaluations(self):
        pass

    def claim_evaluation_id(self):
        evaluation_ID = self.evaluation_ID_counter
        self.evaluation_ID_counter += 1
        return evaluation_ID

    @abc.abstractmethod
    def send_objectives(self, evaluation_ID, objectives, average_flags=None,
                        average_fitness=True, inactive_objectives=None):
        pass

    def open_log_files(self, truncate):
        log_files = list()
        for filename in self.log_filenames:
            log_file = open(f"{self.log_path}/{filename}", "a+")
            if truncate:
                log_file.truncate(0)
            log_files[filename] = log_file
        return log_files

    @abc.abstractmethod
    def __getstate__(self):
        pass

    @abc.abstractmethod
    def __setstate__(self, state):
        self.__dict__.update(state)
        self.log_files = self.open_log_files(truncate=False)


class EvolutionEndedException(Exception):
    pass
