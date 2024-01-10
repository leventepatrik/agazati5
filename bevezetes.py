def feladat1():
    auto_neve:str=input("Ad meg az autó nevét:")
    gyartasi_datum:int=int(input("Ad meg az gyártási dátumát:"))
    print(f"\tAz auto neve: {auto_neve}")
    print(f"\t Az auto gyártási datuma: {gyartasi_datum}")
    if gyartasi_datum <2000:
        print(f"\tEz a(z) {auto_neve} öreg auto")
    elif gyartasi_datum ==2024:
        print(f"\tEz a(z) {auto_neve} friss autó")
    else:
        print(f"\tEz a(z) {auto_neve} átlagos koru")
            
