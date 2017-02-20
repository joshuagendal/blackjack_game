import unittest

from blackjack_gendal import check_aces_players, check_aces_dealer

class BlackJackTests(unittest.TestCase):

    def startingHandsToTest(self):
        self.player_test_hand = []
        self.dealer_test_hand = []

    def testCheckPlayerAces1(self):
        res = check_aces_players([[1, 10], [1, 9]])         # The check_aces_players function should notice that the sum of each of these lists + 10 would make the total between 17 and 21
        self.assertEqual(res, [[1, 10, 10], [1, 9, 10]])

    def testCheckPlayerAces2(self):                               # a list of [1, 6] is the lowest number that should add 10 to it (see function)
        res = check_aces_players([[1, 5], [1, 6]])
        self.assertEqual(res, [[1, 5], [1, 6, 10]])        # Here I make sure that [1, 5] DOES NOT add the 10 and [1, 6] does because the latter list plus 10 = 17

    def testCheckPlayerAces3(self):
        res = check_aces_players([[1, 2], [1, 3]])
        self.assertEqual(res, [[1, 2], [1, 3]])

    def testCheckPlayerAces4(self):            # Here I will check starting cards that would add 10 IF there was an ace, but there is no ace in hand
        res = check_aces_players([[2, 8], [2, 7], [3, 6], [3, 5], [4, 4], [4, 6], [5, 4], [5, 5]])
        self.assertEqual(res, [[2, 8], [2, 7], [3, 6], [3, 5], [4, 4], [4, 6], [5, 4], [5, 5]])

    def testCheckDealerAces1(self):
        res = check_aces_dealer([1, 10])
        self.assertEqual(res, [1, 10, 10])

    def testCheckDealerAces2(self):
        res = check_aces_dealer([1, 8])
        self.assertEqual(res, [1, 8, 10, 0])

    def testCheckDealerAces3(self):
        res = check_aces_dealer([2, 8])
        self.assertEqual(res, [2, 8])

    def testCheckDealerAces4(self):
        res = check_aces_dealer([4, 6])
        self.assertEqual(res, [4, 6])    

if __name__ == '__main__':
    unittest.main()
