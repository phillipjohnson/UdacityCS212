import unittest
import poker

class PokerTest(unittest.TestCase):
	straight_flush = "6C 7C 8C 9C TC".split()
	four_kind = "9D 9H 9C 9S".split()
	full_house = "TD TC TH 7C 7D".split()
	
	def test_straight_flush_beats_all(self):
		hands = [self.straight_flush,self.four_kind,self.full_house]
		self.assertTrue(poker.poker(hands)==self.straight_flush)

	def test_4k_beats_full_house(self):
		hands = [self.four_kind,self.full_house]
		self.assertTrue(poker.poker(hands)==self.four_kind)

	def test_full_house_against_self_returns_self(self):
		hands = [self.full_house,self.full_house]
		self.assertTrue(poker.poker(hands)==self.full_house)		

	def test_solo_player(self):
		hands = [self.full_house]
		self.assertTrue(poker.poker(hands)==self.full_house)

	def test_100_players(self):
		hands = [self.full_house] * 99
		hands + [self.straight_flush]
		self.assertTrue(poker.poker(hands)==self.straight_flush)	

if __name__ == '__main__':
    unittest.main()