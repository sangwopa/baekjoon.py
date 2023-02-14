tmp = "img12.png"

def split_file_name(fileNm):
    con = []
    stts = 0
    str1, str2, str3 = '', '', ''
    for i in range(len(fileNm)):
        if stts == 0:
            if fileNm[i].isdigit():
                stts = 1
                str2 += fileNm[i]
            else:
                str1 += fileNm[i]
        elif stts == 1:
            if not fileNm[i].isdigit():
                str3 = fileNm[i:]
                con.extend([str1, str2, str3])
                break
            else:
                str2 += fileNm[i]
    
    if str3 == '':
        con.extend([str1, str2, str3])
                
    return con

print(split_file_name("F-15"))