from typing import List

class Search:
    def binary_search(self, search_term: str, sorted_terms: List[str]) -> int:
        # Input val
        if len(sorted_terms) == 0:
            return -1
        sorted_terms.sort()
        
        low = 0
        high = len(sorted_terms) - 1
        
        while low <= high: # What is it's the vv last search? Hence <=
            mid = (high + low) // 2
            compare_term = sorted_terms[mid]

            if search_term == compare_term:
                return mid

            elif search_term < compare_term:
                high = mid - 1
                
            elif search_term > compare_term:
                low = mid + 1

        return -1

term = 'cam'
terms= ['adam', 'bill', 'bob', 'cam', 'zak']
search = Search()
index = search.binary_search(term, terms)
print(index)