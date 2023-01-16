import re
from collections import Counter

s = "{{4,2,3},{3},{2,3,4,1},{2,3}}"

s = Counter(re.findall('\d+', s))

print(s)

