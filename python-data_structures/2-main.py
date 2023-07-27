#!/usr/bin/python3
multiple_returns = __import__('2-multiple_returns').multiple_returns

sentence = "At Holberton school, I learnt C!"
length, first = multiple_returns(sentence)

sentence1=""
length1, first1 = multiple_returns(sentence1)
print("Length: {:d} - First character: {}".format(length, first))
print("Length: {:d} - First character: {}".format(length1, first1))
