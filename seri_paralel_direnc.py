# Seri-Paralel Direnç Hesaplayıcı


def seri_direnc(direnc_listesi):
    return sum(direnc_listesi)

def paralel_direnc(direnc_listesi):
    return 1 / sum(1/r for r in direnc_listesi)

print("Seri-Paralel Direnç Hesaplama Programı")
print("-------------------------------------")

while True:
    secim = input("\nSeri için 's', Paralel için 'p', Çıkış için 'q' giriniz: ").lower()
    
    if secim == 'q':
        print("Program sonlandırıldı.")
        break
    
    elif secim in ['s', 'p']:
        degerler = input("Direnç değerlerini ohm cinsinden aralarına boşluk koyarak giriniz: ")
        direncler = [float(x) for x in degerler.split()]
        
        if secim == 's':
            Rt = seri_direnc(direncler)
            print(f"Seri bağlı dirençlerin eşdeğer direnci: {Rt:.2f} Ω")
        else:
            Rt = paralel_direnc(direncler)
            print(f"Paralel bağlı dirençlerin eşdeğer direnci: {Rt:.2f} Ω")
    else:
        print("Hatalı seçim yaptınız. Tekrar deneyin.")
    