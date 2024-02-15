onemli_telefonlar = ["Acil Çağri Merkezi:112" , "Polis İmdat:155" , "Milli Eğitim Bakanliği İletişim Merkezi:444 0 632"] 
önemli_bilgiler = onemli_telefonlar.copy()
new_önemli_bilgiler = onemli_telefonlar.copy()

print (önemli_bilgiler)
önemli_bilgiler.clear()

print(önemli_bilgiler)
new_önemli_bilgiler.remove("Acil Çağri Merkezi:112")

print (new_önemli_bilgiler)
say= new_önemli_bilgiler.count("Sağlik bakanliği") 
print(say)

new_önemli_bilgiler.clear()
print(new_önemli_bilgiler)