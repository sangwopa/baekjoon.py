div = list(map(int, input().split()))

# 확률 계산의 위해 100으로 나눠줌
for i in range(len(div)):
    div[i] /= 100

# 각각의 경우에 대해 확률 계산
win_0 = div[0]*(div[13]*div[1]+(1-div[13])*div[2])*(div[22]*div[27]*div[23]*div[3]+div[22]*div[27]*(1-div[23])*div[5]
                                                    +div[22]*(1-div[27])*div[24]*div[3]+div[22]*(1-div[27])*(1-div[24])*div[6]
                                                   +(1-div[22])*div[27]*div[25]*div[4]+(1-div[22])*div[27]*(1-div[25])*div[5]
                                                   +(1-div[22])*(1-div[27])*div[26]*div[4]+(1-div[22])*(1-div[27])*(1-div[26])*div[6])
win_1 = (1-div[0])*(div[13]*div[7]+(1-div[13])*div[8])*(div[22]*div[27]*div[23]*div[9]+div[22]*div[27]*(1-div[23])*div[11]
                                                    +div[22]*(1-div[27])*div[24]*div[9]+div[22]*(1-div[27])*(1-div[24])*div[12]
                                                   +(1-div[22])*div[27]*div[25]*div[10]+(1-div[22])*div[27]*(1-div[25])*div[11]
                                                   +(1-div[22])*(1-div[27])*div[26]*div[10]+(1-div[22])*(1-div[27])*(1-div[26])*div[12])
win_2 = div[13]*(div[0]*(1-div[1])+(1-div[0])*(1-div[7]))*(div[22]*div[27]*div[23]*div[14]+div[22]*div[27]*(1-div[23])*div[16]
                                                    +div[22]*(1-div[27])*div[24]*div[14]+div[22]*(1-div[27])*(1-div[24])*div[17]
                                                   +(1-div[22])*div[27]*div[25]*div[15]+(1-div[22])*div[27]*(1-div[25])*div[16]
                                                   +(1-div[22])*(1-div[27])*div[26]*div[15]+(1-div[22])*(1-div[27])*(1-div[26])*div[17])
win_3 = (1-div[13])*(div[0]*(1-div[2])+(1-div[0])*(1-div[8]))*(div[22]*div[27]*div[23]*div[18]+div[22]*div[27]*(1-div[23])*div[20]
                                                    +div[22]*(1-div[27])*div[24]*div[18]+div[22]*(1-div[27])*(1-div[24])*div[21]
                                                   +(1-div[22])*div[27]*div[25]*div[19]+(1-div[22])*div[27]*(1-div[25])*div[20]
                                                   +(1-div[22])*(1-div[27])*div[26]*div[19]+(1-div[22])*(1-div[27])*(1-div[26])*div[21])
win_4 = div[22]*(div[27]*div[23]+(1-div[27])*div[24])*(div[0]*div[13]*div[1]*(1-div[3])+div[0]*div[13]*(1-div[1])*(1-div[14])
                                                    +div[0]*(1-div[13])*div[2]*(1-div[3])+div[0]*(1-div[13])*(1-div[2])*(1-div[18])
                                                   +(1-div[0])*div[13]*div[7]*(1-div[9])+(1-div[0])*div[13]*(1-div[7])*(1-div[14])
                                                   +(1-div[0])*(1-div[13])*div[8]*(1-div[9])+(1-div[0])*(1-div[13])*(1-div[8])*(1-div[18]))
win_5 = (1-div[22])*(div[27]*div[25]+(1-div[27])*div[26])*(div[0]*div[13]*div[1]*(1-div[4])+div[0]*div[13]*(1-div[1])*(1-div[15])
                                                    +div[0]*(1-div[13])*div[2]*(1-div[4])+div[0]*(1-div[13])*(1-div[2])*(1-div[19])
                                                   +(1-div[0])*div[13]*div[7]*(1-div[10])+(1-div[0])*div[13]*(1-div[7])*(1-div[15])
                                                   +(1-div[0])*(1-div[13])*div[8]*(1-div[10])+(1-div[0])*(1-div[13])*(1-div[8])*(1-div[19]))
win_6 = div[27]*(div[22]*(1-div[23])+(1-div[22])*(1-div[25]))*(div[0]*div[13]*div[1]*(1-div[5])+div[0]*div[13]*(1-div[1])*(1-div[16])
                                                    +div[0]*(1-div[13])*div[2]*(1-div[5])+div[0]*(1-div[13])*(1-div[2])*(1-div[20])
                                                   +(1-div[0])*div[13]*div[7]*(1-div[11])+(1-div[0])*div[13]*(1-div[7])*(1-div[16])
                                                   +(1-div[0])*(1-div[13])*div[8]*(1-div[11])+(1-div[0])*(1-div[13])*(1-div[8])*(1-div[20]))
win_7 = (1-div[27])*(div[22]*(1-div[24])+(1-div[22])*(1-div[26]))*(div[0]*div[13]*div[1]*(1-div[6])+div[0]*div[13]*(1-div[1])*(1-div[17])
                                                    +div[0]*(1-div[13])*div[2]*(1-div[6])+div[0]*(1-div[13])*(1-div[2])*(1-div[21])
                                                   +(1-div[0])*div[13]*div[7]*(1-div[12])+(1-div[0])*div[13]*(1-div[7])*(1-div[17])
                                                   +(1-div[0])*(1-div[13])*div[8]*(1-div[12])+(1-div[0])*(1-div[13])*(1-div[8])*(1-div[21]))

print(win_0, win_1, win_2, win_3, win_4, win_5, win_6, win_7)
