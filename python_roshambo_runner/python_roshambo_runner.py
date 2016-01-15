# -*- coding: utf-8 -*-
import sys
import random

from prettytable import PrettyTable

from bots import *

ROUNDS = 1000


class RoShamBo():
    def __init__(self):
        self.bots = []
        self.result_table = PrettyTable(["Bot Name", "Hand Total", "Losses",
                                         "Ties", "Wins", "Score"])
        self._load_bots()
        self._setup_table()

    def _load_bots(self):
        bots = [key for key in sys.modules.keys() if key.startswith("bots.")]
        for b in bots:
            function_name = sys.modules[b].__entryfunction__
            bot = {}
            bot['name'] = sys.modules[b].__botname__
            bot['function'] = getattr(sys.modules[b], function_name)
            bot['totalhands'] = 0
            bot['wins'] = []
            bot['losses'] = []
            bot['ties'] = []
            self.bots.append(bot)

    def _setup_table(self):
        self.result_table.align['Bot Name'] = 'l'
        self.result_table.padding_width = 1

    def generate_results(self):
        results = sorted(self.bots, key=lambda k: k['score'], reverse=True)
        for bot in results:
            self.result_table.add_row([bot['name'], bot['totalhands'],
                                      len(bot['losses']), len(bot['ties']),
                                      len(bot['wins']), bot['score']])

    def run_match(self, player1, player2):
        player1_score = 0
        player2_score = 0
        player1_match = []
        player2_match = []
        for round_count in range(ROUNDS):
            player1_match.append(player1['function'](player2_match))
            player2_match.append(player2['function'](player1_match))
            hand_result = self.compare_hand(player1_match[round_count],
                                            player2_match[round_count])
            if hand_result == 0:
                # leaving in here in case there is any work to do in the event
                # of a hand tie
                pass
            elif hand_result == 1:
                player1_score = player1_score + 1
            elif hand_result == 2:
                player2_score = player2_score + 1
            else:
                print("Shit fucked up")
        player1['totalhands'] = player1['totalhands'] + player1_score
        player2['totalhands'] = player2['totalhands'] + player2_score
        if player1_score == player2_score:
            return 0
        elif player1_score > player2_score:
            return 1
        elif player1_score < player2_score:
            return 2
        else:
            return False  # this should no happen but just being safe

    def run_tourney(self):
        bot_index = 0
        for bot in self.bots:
            bot_index = bot_index + 1
            if bot_index > len(self.bots):
                return
            for opp in self.bots[bot_index:]:
                winner = self.run_match(bot, opp)
                if winner == 0:
                    bot['ties'].append(opp)
                    opp['ties'].append(bot)
                elif winner == 1:
                    bot['wins'].append(opp)
                    opp['losses'].append(bot)
                elif winner == 2:
                    bot['losses'].append(opp)
                    opp['wins'].append(bot)
                else:
                    return False  # should never get here
        for bot in self.bots:
            bot['score'] = (len(bot['wins']) * 2) + len(bot['ties'])

    def compare_hand(self, p1, p2):
        if p1 == p2:
            return 0
        elif (p1 - p2 + 3) % 3 == 1:
            return 1
        else:
            return 2

    @classmethod
    def test_bots(self):
        bots = [key for key in sys.modules.keys() if key.startswith("bots.")]
        for b in bots:
            try:
                function_name = sys.modules[b].__entryfunction__
            except:
                print("{} failed: no __entryfunction__")

            bot = {}
            try:
                bot['name'] = sys.modules[b].__botname__
            except:
                print("{} failed: no __botname__".format(b))

            try:
                bot['function'] = getattr(sys.modules[b], function_name)
            except:
                print("{} failed: no function_name".format(b))

            test_array = []
            try:
                bot['function'](test_array)
            except:
                print("{} failed: zero length array".format(b))

            test_array = [random.randrange(0, 3) for _ in range(1000)]
            try:
                bot['function'](test_array)
            except:
                print("{} failed: full length array".format(b))
