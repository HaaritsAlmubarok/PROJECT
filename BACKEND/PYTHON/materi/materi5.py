# imput () menerima imputan dari user
# if - elif - else (kondisional)
# operator pembanding == (sama dengan nilai)
RumahDoni = input ("rumah mu di mana doni?")
print("doni rumahnya di", RumahDoni)

if (RumahDoni == "3 A"):
    print("berarti rumah mu dekar rumah pak RT")
elif (RumahDoni == "7 C"):
    print("berarti rumah mu dekat sawah" )
elif (RumahDoni == "9 b"):
    print("berarti rumah mu dekat masjid")
else:  
    print("apakah rumah mu dekat lapangan?")