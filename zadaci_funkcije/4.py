def jedinstveni_elementi(lista):
    jedinstveni=[]
    for element in lista:
        if element not in jedinstveni:
            jedinstveni.append(element)
    return jedinstveni
print(jedinstveni_elementi([1, 2, 2, 3, 3, 3, 4, 5, 5]))
