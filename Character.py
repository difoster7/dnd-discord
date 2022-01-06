# Character class

class Character:

    MAX_DAYS_AVAILABLE = 28

    def __init__(self, name):

        # The characters name
        self.name = name

        # Inventory
        self.food = 0
        self.gold = 0
        self.wood = 0
        self.stone = 0

        # Settlement the character is currently in
        self.settlement = ''

        # Gold gained during each day of earning
        self.earn_rate = 1

        # Crafting and other personal projects
        self.projects = []

        # Number of days the character has available to work.
        # 7 are earned each week, can 'bank' up to 4 weeks
        self.days_available = 7

    def earn(self, num_days):
        """
        Allows the character to earn gold
        :param num_days: number of days to earn for
        :return: 0 if success, -1 on general error, -2 if not enough days
        """
        if num_days > self.days_available:
            return -2
        try:
            self.days_available -= num_days
            self.gold += self.earn_rate * num_days
            return 0
        except BaseException:
            # Add error logging
            return -1

    def weekly_refresh(self):
        """
        Performs weekly refresh (there are 7 days in a week)
        :return: 0 on success, -1 on error
        """
        try:
            if self.days_available < self.MAX_DAYS_AVAILABLE - 7:
                self.days_available += 7
            else:
                self.days_available = self.MAX_DAYS_AVAILABLE
            return 0
        except BaseException:
            # Add error logging
            return -1

