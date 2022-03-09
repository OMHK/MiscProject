import pyinputplus as pyip
def addsuptoten(numbers):
    numberslist = list(numbers)
    for i , digit in enumerate(numberslist):
        numberslist[i] = int(digit)
    if sum(numberslist) != 10:
        raise Exception ('the digits must add up to 10, not %s.' %(sum(numberslist)))
    return int(numbers)
response = pyip.inputCustom(addsuptoten)