class Solution:
    def isPalindrome(self, x: int) -> bool:
        # save a copy to check with reversed number
        x_copy = x

        # Initialize variable to store the reverse
        x_reverse = 0

        # iterate till the number has digits
        while x > 0:
            # fetch digit at ones place number by remainder division with 10
            x_reverse = x_reverse*10 + (x % 10)
            x //= 10

        # check if number is equal to the reversed number
        return x_copy == x_reverse
