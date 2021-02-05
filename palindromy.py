def czy_palindrom(wyraz):
    lowercase = wyraz.lower()
    if lowercase == lowercase[::-1]:
        print(f"{wyraz} to palindrom")
    else:
        print(f"{wyraz} nie jest palindromem")
czy_palindrom('palindrom')