s=['a','e','i','o','u','A','E','I','O','U']
alp=input()
if alp.isalpha():
    if alp in s:
        print('Vowel')
    else:
        print('Consonant')
else:
    print('invalid')

