class Solution:
    def stoneGame(self, piles: list[int]) -> bool:
        alice = 0
        bob = 0
        for i in range(len(piles)):
            if i % 2 == 0:
                alice += piles[i]
            elif i % 2 != 0:
                bob += piles[i]

        if alice > bob:
            return True
        else:

            rev = piles[::-1]

            alice2 = 0
            bob2 = 0
            for k in range(len(rev)):
                if k % 2 == 0:
                    alice2 += rev[k]
                elif k % 2 != 0:
                    bob2 += rev[k]
                
            if alice2 > bob2:
                return True
            else:
                return False 






            