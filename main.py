import time
import random
import threading 

def RANDOMq():

  symbol = random.choice(['+','-','/','x'])
  if symbol == '+':
    num1 = random.randint(0,99)
    num2 = random.randint(1,99)
    ans = num1 + num2
  elif symbol == '-':
    num1 = random.randint(1,99)
    num2 = random.randint(1,num1)
    ans = num1 - num2
  elif symbol == '/':
    num2 = random.randint(1,12)
    num1 = num2 * random.randint(1,12)
    ans = num1 / num2
  else:
    num1 = random.randint(1,12)
    num2 = random.randint(1,12)
    ans = num1 * num2

  print(f"{num1} {symbol} {num2} = ", end = "")
  return str(int(ans))


def timer():
  global sec
  sec = 40
  while sec > 0:
    time.sleep(1)
    sec = sec - 1

numQuestions = 0
numRight = 0

timerThread = threading.Thread(target = timer)
timerThread.start()

while sec > 0:

  q = RANDOMq()
  a = input("")
  
  if q == a:
    print("Correct")
    numRight = numRight + 1
    
  else:
    print("Incorrect")
  print()

  numQuestions = numQuestions + 1

print("GAME OVER")
print(f"You got {numRight} right with an accuracy of {round(numRight / numQuestions * 100, 2)} %")