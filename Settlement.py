# Settlement Class

class Settlement:

    LEVEL_NAMES = {1: 'hamlet',
                   2: 'village',
                   3: 'town',
                   4: 'city',
                   5: 'metropolis'}

    def __init__(self, name, population=0, happiness=5):
        """Initializer function"""
        self.name = name
        self.population = population
        self.happiness = happiness # happiness is tracked on a scale of 1-10
        self.buildings = []
        self.buildings_in_progress = []
        self.current_events = []

        self.gold = 0
        self.stone = 0
        self.wood = 0
        self.food = 0

        # Production values are per week
        self.gold_prod = 0
        self.stone_prod = 0
        self.wood_prod = 0
        self.food_prod = 0

        self._growth_rate = -1
        self.update_growth_rate()

        self._level = -1
        self.update_level()

    def update_growth_rate(self):
        """
        1 food sustains 1 person for 1 day. 7 food/person needed/week.
        Grow if producing more food than required. Shrink if less.
        Population steady if food prod is within 10% of requirement.
        """
        required_food = self.population * 7
        famine = required_food * .9
        growth = required_food * 1.1
        if self.food_prod > growth:
            self._growth_rate = self.food_prod / growth
        elif self.food_prod < famine:
            self._growth_rate = self.food_prod / famine
        else:
            self._growth_rate = 1

    def update_level(self):
        """
        level 1: hamlet, < 100 pop
        level 2: village, 100 - 1000
        level 3: town, 1000 - 10,000
        level 4: city, 10,000 - 50,000
        level 5: metropolis, 50,000+
        More can be added later if needed
        :return:
        """
        if self.population < 100:
            self._level = 1
        elif self.population < 1000:
            self._level = 2
        elif self.population < 10000:
            self._level = 3
        elif self.population < 50000:
            self._level = 4
        else:
            self._level = 5

    def __str__(self):
        return_string = ""
        return_string += self.name + ' is a ' + self.LEVEL_NAMES.get(self._level) + \
            ' with a population of ' + str(self.population) + '.'
        return return_string

if __name__ == "__main__":
    settlement1 = Settlement('Albansville', 800, 3)
    print(settlement1)

