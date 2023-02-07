import time

def return_abc():
  alphabets = []
  for ch in "ABC":
    time.sleep(1)
    alphabets.append(ch)
  return alphabets

for ch in return_abc():
  print(ch)
  
def yield_abc():
    for ch in "ABC":
        time.sleep(1)
        yield ch
    
for ch in yield_abc():
  print(ch)