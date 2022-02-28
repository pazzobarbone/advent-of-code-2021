from pathlib import Path
from abc import abstractmethod
from copy import deepcopy


class State:
    @abstractmethod
    def parse_line(self, line, context):
        pass


class TemplateState(State):
    def parse_line(self, line, context):
        line = line.strip()
        if line:
            context._template = line

        else:
            context.set_new_state(RuleState())


class RuleState(State):
    def parse_line(self, line, context):
        line = line.strip()
        if line:
            rule = line.split(" -> ")
            context._rules[rule[0]] = rule[1]
        else:
            context._done = True


class LineParser:
    def __init__(self, initial_state):
        self._state = initial_state
        self._template = None
        self._rules = {}
        self._done = False

    @property
    def state(self):
        return self._state

    @property
    def done(self):
        return self._done

    @property
    def template(self):
        return self._template

    @property
    def rules(self):
        return self._rules

    def set_new_state(self, state):
        self._state = state

    def parse_line(self, line):
        self._state.parse_line(line, self)


this_file = Path(__file__)
line_parser = LineParser(TemplateState())
with open(this_file.parent / "input.txt") as file:
    while not line_parser.done:
        line_parser.parse_line(file.readline())