with open('gg.txt') as datfile:
    text = datfile.read()
print(sum(map(int, text.split(None, 2)[:2])))
