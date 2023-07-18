import sys

for line in sys.stdin:
    # supprimer les espace
    line = line.strip()
    words = line.strip()

for word in words:
    print("%s\t%d") % (word, 1)