#A PYTHON PROGRAMM FOR ELIGIBILITY TO START A CAR

age= int(input('how old are you?: '))
licensed = str(input('enter Y or N: '))
if age >= 18:
    if licensed == 'Y':
        print('you can drive now')
    else:
        print("you are not allowed to drive")
print('safe trip man') 