def solution(grid):
    answer = []
    table = []
    for i in range(len(grid)+2):
        table.append(list())
        for n in range(len(grid[0])+2):
            if (i==0 and n==0) or (i==0 and n==(len(grid[0])+1)) or (i==(len(grid[0])+1) and n==0) or (i==(len(grid[0])+1) and n==(len(grid[0])+1)):
                table[i].append('P')
            else:
                table[i].append('')
    print(table)
    
    for i, n in enumerate(grid):
        for u, p in enumerate(n):
            table[i+1][u+1] = p
            
    print(table)
    print('' in table[0])
    while 1:
        table_n = table.copy()
        for i, n in enumerate(table_n):
            for u, p in enumerate(n):
                if p != 'P' and p != 'S' and p != 'L' and p != 'R':
                    
    def cal_route(table):
        for i, n in enumerate(table_n):
            for u, p in enumerate(n):
                if p != 'P':
                    while 1:
                                          
                
    
    return answer

grid = ["SL","LR"]
print(solution(grid))