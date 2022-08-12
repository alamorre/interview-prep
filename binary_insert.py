from typing import List

class Insert():
    def binary_search(self, search_term: str, sorted_terms: List[str]):
        low = 0
        high = len(sorted_terms) - 1

        while low <= high:
            mid = (low + high) // 2

            # Base cases, if terminated - determine where to place the component
            if low == high:
                if sorted_terms[low] > search_term:
                    return low
                else:
                    return low + 1
            elif low > high:
                return low

            if search_term < sorted_terms[mid]: # If our index is lower, bring high down
                high = mid - 1
            elif search_term > sorted_terms[mid]: # If our index is higher, bring low up
                low = mid + 1
            else:
                return mid
        


    def binary_insert(self, insert_term: str, sorted_terms: List[str]) -> List[str]:
        if len(sorted_terms) == 0:
            return [insert_term]

        index = self.binary_search(
            search_term=insert_term, 
            sorted_terms=sorted_terms
        )
        
        sorted_terms.insert(index, insert_term)
        return sorted_terms

insert_term = 'Cam'
terms = ['Adam', 'Bill', 'Nick', 'Ryland', 'Zak']
new_list = Insert().binary_insert(insert_term=insert_term, sorted_terms=terms)
print(new_list)