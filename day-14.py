from os import pathsep
from pathlib import Path
import numpy as np
from abc import abstractmethod


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

template = line_parser.template
rules = line_parser.rules

iterations = 10
element_counter = {}


def update_counter(template):
    for e in template:
        if e in element_counter:
            element_counter[e] += 1
        else:
            element_counter[e] = 1


update_counter(template)
step = 1
while step < iterations + 1:
    #print(step)
    i = 0
    new_template = ""
    while (i + 1) < len(template):
        new_template += template[i]
        section = template[i : i + 2]
        new_template += rules[section]
        update_counter(rules[section])
        i += 1
    new_template += template[i]
    template = new_template
    #print(element_counter)
    step += 1

print(max(element_counter.values()) - min(element_counter.values()))
