# In this challenge, the task is to debug the existing code to successfully execute all provided test files.
# Consider that vowels in the alphabet are a, e, i, o, u and y.
# Function score_words takes a list of lowercase words as an argument and returns a score as follows:
# The score of a single word is  if the word contains an even number of vowels. Otherwise, the score of this word is .
# The score for the whole list of words is the sum of scores of all words in the list.
# Debug the given function score_words such that it returns a correct score.
# Your function will be tested on several cases by the locked template code.
# Input Format
# The input is read by the provided locked code template.
# In the first line, there is a single integer  denoting the number of words. In the second line, there are  space-separated lowercase words.
# Constraints
# Each word has at most  letters and all letters are English lowercase letters
# Output Format
# The output is produced by the provided and locked code template.
# It calls function score_words with the list of words read from the input as the argument and prints the returned score to the output.

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math


def score_words(list_word):
    score = 0
    vowels = 'aeiouy'

    for word in list_word:
        # check for a, e, i, o, u and y
        vowels_cnt = [0, 0, 0, 0, 0, 0, 0]
        for letter in word:
            index = vowels.find(letter)
            if index > -1:
                vowels_cnt[index] += 1

        if math.fsum(vowels_cnt) % 2 == 0:
            score = score + 2
        else:
            score = score + 1

    print(score)


n = input()
instr = input()
listwords = instr.split(' ')
score_words(listwords)