def substring(str1,str2):
    status = False
    for i in range(len(str2)):
        if str1[i] == str2[i]:
            status = True
    return status 

print(substring('casorio','casa'))