import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame:
    
    # def test_value_is_1(self):
    #     self.assertEqual(1, self.check_for_ace(1))

    # def which_is_higher__card_1(self, card1, card2):
    #     self.assertEqual(self.highest_card(10), self.highest_card(9))

    # def which_is_higher__card_2(self, card1, card2):
    #     self.assertEqual(self.highest_card(8), self.highest_card(9))

    def what_is_total(self, cards):
        cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEquals(55, self.cards_total(cards))