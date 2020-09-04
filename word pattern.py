#Yingxuan Wang
#word pattern

def word_pattern(pattern, str):
    #input validation
    if len(str)==0:
        raise ValueError("Your string cannot be empty. Please try again.")
    
    #try to store all inputs into dictionaries for further use
    checked_dic = {}
    matched_dic = {}
    str = str.split(" ")
    
    #if the length pattern does not match the size of words
    if len(pattern)!=len(str):
        return False
    
    for i in range(len(pattern)):
        #match the pattern with a specified word and let it be fixed
        #eg. pattern = 'abc', str = 'dog cat wolf'
        #->'a' must be 'dog', 'b' must be cat and 'c' must be 'wolf'
        #here, a bijection relation is formed
        
        #situation1: we have already seen the word, but it is not matched with its specified pattern
        if pattern[i] not in matched_dic and str[i] in checked_dic:
            return False
        #situation2: we have already seen the pattern, but the word assigned to it is incorrect
        elif pattern[i] in matched_dic and str[i] != matched_dic[pattern[i]]:
            return False
        else:
            matched_dic[pattern[i]] = str[i]
            checked_dic[str[i]]="checked"
            
    return True