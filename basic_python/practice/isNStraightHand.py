def isNStraightHand(hand, groupSize):
    if len(hand) % groupSize != 0:
        return False
    else:
        while hand:
            for i in range(int(len(hand)/groupSize)):
                m = min(hand)
                a = 0
                while a < groupSize:
                    if m in hand:
                        hand.remove(m)
                        m += 1
                        a += 1
                    else:
                        return False
        return not hand


print(isNStraightHand([1,2,3,6,2,3,4,7,9], 3))