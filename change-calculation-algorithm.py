paralar = [200,100,50,20,10,5,1,0.5]
sozluk = {200:0 , 100:0, 50:0, 20:0 , 10:0 , 5:0 , 1:0 , 0.5:0 , 0.25:0 , 0.05:0}
def Para_Ustu(para_ustu):
    index = 0
    string = ""
    while para_ustu > 0:
        if paralar[index] > para_ustu:
            index += 1
            continue
        para_ustu -= paralar[index]
        sozluk[paralar[index]] += 1
    for x,y in sozluk.items():
        if y != 0:
            string += f"{y} tane {x}lik var\n"
    return string
print(Para_Ustu(89.5))
