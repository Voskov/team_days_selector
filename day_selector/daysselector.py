import random
from typing import List


class DaysSelector:
    DAYS = [1, 2, 3, 4, 5]
    TEAM = ['Ariel', 'Ofir', 'Harel', 'Udi', 'Josef']

    def __init__(self):
        self.wanted = {person: self.DAYS for person in self.TEAM}
        self.days = {day: self.TEAM for day in self.DAYS}

    def update_wanted_days(self, person: str, days: List[int]) -> None:
        self.wanted[person] = days
        # for day in days:
        #     self.days[day].append(person)

    def distribute_shifts(self):
        shifts = {}
        for day in self.DAYS:
            shifts[day] = random.sample(self.days[day], 3)
        return shifts


ds = DaysSelector()
print(ds.distribute_shifts())