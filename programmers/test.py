def get_cantor(n):
    cantor = ['1']
    
    for i in range(0, n):
        tmp = []
        for n in range(len(cantor)):
            if cantor[n] == '0':
                tmp.extend(['0', '0', '0', '0', '0'])
            else:
                tmp.extend(['1', '1', '0', '1', '1'])
        
        cantor = tmp.copy()      
    
    return ''.join(cantor)
    
print(get_cantor(0))
print(get_cantor(1))
print(get_cantor(2))
print(get_cantor(3))
print(get_cantor(4))
        

    
    
        

        
    