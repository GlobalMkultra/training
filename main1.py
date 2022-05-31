import random
import time


lucky_number = random.randint (1,100)
fortune_number = random.randint (1,10)
fortune_text = ''
if fortune_number == 1:
  fortune_text = 'Your work interests can capture the highest status or prestige'

if fortune_number == 2:
  fortune_text = 'Your talents will be recognized and suitably rewarded'

if fortune_number == 3:
  fortune_text = 'Your success will astonish everyone'

if fortune_number == 4:
  fortune_text = 'Your reputation is your wealth'

if fortune_number == 5:
  fortune_text = 'Your quick wits will get you out of a tough situation'

if fortune_number == 6:
  fortune_text = 'Your moods signal a period of change'

if fortune_number == 7:
  fortune_text = 'Your mind is your greatest asset'

if fortune_number == 8:
  fortune_text = 'Your mind is creative, original and alert'

if fortune_number == 9:
  fortune_text = 'Your mentality is alert, practical, and analytical'


if fortune_number == 10:
  fortune_text = 'Your loyalty is a virtue, but not when it’s wedded with blind stubbornness'  

print(f"{fortune_text}. Your Lucky Number Is:{lucky_number}")

#user_text = input (" Enter some text: ")
#upper_or_lower = input ("Enter 1 for upper or 2 for lower case: ")
#if upper_or_lower == "1":
#  print (user_text.upper())
#else:
# print (user_text.lower())
# Guessing game
guess = int(input("What is your guess? Please pick between 1 and 100.: "))
time.sleep (3)
print ("I am picking a number")
time.sleep (2)
correct_number = random.randint (1,100)
guess_count = 1
while guess != correct_number:
  time.sleep (1)
  guess_count += 1
  if guess < correct_number:
    guess = int(input("Wrong you need to guess higher. What is your guess?: "))
  else:
    guess = int(input("Wrong you need to guess lower. What is your guess?: "))
print (f"Congradulations, The correct answer was {correct_number}. It took you {guess_count}.") 
