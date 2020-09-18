#Problem here 

with open ("vocabulary.txt",'r') as str1:
    file = list(str1)
    for line in file:
        x = file.find("–")
        y = file[0:(x-1)]
        with open ("vocabulary2.txt",'w+') as string2:
            string2.write(y)
