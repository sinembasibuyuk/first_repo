# title(): Her kelimenin ilk harfini büyük yapar.
metin = "pyhton uygulamaları kursu"

metin.title()
# uppper(): Baş harfler büyük
metin.upper()

# lower():
print(metin.lower())

# capitalize():
print(metin.capitalize())

# startswith
metin = "python uygulamaları kursu"
metin.startswith("ptyhon")

# find()
metin = "python uygulamaları kursu"
metin.find("t")

metin.find("uygulamaları")
metin.find("thon")
metin.find("P") # -1 döndürür.

# replace()
metin = "python uygulamaları kursu"

# count(): belirtilen substringin kaç defa geçtiğini döndürür
e_mail = "salim@gmail.com, ensari@gmail.com, yeter@gmail.com"
e_mail.count("mail.com")

# swapcase() büyükleri küçük küçükleri büyük çevir
metin = "BilgeAdam"
metin.swapcase()

# join()
isim_listesi = ["Ali", "Veli", "Emel"]
" & ".join(isim_listesi)

# string methods demo
website = "http://www.bilgeadam.com"
website[11:20]
website.split(".") [1]

metin = "Python kursu"
#Python ifadesini Java ile değiştirir
metin.replace("Python", "Java")