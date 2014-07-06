def poker(hands):
    "Return the best hand: poker([hand,...]) => hand"
    return max(hands, key=hand_rank)

def card_ranks(cards):
    "Return a list of the ranks, sorted with higher first."
    ranks = [r for r,s in cards]
    rankDict = {"A":14,"K":13,"Q":12,"J":11,"T":10}
    ranks = [int(rankDict.get(r,r)) for r in ranks]
    ranks.sort(reverse=True)
    return ranks

def straight(ranks):
    for i in range(1,len(ranks)):
        if ranks[i-1] - ranks[i] > 1:
            return False
    return True

def flush(hand):
    suits = [s for r,s in hand]
    return len(set(suits)) <= 1

def kind(n, ranks):
    """Return the first rank that this hand has exactly n of.
    Return None if there is no n-of-a-kind in the hand."""
    for search_rank in set(ranks):
        if ranks.count(search_rank)==n:
            return search_rank
    return None

def two_pair(ranks):
    """If there are two pair, return the two ranks as a
    tuple: (highest, lowest); otherwise return None."""
    pair1 = kind(2,ranks)
    pair2 = None
    if pair1:
        pair2 = kind(2,[r for r in ranks if r!=pair1])
    if pair1 and pair2:
        return (pair1,pair2)

    return None

def hand_rank(hand):
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):            # straight flush
        return (8, max(ranks))
    elif kind(4, ranks):                           # 4 of a kind
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):        # full house
        return (6,kind(3,ranks),kind(2,ranks))
    elif flush(hand):                              # flush
        return (5,ranks)
    elif straight(ranks):                          # straight
        return (4,max(ranks))
    elif kind(3, ranks):                           # 3 of a kind
        return (3,kind(3,ranks),ranks)
    elif two_pair(ranks):                          # 2 pair
        return (2,two_pair(ranks),ranks)
    elif kind(2, ranks):                           # kind
        return (1,kind(2,ranks),ranks)
    else:                                          # high card
        return (0,ranks)