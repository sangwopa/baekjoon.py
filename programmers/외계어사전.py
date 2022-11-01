def val_str(spell, word):
    for i in spell:
        if i in word:
            word = word.replace(i, '', 1)
        else:
            return False
        if i in word:
            return False
    return True

def solution(spell, dic):    
    for i in dic:
        if val_str(spell, i):
            return 1  
    return 2

spell = ["p", "o", "s"]
dic = ["sod", "eocd", "qixm", "adio", "soo"]
print(solution(spell, dic))

spell = ["z", "d", "x"]
dic = ["def", "dww", "dzx", "loveaw"]
print(solution(spell, dic))

spell = ["s", "o", "m", "d"]
dic = ["moos", "dzx", "smm", "sunmmo", "som"]	
print(solution(spell, dic))