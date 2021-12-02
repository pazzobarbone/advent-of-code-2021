from pathlib import Path


class SubmarinePart1:
    def __init__(self):
        self._horizontal_position = 0
        self._depth = 0

    @property
    def horizontal_position(self):
        return self._horizontal_position

    @property
    def depth(self):
        return self._depth

    def move(self, input):
        command = input.split()
        move_handles = {
            "forward": self.forward_handle,
            "up": self.up_handle,
            "down": self.down_handle,
        }
        move_handles[command[0]](int(command[1]))

    def forward_handle(self, magnitude):
        self._horizontal_position += magnitude

    def up_handle(self, magnitude):
        self._depth -= magnitude

    def down_handle(self, magnitude):
        self._depth += magnitude


class SubmarinePart2(SubmarinePart1):
    def __init__(self):
        super().__init__()
        self._aim = 0

    @property
    def aim(self):
        return self._aim

    def forward_handle(self, magnitude):
        self._horizontal_position += magnitude
        self._depth += self._aim * magnitude

    def up_handle(self, magnitude):
        self._aim -= magnitude

    def down_handle(self, magnitude):
        self._aim += magnitude


submarine1 = SubmarinePart1()
submarine2 = SubmarinePart2()
this_file = Path(__file__)
with open(this_file.parent / "input.txt") as file:
    depth_measurements = list()
    for line in file.readlines():
        submarine1.move(line)
        submarine2.move(line)

print(submarine1.horizontal_position * submarine1.depth)
print(submarine2.horizontal_position * submarine2.depth)
