import sys

class Solution:
    """_summary_
        Merge three sorted lists into one sorted list.
        Uses 3 pointers to each list.
        Find smallest value between the 3 pointers, add to list (if not already in list)
        Move pointer with that added value, by comparing it against the values
    """
    def merge_three_sorted_lists(self, l1, l2, l3):
        merged = []
        i, j, k = 0, 0, 0
        valA, valB, valC = 0, 0, 0
        
        if (i <= len(l1)):
            valA = sys.maxsize
        else:
            valA = l1[i]
            
        if (j <= len(l2)):
            valB = sys.maxsize
        else:
            valB = l2[j]

        if (j <= len(l3)):
            valC = sys.maxsize
        else:
            valC = l3[k]

        smallest = min(valA, valB, valC)
        if (smallest not in merged):
            merged.append(smallest)
        
        if (smallest == valA):
            i += 1
        elif (smallest == valB):
            j += 1
        else:
            k += 1
        
        return merged