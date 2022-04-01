num=int(input(' Please Enter Your Mark: \n'))
if num<=100 and num>=70:
    print(' You are a Genious and You got A grade!')
elif num<69 and num>60:
    print('You got B grade')
elif num < 59 and num > 50:
    print('You got C grade')
elif num < 49 and num > 40:
    print('You got D grade')
elif num<0:
    print('Invalid Option!')

else :
    print('Sorry! You have a Supplimentary')