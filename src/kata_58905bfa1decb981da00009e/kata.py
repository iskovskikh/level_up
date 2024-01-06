# class Dinglemouse(object):
#     up_queues = {}
#     down_queues = {}
#     cabin = []
#     current_floor = 0
#     next_stops = []
#     result_stops = [0, ]
#     next_floor_list = []
#
#     def __init__(self, queues, capacity):
#         self.capacity = capacity
#         self.result_stops = [0, ]
#
#         for index, item in enumerate(queues):
#             if item:
#                 up = list(filter(lambda x: x > index, item))
#                 if up:
#                     self.up_queues[index] = sorted(up)
#                 down = list(filter(lambda x: x < index, item))
#                 if down:
#                     self.down_queues[index] = sorted(down, reverse=True)
#
#     @property
#     def cabin_capacity(self):
#         return self.capacity - len(self.cabin)
#
#     def load_passengers(self, direction: bool):
#
#         while self.cabin_capacity > 0 and self.floor_has_passengers(direction):
#             if direction:
#                 self.cabin.append(self.up_queues[self.current_floor].pop())
#                 if not self.up_queues[self.current_floor]:
#                     self.up_queues.pop(self.current_floor)
#             else:
#                 self.cabin.append(self.down_queues[self.current_floor].pop())
#                 if not self.down_queues[self.current_floor]:
#                     self.down_queues.pop(self.current_floor)
#
#     def unload_passengers(self):
#         self.cabin = list(filter(lambda x: x != self.current_floor, self.cabin))
#
#     def travel_to_floor(self, floor):
#         if self.current_floor != floor:
#             self.current_floor = floor
#             self.result_stops.append(floor)
#
#     def get_next_floor(self, direction: bool) -> list[int]:
#         if direction:
#             queue = list(self.up_queues.keys()) if self.cabin_capacity > 0 else []
#         else:
#             queue = list(self.down_queues.keys()) if self.cabin_capacity > 0 else []
#         cabin = self.cabin
#         return sorted(list(set(cabin + queue)), reverse=not direction)
#
#     def lift(self, direction: bool):
#         self.next_floor_list = self.get_next_floor(direction=direction)
#
#         while self.next_floor_list:
#             self.travel_to_floor(self.next_floor_list[0])
#             self.unload_passengers()
#             self.load_passengers(direction=direction)
#             self.next_floor_list = self.get_next_floor(direction=direction)
#             print("cabin\t", self.cabin, self.current_floor, direction, self.next_floor_list)
#
#     def theLift(self):
#         print("capacity\t", self.capacity)
#
#         while self.up_queues or self.down_queues:
#             print("Up\t", self.up_queues)
#             print("Down\t", self.down_queues)
#             self.lift(direction=True)
#             self.lift(direction=False)
#
#         if self.current_floor != 0:
#             self.travel_to_floor(0)
#
#         return self.result_stops
#
#     def floor_has_passengers(self, direction):
#         if direction:
#             if self.current_floor in self.up_queues:
#                 if len(self.up_queues[self.current_floor]) > 0:
#                     return True
#                 else:
#                     self.up_queues.pop(self.current_floor)
#             return False
#         else:
#             if self.current_floor in self.down_queues:
#                 if len(self.down_queues[self.current_floor]) > 0:
#                     return True
#                 else:
#                     self.down_queues.pop(self.current_floor)
#             return False
from enum import Enum


class Direction(Enum):
    UP = "UP"
    DOWN = "DOWN"


class Dinglemouse(object):
    current_floor = 0
    result_stops = [0, ]
    cabin = []

    def __init__(self, queues, capacity):
        self.capacity = capacity
        self.queue = dict()
        self.queue[Direction.UP] = {}
        self.queue[Direction.DOWN] = {}
        self.result_stops = [0, ]

        for index, item in enumerate(queues):
            if item:
                print(item)
                up = list(filter(lambda x: x > index, item))
                if up:
                    self.queue[Direction.UP][index] = up
                down = list(filter(lambda x: x < index, item))
                if down:
                    self.queue[Direction.DOWN][index] = down

    def travel_to_floor(self, *, floor: int):
        if self.current_floor != floor:
            self.current_floor = floor
            self.result_stops.append(floor)
            # print(f'Лифт приехал на {floor} этаж')

    @property
    def cabin_capacity(self):
        return self.capacity - len(self.cabin)

    def get_next_floor_list(self, *, direction: Direction) -> list:
        queue = list(self.queue[direction].keys())
        cabin = self.cabin
        return sorted(list(set(cabin + queue)), reverse=direction != Direction.UP)

    def floor_has_passengers(self, *, direction: Direction) -> bool:
        return (self.current_floor in self.queue[direction]) and (self.queue[direction][self.current_floor] != [])

    def get_passenger_from_current_floor(self, *, direction: Direction) -> int:
        passenger = self.queue[direction][self.current_floor].pop(0)
        if not self.floor_has_passengers(direction=direction):
            self.queue[direction].pop(self.current_floor)
        return passenger

    def load_passengers(self, *, direction: Direction):
        while self.cabin_capacity > 0 and self.floor_has_passengers(direction=direction):
            passenger=self.get_passenger_from_current_floor(direction=direction)
            self.cabin.append(passenger)
            # print(f'Забрали пассажира едущего c {self.current_floor} этажа на {passenger} этаж')

    def unload_passengers(self):
        while self.current_floor in self.cabin:
            self.cabin.remove(self.current_floor)
            # print(f'Пассажир вышел на {self.current_floor} этаже')

    def lift(self, *, direction: Direction):
        next_floor = self.get_next_floor_list(direction=direction)

        while next_floor:
            self.travel_to_floor(floor=next_floor[0])
            self.unload_passengers()
            self.load_passengers(direction=direction)
            next_floor = list(filter(
                lambda x: (x > self.current_floor) if direction == Direction.UP else (x < self.current_floor),
                self.get_next_floor_list(direction=direction)
            ))

        self.unload_passengers()

    def theLift(self):

        while self.queue[Direction.UP] or self.queue[Direction.DOWN]:
            print(self.queue, self.capacity)
            # print('========== UP ===============')
            self.lift(direction=Direction.UP)
            # print("========== DoWN ===============")
            self.lift(direction=Direction.DOWN)
        if self.current_floor != 0:
            self.travel_to_floor(floor=0)
        return self.result_stops
