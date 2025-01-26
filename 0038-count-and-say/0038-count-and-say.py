class Solution:
    def countAndSay(self, n: int) -> str:
        rle = "1"
        for i in range(1, n):
            new_rle = ""
            count = 1
            for j in range(1,len(rle)):
                if rle[j] == rle[j-1]:
                    count += 1
                else:
                    new_rle += (str(count) + rle[j-1])
                    count = 1
            new_rle += (str(count) + rle[-1])
            rle = new_rle
        return rle
            