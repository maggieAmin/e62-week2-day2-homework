class Team:
    def __init__ (self, input_name, input_list_of_names, input_coach):
        self.name = input_name
        self.players = input_list_of_names
        self.coach = input_coach
        self.points = 0

    def add_player(self, new_player):
        self.players.append(new_player)

    def has_player(self,player_name):
        return player_name in self.players

    def play_game(self, has_won):
        if has_won == True:
            self.points += 3

