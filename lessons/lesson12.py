class Solution:
    def intToRoman(self, num: int) -> str:
        # Convert num to string
        M = str(num)
        # Pad with leading zeros
        M = (4-len(M))*'0' + M
        R = ''                                              # Initialize the Roman Numeral
        # Set the 1's and 5's values for each place
        K = [['M'], ['C', 'D'], ['X', 'L'], ['I', 'V']]
        # Iterate over the arabic numeral string
        for i in range(len(M)):
            # Convert the current numeral to integer for comparison
            d = int(M[i])
            if d < 4:                                      # If the digit is less than 4 add d number of the 1's
                R = R + d * K[i][0]  # for that place to the Roman Number
            elif d == 4:                                   # Else If the digit is 4 add one of the 1's and one of the 5's
                R = R + K[i][0] + K[i][1]  # for that place
            # Else If the digit is less than 9 (5 through 8) add one of the 5's plus
            elif d < 9:
                # ( the digit - 5 ) of the 1's for that place
                R = R + K[i][1] + (d - 5) * K[i][0]
            else:                                           # Else the value of the digit is 9 so add one of the 1's for the
                # current place plus one of the 1's for the previous place.
                R = R + K[i][0] + K[i-1][0]
        return R
