### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    # For a conditional, you need == for an if statement.
    if card.value = 1:
      return True
    # missing :
    else
      return False
   
  # typo on dif, should be def and missing comma, after card1
  dif highest_card(self, card1 card2):
  # missing indent here, and on further lines
  if card1.value > card2.value:
    # there is no card, it must be card1
    return card
  else:
    return card2
  

# missing indent for whole section
def cards_total(self, cards):
  # total needs a value, I think it should be = 0
  total
  for card in cards:
    total += card.value
    # return should be outside the for loop
    return "You have a total of" + total
  
```
