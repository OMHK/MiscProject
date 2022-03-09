while True:
    print('please enter your age:')
    age = input()
    try:
        age = int(age)
    except:
        print('Please enter positive numeric digits only')
        continue
    if age < 0 :
        print('Please enter a positive number')
        continue
    break
print(f'Your age is: {age}.')