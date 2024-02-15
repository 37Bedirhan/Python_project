def two_product_information_take():
    product1 = int(input("Birinci Ürünün Fiyatını Giriniz :\n"))
    product2 = int(input("İkinci Ürünün Fiyatını Giriniz :\n"))
    total = product1 + product2
    discount = (product1 + product2) /4
    return  total , discount

def Discounted_product_take():
    total,discount = two_product_information_take()
    if total <= 200 :
        print(f"Ödenecek Tutar {total} TL")
    elif total >= 200:
        print(f"Ödenecek Tutar {total} TL İndirimden Sonraki Tutar {discount} TL")
Discounted_product_take()