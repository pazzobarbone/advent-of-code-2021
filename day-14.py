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

template = line_parser.template
rules = line_parser.rules

# Transform the rules from XX -> Y to XX -> XY, YX
for key in rules.keys():
    insertion = rules[key]
    rules[key] = [key[0] + insertion, insertion + key[1]]


chain_pairs = dict([(base, 0) for base in rules.keys()])

i = 0
while (i + 1) < len(template):
    section = template[i : i + 2]
    chain_pairs[section] += 1
    i += 1


# Dictionary to count the occurrences of each element
element_counter = {}


def update_counter(element, occurrences):
    if element in element_counter:
        element_counter[element] += occurrences
    else:
        element_counter[element] = occurrences


# Initialise the counter with the elements in the starting template
for e in template:
    update_counter(e, 1)


iterations = 40
for i in range(1, iterations + 1):
    temp_chain_pairs = deepcopy(chain_pairs)
    for key in chain_pairs.keys():
        new_pairs = rules[key]
        multiplicity = chain_pairs[key]
        update_counter(new_pairs[0][1], multiplicity)
        for p in new_pairs:
            temp_chain_pairs[p] += multiplicity
        temp_chain_pairs[key] -= multiplicity
    chain_pairs = deepcopy(temp_chain_pairs)
    if i == 10:
        print(max(element_counter.values()) - min(element_counter.values()))

print(max(element_counter.values()) - min(element_counter.values()))
