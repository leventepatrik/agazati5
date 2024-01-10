import random
def feladat2():
    lista=[]
    print(f"\t",end="")
    for i in range(0,5,1):
        szam=random.randint(-10,100)
        lista.append(str(szam))
        if i < 4:
            print(lista[i],end=";")
        else:
            print(lista[i],end=" ")   
    return lista     


def egyjegyuek(lista):
    szamlalo=0
    for i in range (0,len(lista),1):
        if lista[i] > 0 and lista[i]<10:
            szamlalo+=1
        i+=1
        print(f"Az egyjegyüek száma:")    
    return szamlalo        
             