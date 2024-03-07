import math

def toplama(x, y):
    return x + y

def cikarma(x, y):
    return x - y

def carpma(x, y):
    return x * y

def bolme(x, y):
    if y == 0:
        return "Sıfıra bölme hatası!"
    else:
        return x / y

def us_alma(x, y):
    return x ** y

def karekok(x):
    return math.sqrt(x)

def logaritma(x, taban=math.e):
    if x <= 0:
        return "Pozitif sayılar için logaritma hesaplanabilir."
    else:
        return math.log(x, taban)

def trigonometrik_fonksiyon(islem, x):
    if islem == "sin":
        return math.sin(math.radians(x))
    elif islem == "cos":
        return math.cos(math.radians(x))
    elif islem == "tan":
        return math.tan(math.radians(x))
    else:
        return "Geçersiz işlem."

# Kullanıcı arayüzü
def hesap_makinesi():
    print("Basit Python Hesap Makinesi")
    while True:
        print("\nİşlemler:\n1.Toplama\n2.Çıkarma\n3.Çarpma\n4.Bölme\n5.Üs Alma\n6.Karekök\n7.Logaritma\n8.Trigonometrik Fonksiyonlar\n9.Çıkış")
        secim = input("Yapmak istediğiniz işlemi seçin (1-9): ")

        if secim == '9':
            print("Hesap makinesinden çıkılıyor.")
            break

        num1 = float(input("Birinci sayıyı girin (Trigonometrik işlemler ve karekök için geçerli değil): ")) if secim not in ['6', '8'] else 0
        num2 = float(input("İkinci sayıyı girin: ")) if secim in ['1', '2', '3', '4', '5', '7'] else 0

        if secim == '1':
            print("Sonuç: ", toplama(num1, num2))
        elif secim == '2':
            print("Sonuç: ", cikarma(num1, num2))
        elif secim == '3':
            print("Sonuç: ", carpma(num1, num2))
        elif secim == '4':
            print("Sonuç: ", bolme(num1, num2))
        elif secim == '5':
            print("Sonuç: ", us_alma(num1, num2))
        elif secim == '6':
            x = float(input("Sayıyı girin: "))
            print("Sonuç: ", karekok(x))
        elif secim == '7':
            taban = input("Logaritma tabanını girin (e için boş bırakın): ")
            if taban == '':
                print("Sonuç: ", logaritma(num1))
            else:
                print("Sonuç: ", logaritma(num1, float(taban)))
        elif secim == '8':
            islem = input("Trigonometrik işlemi girin (sin, cos, tan): ")
            aci = float(input("Açıyı girin (derece): "))
            print("Sonuç: ", trigonometrik_fonksiyon(islem, aci))
        else:
            print("Geçersiz seçim.")

if __name__ == "__main__":
    hesap_makinesi()
