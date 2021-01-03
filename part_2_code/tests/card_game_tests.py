import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    
    def setUp(self):
        self.card_1 = Card("spade", 1)
        self.card_2 = Card("spade", 3)
        self.card_3 = Card("spade", 10)
        

        self.cards = [self.card_1, self.card_2, self.card_3]


    def test_value_is_1(self):
        self.assertEqual(1, self.card_1.value)

    def test_suit_is_spades(self):
        self.assertEqual('spade', self.card_2.suit)

    def test_card_is_ace__True(self):
        self.assertEqual(True, CardGame.check_for_ace(1, self.card_1))

    def test_card_is_ace__False(self):
        self.assertEqual(False, CardGame.check_for_ace(3, self.card_2))

    # def test_card1_is_greater__true(self):
    #     result = CardGame.highest_card(self.card_1, self.card_2, self.card_3)
    #     self.assertEqual(card_1, result)