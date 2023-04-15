# Code de https://towardsdatascience.com/how-to-win-over-70-matches-in-rock-paper-scissors-3e17e67e0dab
# Modifié, adapté et francisé (commentaire) par Audrey Guy 2023-04-17

from __future__ import division
import random
import itertools

# dictionnaire des combinaisons gagnantes
beat = {'rock': 'paper', 'paper': 'scissor', 'scissor': 'rock'}


# Classe d'implémentation d'une chaîne de Markov
class MarkovChain:

    def __init__(self, order, decay=1.0):
        self.decay = decay
        self.matrix = self.create_matrix(order)

    @staticmethod
    def create_matrix(order):
        """
        Permet de créer la matrice de probabilité selon l'ordre désiré

        :param order:
        :return:
        """

        def create_keys(order):
            """
            Crée le dictionnaire permettant d'accéder aux éléments de la matrice

            :param order:
            :return:
            """

            keys = ['rock', 'paper', 'scissor']

            for i in range((order * 2 - 1)):
                key_len = len(keys)
                for i in itertools.product(keys, keys):
                    keys.append(''.join(i))
                keys = keys[key_len:]

            return keys

        keys = create_keys(order)

        matrix = {}
        for key in keys:
            matrix[key] = {'rock': {'prob': 1 / 3,
                                    'n_obs': 0
                                    },
                           'paper': {'prob': 1 / 3,
                                     'n_obs': 0
                                     },
                           'scissor': {'prob': 1 / 3,
                                       'n_obs': 0
                                       }
                           }

        return matrix

    # Exemple de matrice une fois formée
    # markov_model.matrix
    # {'PP': {'P': {'n_obs': 0, 'prob': 0.3333333333333333},
    #         'R': {'n_obs': 0, 'prob': 0.3333333333333333},
    #         'S': {'n_obs': 0, 'prob': 0.3333333333333333}},
    #  'PR': {'P': {'n_obs': 0, 'prob': 0.3333333333333333},
    #         'R': {'n_obs': 0, 'prob': 0.3333333333333333},
    #         'S': {'n_obs': 0, 'prob': 0.3333333333333333}},
    #  'PS': {'P': {'n_obs': 0, 'prob': 0.3333333333333333},
    #         'R': {'n_obs': 0, 'prob': 0.3333333333333333},
    #         'S': {'n_obs': 0, 'prob': 0.3333333333333333}},
    #  'RP': {'P': {'n_obs': 0, 'prob': 0.3333333333333333},
    #         'R': {'n_obs': 0, 'prob': 0.3333333333333333},
    #         'S': {'n_obs': 0, 'prob': 0.3333333333333333}}, ...

    def update_matrix(self, pair, input):
        """
        Rafraîchi les probabilités à chaque coup joué

        :param pair:
        :param input:
        :return:
        """

        for i in self.matrix[pair]:
            self.matrix[pair][i]['n_obs'] = self.decay * self.matrix[pair][i]['n_obs']

        self.matrix[pair][input]['n_obs'] = self.matrix[pair][input]['n_obs'] + 1

        n_total = 0
        for i in self.matrix[pair]:
            n_total += self.matrix[pair][i]['n_obs']

        for i in self.matrix[pair]:
            self.matrix[pair][i]['prob'] = self.matrix[pair][i]['n_obs'] / n_total

    def predict(self, pair):
        """
        Prédiction du coup à jouer selon les statistiques des derniers coups

        :param pair:
        :return:
        """

        probs = self.matrix[pair]

        if max(probs) == min(probs):
            return random.choice(['rock', 'paper', 'scissor'])
        else:
            if max([(i[1], i[0]) for i in probs.items().mapping])[1] == 'r':
                return 'rock'
            elif max([(i[1], i[0]) for i in probs.items().mapping])[1] == 'p':
                return 'paper'
            elif max([(i[1], i[0]) for i in probs.items().mapping])[1] == 's':
                return 'scissor'


class RandomPredictor:

    @staticmethod
    def predict():
        return random.choice(['rock', 'paper', 'scissor'])


class RPCMarkov:

    def __init__(self):
        self.random_predictor = RandomPredictor()
        self.computer_move = self.random_predictor.predict()
        self.markov_model = MarkovChain(1, 0.9)

        self.pair_diff2 = ''
        self.pair_diff1 = ''

    def play(self, user_move):
        """
        Lorsqu'un coup est joué, cette fonction est appelée pour déterminer le prochain coup de l'ordinateur

        :param user_move:
        :return:
        """
        # the first round
        if user_move == '':
            self.pair_diff2 = ''
            self.pair_diff1 = ''

        # further rounds
        else:
            self.pair_diff2 = self.pair_diff1
            self.pair_diff1 = self.computer_move + user_move

        if self.pair_diff2 != '':
            self.markov_model.update_matrix(self.pair_diff2, user_move)
            self.computer_move = beat[self.markov_model.predict(self.pair_diff1)]

        else:
            self.computer_move = self.random_predictor.predict()

        return self.computer_move
