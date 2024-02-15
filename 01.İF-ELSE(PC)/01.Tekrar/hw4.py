
product= int(input("1.Ürünün fiyatini giriniz :"))
pruduct2= int(input("2.Ürünün fiyatini giriniz :"))
product_total= (product + pruduct2)

if product_total <= 200:
    addproduct= 200 - product_total
    print("Ödenecek miktar",addproduct )
else:
    discount= product_total-(product_total/4) 
    product_total= product_total - discount
    print("İndirim miktari", discount)
    print("Ödenecek tutar", product_total)
