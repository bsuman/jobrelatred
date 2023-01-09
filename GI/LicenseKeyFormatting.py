# You are given a license key represented as a string s that consists of only alphanumeric characters and dashes.
# The string is separated into n + 1 groups by n dashes. You are also given an integer k.

# We want to reformat the string s such that each group contains exactly k characters,
# except for the first group, which could be shorter than k but still must contain at least one character.
# Furthermore, there must be a dash inserted between two groups, and you should convert all lowercase letters to uppercase.

# Return the reformatted license key.


def licenseKeyFormatting(s: str, k: int) -> str:
    new_s = s.replace('-', '')
    new_s = new_s.upper()
    final_str = ''
    while len(new_s) > 0:
        if len(new_s) - k > 0:
            final_str = '-' + new_s[len(new_s) - k:len(new_s) + 1] + final_str
            new_s = new_s[:len(new_s) - k]
        else:
            final_str = new_s[:len(new_s) + 1] + final_str
            new_s = ''
    return final_str


if __name__ == '__main__':
    s = "2-4A0r7-4k"
    k = 3
    print(licenseKeyFormatting(s, k))
    s = "2-5g-3-J"
    k = 2
    print(licenseKeyFormatting(s, k))
