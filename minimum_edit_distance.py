"""
Calculates the minimum edit distance between two strings. 
In other words, minimum number of operations to convert a to b.
Also known as the Levenshtein algorithm.
Arguments:
1. a: string
2. b: string
3. cost: (cost of making an edit) int {default 1}
"""


from memoize import memoize

@memoize
def minimum_edit_distance(a, b, cost_insert_delete=1, cost_substitution=2):
    if(not all(isinstance(arg, str) for arg in [a, b])):
        raise Exception("Please pass strings!")
    if(len(a) == 0):
        return(len(b))
    elif(len(b) == 0):
        return(len(a))
    else:
        return(
            min(
                minimum_edit_distance(a[1:], b, cost_insert_delete) + cost_insert_delete,
                minimum_edit_distance(a, b[1:], cost_insert_delete) + cost_insert_delete,
                minimum_edit_distance(a[1:], b[1:], cost_insert_delete) + (
                    lambda x, y, cost: 0 if x[0] == y[0] else cost)(a, b, cost_substitution
                )
            )
        )
