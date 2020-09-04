#Yingxuan Wang
#Binary search tree

def BST(n):
    #if n = 0 or n = 1, we know that the result is 1
    if n == 0 or n == 1:
        return 1
    #if n = 2, we have two possibilities of drawing trees
    # 1         2
    #  \       /
    #   2     1
    if n == 2:
        return 2
    #we need to pick one "i" from 1, 2, ..., n to be our root
    #numbers less than i should be in the left subtrees
    #namely, from 1 to i
    #numbers larger than i should be in the right subtrees
    #namely, from i+1 to n
    #the sum of combinations of left subtrees and right subtrees is the result
    #Cuz' I'm not sure about how to write a recurrent func, I'll just leave my thoughts here
    
    count = 0
    for i in range (1, n+1):
        count += BST(i-1) * BST(n-i)
    return count
        