from typing import List

class Insert():
    def binary_search(
            self, 
            search_term: str, 
            sorted_terms: List[str], 
            start: int, 
            end: int
        ):
        # Base cases, if terminated - determine where to place the component
        if start == end:
            if sorted_terms[start] > search_term:
                return start
            else:
                return start+1
        elif start > end:
            return start

        mid = (start+end) // 2
        if sorted_terms[mid] < search_term:
            return self.binary_search(search_term, sorted_terms, mid+1, end)
        elif sorted_terms[mid] > search_term:
            return self.binary_search(search_term, sorted_terms, start, mid-1)
        else:
            return mid
        


    def binary_insert(self, insert_term: str, sorted_terms: List[str]) -> List[str]:
        if len(sorted_terms) == 0:
            return [insert_term]

        index = self.binary_search(
            search_term=insert_term, 
            sorted_terms=sorted_terms,
            start=0,
            end=len(sorted_terms) - 1
        )
        
        sorted_terms.insert(index, insert_term)
        return sorted_terms

insert_term = 'Cam'
terms = ['Adam', 'Bill', 'Nick', 'Ryland', 'Zak']
new_list = Insert().binary_insert(insert_term=insert_term, sorted_terms=terms)
print(new_list)