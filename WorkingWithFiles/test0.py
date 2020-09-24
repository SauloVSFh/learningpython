with open("testin.txt",'w+') as fw:
    for i in range(10):
        fw.write("This is line %d\n\n" % (i+1))
