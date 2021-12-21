def solution(s):
    # 언어에 해당하는 숫자
    my_number = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8","nine":"9"}
    answer = ""
    str_num = ""
    for i in s: #조건에 따라 answer에 저장
        str_num = str_num + i
        if str_num == "zero" or str_num == "0":
            answer  = answer + my_number["zero"]
            str_num = ""
        elif str_num == "one" or str_num == "1":
            answer  = answer + my_number["one"]
            str_num = ""
        elif str_num == "two" or str_num == "2":
            answer  = answer + my_number["two"]
            str_num = ""
        elif str_num == "three" or str_num == "3":
            answer  = answer + my_number["three"]
            str_num = ""
        elif str_num == "four" or str_num == "4":
            answer  = answer + my_number["four"]
            str_num = ""
        elif str_num == "five" or str_num == "5":
            answer  = answer + my_number["five"]
            str_num = ""
        elif str_num == "six" or str_num == "6":
            answer  = answer + my_number["six"]
            str_num = ""
        elif str_num == "seven" or str_num == "7":
            answer  = answer + my_number["seven"]
            str_num = ""
        elif str_num == "eight" or str_num == "8":
            answer  = answer + my_number["eight"]
            str_num = ""
        elif str_num == "nine" or str_num == "9":
            answer  = answer + my_number["nine"]
            str_num = ""
        else:
            continue
    return int(answer)