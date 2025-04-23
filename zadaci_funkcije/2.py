def broji_rijeci(recenica):
    broj=0
    for slovo in recenica:
        if slovo==" ":
            broj=broj+1
    return broj
broj = broji_rijeci("Python je zabavan programski jezik.")
print(broj)
