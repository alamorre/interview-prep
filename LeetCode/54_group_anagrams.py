from typing import List 
from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans_dict = {}
        for word in strs:
            char_counts = [0] * 26
            for char in word:
                char_counts[ord(char) % 26] += 1
            anagram_list = ans_dict.get(str(char_counts), [])
            anagram_list.append(word)
            ans_dict[str(char_counts)] = anagram_list
        return list(ans_dict.values())
    [].pop(0)

print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

"""
Your runtime analysis was wrong. You assumed sorted by default and 
a linear time to construct the collection. Even if its sorted by default thats 
still nlgn...

Because we know the chars are english letters, there is a range limit of 26.
This allows us to effectively sort in linear time!!!!!

Practice a linear sort on known ranges below. 
CAPITALIZE ON THE CHAR LIMITATIONS!!!!!!
"""