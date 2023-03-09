str1 = 'oicarovoce'
str2 = 'oi*voce'
string1 = ''
string2 = ''

for i in range(len(str2) -1):
    string1 += str2[i]
    if str2[i] == '*':
        string2 += str2[i + 1]
      
print(string1)
print(string2)
    