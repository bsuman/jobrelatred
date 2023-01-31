# RomanToInt
# For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II.
# The number 27 is written as XXVII, which is XX + V + II.
# Roman numerals are usually written largest to smallest from left to right.
# However, the numeral for four is not IIII. Instead, the number four is written as IV.
# Because the one is before the five we subtract it making four.
# The same principle applies to the number nine, which is written as IX.
# There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.

def romanToInt(s: str) -> int:
    symbol_to_value_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    ch_num = 0
    final_num = 0
    while ch_num < len(s):
        if s[ch_num] == 'I' and ch_num + 1 < len(s) and s[ch_num + 1] == 'V':
            val = 4
            ch_num += 2
        elif s[ch_num] == 'I' and ch_num + 1 < len(s) and s[ch_num + 1] == 'X':
            val = 9
            ch_num += 2
        elif s[ch_num] == 'X' and ch_num + 1 < len(s) and s[ch_num + 1] == 'C':
            val = 90
            ch_num += 2
        elif s[ch_num] == 'X' and ch_num + 1 < len(s) and s[ch_num + 1] == 'L':
            val = 40
            ch_num += 2
        elif s[ch_num] == 'C' and ch_num + 1 < len(s) and s[ch_num + 1] == 'D':
            val = 400
            ch_num += 2
        elif s[ch_num] == 'C' and ch_num + 1 < len(s) and s[ch_num + 1] == 'M':
            val = 900
            ch_num += 2
        else:
            val = symbol_to_value_map[s[ch_num]]
            ch_num += 1
        final_num = final_num + val
    return final_num


if __name__ == '__main__':
    print(romanToInt("MCMXCIV"))
    print(romanToInt("LVIII"))
    print(romanToInt("III"))