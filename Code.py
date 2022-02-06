 girdi = (input("Hesaplamak istediğiniz şeklin ismini girin(kare,üçgen,dikdörtgen,daire): "))

if girdi == "kare":
    z = int(input("Bir kenarın uzunluğunu girin: "))
    kare = z * z
    print("Karenizin alanı: {}".format(kare))
elif girdi == "üçgen":
    y = int(input("üçgenin yüksekliğini girin: "))
    x = int(input("tabanının boyunu girin: "))
    ucgen = (y * x)/2
    print("üçgeninizin alanı: {}".format(ucgen) )
elif girdi == "dikdörtgen":
    a = int(input("kısa kenarının boyunu girin: "))
    b = int(input("uzun kenarının boyunu girin: "))
    dikdörtgen = a * b
    print("dikdörtgeninizin alanı: {}".format(dikdörtgen))
elif girdi == "daire":
    c = int(input("yarı çapı girin: "))
    daire = (c*c)*3
    print("dairenizin alanı(pi=3): {}".format(daire))
else:
    print("Bir hata oluştu! Lütfen sorulara doğru cevap verdiğinizden emin olunuz.")
