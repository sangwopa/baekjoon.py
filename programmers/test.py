tmp1 = '06:00'

tmp2 = '07:30'


con = (int(tmp2[:2])*60 + int(tmp2[-2:])) - (int(tmp1[:2])*60 + int(tmp1[-2:]))

print(con)