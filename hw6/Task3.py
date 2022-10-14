def slovar (*names):
    res = {}
    for i in names:
        key=i[0].capitalize()
        if key not in res:
            res[key]=[]
        res[key].append(i)
    return res
print (slovar("Tata", "Nata", "Kata", "Zlata"))
