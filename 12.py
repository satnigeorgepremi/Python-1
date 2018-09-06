a = input('Enter any number : ')
if(a == str(a)[::-1]):
      print('The given number is PALINDROME')
elif(a<=1000 ):
      print('The given number is NOT in 1000')
else:
      print('The given number is NOT a palindrome')