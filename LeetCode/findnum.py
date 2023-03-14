import math
def solution(S):
    # Implement your solution here
    sum = 0
    num_nums = 0
    nums = S.split(',')
    for num in nums:
        try:
            if not math.isnan(float(num)):
                num_nums=num_nums + 1
                sum = sum+float(num)
        except ValueError:
            continue

    if num_nums > 0:
        return math.floor(sum/num_nums)
    else:
        return 0

import re
def average_numbers_in_string(string):
    numbers = re.findall(r'\d+', string)
    if not numbers:
        return 0
    else:
        numbers = [int(num) for num in numbers]
        avg = sum(numbers) / len(numbers)
        return math.floor(avg)

if __name__ == "__main__":
    S = "2.5,2.5,e,2.5,7.5"
    print(average_numbers_in_string(S))
    S = "1,-2.5,e,7"
    print(solution(S))