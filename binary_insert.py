from typing import List

class Insert():
    def passive_binary_search(self, search_term: str, sorted_terms: List[str]):
        # terminates at where low and high match
        low = 0
        high = len(sorted_terms) - 1
        mid = (low + high) // 2

        while low <= high:
            compare_term = sorted_terms[mid]

            if search_term == compare_term:
                return mid 
            elif search_term < compare_term:
                high = mid - 1
                mid = (low + high) // 2
            elif search_term > compare_term:
                low = mid + 1
                mid = (low + high) // 2        

        return mid # Can be lower or higher

    def binary_insert(self, insert_term: str, sorted_terms: List[str]) -> List[str]:
        if len(sorted_terms) == 0:
            return [insert_term]

        area_to_insert = self.passive_binary_search(
            search_term=insert_term, 
            sorted_terms=sorted_terms
        )
        print(area_to_insert)
        print(insert_term, sorted_terms[area_to_insert])
        if insert_term < sorted_terms[area_to_insert]:
            sorted_terms.insert(area_to_insert, insert_term)
        else:
            sorted_terms.insert(area_to_insert + 1, insert_term)
        
        return sorted_terms

insert_term = 'Aaron'
terms = ['Adam', 'Bill', 'Nick', 'Ryland', 'Zak']
new_list = Insert().binary_insert(insert_term=insert_term, sorted_terms=terms)
print(new_list)