ders1={"Ali","Ayşe","Zeynep"}
ders2={"Zeynep","Mehmet","Ali"}

print(f"İki derse de girenler {ders1.intersection(ders2)}")

print(f"Yalnızca bir derse girenler {ders1.difference(ders2)}, {ders2.difference(ders1)}")

print(f"Ders 1'i alanlar {ders1}")