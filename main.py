import random



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
