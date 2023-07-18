def ecriture (filename, text):
    f = open(filename, mode='w+')
    f.write(text)
    f.close()
ecriture('H:\justine.txt ',' je veux manger')

def lecture (filename, text):
    f = open(filename, mode='r')
    print(f.read(text))
    f.close()

