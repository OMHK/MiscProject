import pyinputplus as pyip
while True :
    Intro = 'Do you know how can you keep an idiot busy for eternity ? \n'
    response = pyip.inputYesNo(Intro)
    if response == 'no':
        print("Thank you my dude")
        break
