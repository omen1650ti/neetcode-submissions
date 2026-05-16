class Solution:
    def reverseBits(self, n: int) -> int:
        shift =0
        print(n)
        print(n&1)
        for i in range(0,32):
            bit = n & 1
            print(bit)
            shift = shift << 1 | bit
            print(shift)
            n = n>>1
        return shift
