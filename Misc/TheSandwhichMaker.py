import pyinputplus as pyip
bread = pyip.inputMenu(prompt= 'What type of bread do you want? (wheat, white, or sourdough)',choices=[r'wheat','white','sourdough'])
protein = pyip.inputMenu(prompt= 'What type of protein do you want? (chicken, turkey, tofu or beef)',choices=[r'chicken','turkey','tofu','beef'])
fat = pyip.inputYesNo(prompt= 'Do you want cheese?(Yes or No)')
if fat == 'Yes':
    fatype = pyip.inputMenu(prompt= 'What type of cheese do you want? (cheddar, Swiss or mozzarella)',choices=[r'cheddar','Swiss','mozzarella.'])
veggies = pyip.inputYesNo(prompt= 'Do you want veggies?(Yes or No)')
many = pyip.inputInt(prompt= 'how many do you want?',min = 1)
print(bread)
print(protein)
print(fat)
print(fatype)
print(veggies)
print(many)
print('is your order correct?')


### This code is Not yer finished
