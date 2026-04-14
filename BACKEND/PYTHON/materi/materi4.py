x = 80
y = 100
print ("x= ",x)
print ("y= ",y)

# operator penugasan += (y = y + 5)
y += 5
y += 20
print ("y: ",y)

# operator penugasan -= (y = y - 10)
y -= 10
y -= 30
print ("y: ",y)

# operator pembanding > (lebih besar), < (lebih kecil)
nilaiBudi = 80
nilaiAsep = 85
if (nilaiBudi > nilaiAsep):
    print("budi dapat roti bakar", nilaiBudi)
else:
    print("budi dapat hikmahnya", nilaiBudi)
# pusinggggg........

umur =int(input("masuk kan umur mu:"))
if umur >= 18 and umur <= 70:
    print("kamu cukup umur")
elif umur >= 7 and umur <= 15:
    print("kamu belum cukup umur")
elif umur >= 16 and umur <= 17:
    print("sedikit lagi")
elif umur >= 70 and umur <= 1000:
    print("sepertinya kamu sudah mati...")
else:
    print("kamu masih sangat kecil")


p = (input("apakah kamu wibu atau gemer? "))
if p == "wibu":
    print("sebutkan waifu mu :")
else :
    print("apa game faforit mu :")