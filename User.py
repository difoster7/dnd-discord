# User Class
from datetime import date
from Character import Character


class User:

    def __init__(self, user_id):
        self.user_id = user_id
        self.join_date = date.today()
        self.games_played = 0
        self.character_slots = 1
        self.characters = []
        self.active_character = None

    def create_new_character(self, char_name):
        """
        Creates a new character if there's available space
        :param name: (str) name of the character
        :return: 0 if success, -1 general error, -2 no character slots left
        """
        if len(self.characters) >= self.character_slots:
            return -1
        else:
            try:
                self.characters.append(Character(char_name))
            except BaseException:
                # Add something in here that prints to an error log
                return -2
            return 0

    def switch_active_character(self, char_name):
        """
        Switches the active character
        :param char_name: (str) name of the character to switch to
        :return: 0 on success, -1 general error, -2 if character is not found
        """

        # search for char_name in characters[]
        # update active_char if found
        return -1
