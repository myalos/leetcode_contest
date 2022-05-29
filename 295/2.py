from typing import *

class Solution:
    def discountPrices(self, sentence : str, discount : int) -> str:
        sentence_split = sentence.split()
        for index, word in enumerate(sentence_split):
            if len(word) > 1 and word[0] == '$' and str.isdigit(word[1:]):
                price = int(word[1:])
                price = (100 - discount) * price / 100
                sentence_split[index] = f'${price:.2f}'
        return ' '.join(sentence_split)

def main():
    sol = Solution()
    _input = ("there are $1 $2 and 5$ candies in the shop", 50 )
    _output = sol.discountPrices(*_input)
    print(_output)

if __name__ == '__main__':
    main()
