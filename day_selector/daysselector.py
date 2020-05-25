from typing import List


class DaysSelector:
    def __init__(self):
        self.wanted = {}
        self.days = {}

    def update_wanted_days(self, person: str, days: List[int]) -> dict:
        self.wanted[person] = days
        for day in days:
            self.days[day].append(person)
        return self.wanted

    def distribute_shifts(self):
        for day in range(1, 6):
            pass
