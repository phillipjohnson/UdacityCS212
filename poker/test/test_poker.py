import unittest
import poker

class PokerTest(unittest.TestCase):
    straight_flush = "6C 7C 8C 9C TC".split()
    four_kind = "9D 9H 9C 9S 7H".split()
    full_house = "TD TC TH 7C 7D".split()

    def test_card_ranks(self):
        self.assertEquals(poker.card_ranks(self.straight_flush),[10,9,8,7,6])
        self.assertEquals(poker.card_ranks(self.four_kind),[9,9,9,9,7])
        self.assertEquals(poker.card_ranks(self.full_house),[10,10,10,7,7])
    
    def test_straight(self):
        self.assertTrue(poker.straight([10,9,8,7,6]))
        self.assertFalse(poker.straight([10,8,7,6,5]))

    def test_flush(self):
        self.assertTrue(poker.flush(self.straight_flush))
        self.assertFalse(poker.flush(self.four_kind))

    def test_kind(self):
        fkranks = poker.card_ranks(self.four_kind)
        self.assertEquals(poker.kind(4, fkranks),9)
        self.assertEquals(poker.kind(3, fkranks),None)
        self.assertEquals(poker.kind(2, fkranks),None)
        self.assertEquals(poker.kind(1, fkranks),7)

    def test_two_pair(self):
        self.assertEquals(poker.two_pair([10,10,6,6,5]),(10,6))
        self.assertEquals(poker.two_pair([10,10,6,5,4]),None)

    def test_straight_flush_beats_all(self):
        hands = [self.straight_flush,self.four_kind,self.full_house]
        self.assertEquals(poker.poker(hands),self.straight_flush)

    def test_4k_beats_full_house(self):
        hands = [self.four_kind,self.full_house]
        self.assertEquals(poker.poker(hands),self.four_kind)

    def test_full_house_against_self_returns_self(self):
        hands = [self.full_house,self.full_house]
        self.assertEquals(poker.poker(hands),self.full_house)       

    def test_solo_player(self):
        hands = [self.full_house]
        self.assertEquals(poker.poker(hands),self.full_house)

    def test_100_players(self):
        hands = [self.full_house] * 99
        hands += [self.straight_flush]
        self.assertEquals(poker.poker(hands),self.straight_flush)   

    def test_straight_flush_rank(self):
        self.assertEquals(poker.hand_rank(self.straight_flush),(8,10))

    def test_4k_rank(self):
        self.assertEquals(poker.hand_rank(self.four_kind),(7,9,7))

    def test_full_house_rank(self):
        self.assertEquals(poker.hand_rank(self.full_house),(6,10,7))

    def test_flush_rank(self):
        hand = "KC TC 8C 5C 4C".split()
        self.assertEquals(poker.hand_rank(hand),(5,[13,10,8,5,4]))

    def test_straight_rank(self):
        hand = "JC TH 9S 8S 7D".split()
        self.assertEquals(poker.hand_rank(hand),(4,11))

    def test_3k_rank(self):
        hand = "5D 5C 5H KS TC".split()
        self.assertEquals(poker.hand_rank(hand),(3,5,[13,10,5,5,5]))

    def test_two_pair_rank(self):
        hand = "5D 5C 8H 8S TC".split()
        self.assertEquals(poker.hand_rank(hand),(2,(8,5),[10,8,8,5,5]))

    def test_pair_rank(self):
        hand = "5D 3C 8H 8S TC".split()
        self.assertEquals(poker.hand_rank(hand),(1,8,[10,8,8,5,3]))

    def test_highcard_rank(self):
        hand = "5D 3C 8H 7S TC".split()
        self.assertEquals(poker.hand_rank(hand),(0,[10,8,7,5,3]))

if __name__ == '__main__':
    unittest.main()