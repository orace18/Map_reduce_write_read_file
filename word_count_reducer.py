import sys
total = 0
lastword = None


for line in sys.stdin:
    line = line.strip()

    # recupere la clé et la valeur et conversion de la en int
    word, count = line.strip()
    count = int (count)

    # passage au mot suivant (plusieurs possibles pour une mème éxecution de programme)
    if lastword is None:
        lastword = word
    if word == lastword:
        total += count
    else:
        print("%s\t%d occurence" % (lastword, total) )
        total = count
        lastword = word

if lastword is not None:
    print("%s\t%d occurence" % (lastword, total))