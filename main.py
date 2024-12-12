# 4 -oy 6 dars
# homewroks
from collections import namedtuple

# 1: Talabalar ro'yxati
Talaba = namedtuple('Talaba', ['name', 'age', 'major'])
talabalar = [
    Talaba('Ali', 20, 'Computer Science'),
    Talaba('Laylo', 21, 'Law'),
    Talaba('Olim', 19, 'Mathematics')
]
for talaba in talabalar:
    print(talaba)

# 2: Mahsulotlar
Mahsulot = namedtuple('Mahsulot', ['product_name', 'price', 'quantity'])
mahsulotlar = [
    Mahsulot('Olma', 5000, 10),
    Mahsulot('Banana', 6000, 15),
    Mahsulot('Kivi', 8000, 8)
]
for mahsulot in mahsulotlar:
    print(f"Mahsulot: {mahsulot.product_name}, Narxi: {mahsulot.price}, Miqdori: {mahsulot.quantity}")

# 3: Shaharlar
Shahar = namedtuple('Shahar', ['city_name', 'country', 'population'])
shaharlar = [
    Shahar('Toshkent', 'Uzbekistan', 2700000),
    Shahar('New York', 'USA', 8419000),
    Shahar('Tokyo', 'Japan', 13929286)
]
eng_katta_shahar = max(shaharlar, key=lambda s: s.population)
print(f"Eng katta shahar: {eng_katta_shahar.city_name}, Aholisi: {eng_katta_shahar.population}")

# 4: Avtomobillar
Avtomobil = namedtuple('Avtomobil', ['make', 'model', 'year'])
avtomobillar = [
    Avtomobil('Toyota', 'Camry', 2020),
    Avtomobil('BMW', 'X5', 2023),
    Avtomobil('Audi', 'A6', 2022)
]
eng_yangi_avto = max(avtomobillar, key=lambda a: a.year)
print(f"Eng yangi avtomobil: {eng_yangi_avto.make} {eng_yangi_avto.model}, Yili: {eng_yangi_avto.year}")

# 5: Oddiy closure
def oddiy_closure():
    def ichki_funksiya():
        return "Oddiy closure ishladi!"
    return ichki_funksiya
closure1 = oddiy_closure()
print(closure1())

# 6: Salomlashish funksiyasi
def salomlashish():
    def salom_ber(ism):
        return f"Salom, {ism}!"
    return salom_ber
salom_funksiya = salomlashish()
print(salom_funksiya("Ali"))

# 7: Qo'shuvchi funksiya
def qoshuvchi(son1):
    def qosh(son2):
     return son1 + son2
    return qosh
qosh = qoshuvchi(10)
print(qosh(5))

# 8: Counter funksiyasi
def counter():
    count = 0
    def ichki_counter():
        nonlocal count
        count += 1
        return count
    return ichki_counter
count_fun = counter()
print(count_fun())
print(count_fun())

# 9: Kvadrat hisoblash
def kvadrat_hisobla():
    def hisobla(son):
        return son ** 2
    return hisobla
kvadrat_fun = kvadrat_hisobla()
print(kvadrat_fun(6))

# 10: Ismlar ro'yxati
def ismlar_royxati():
    royxat = []
    def qosh_ism(ism):
        royxat.append(ism)
        return royxat
    return qosh_ism
ismlar_fun = ismlar_royxati()
print(ismlar_fun("Ali"))
print(ismlar_fun("Laylo"))

# 11: Doimiy chegirma
def chegirma(foiz):
    def narxni_chegirma(narx):
        return narx - (narx * foiz / 100)
    return narxni_chegirma
chegirma_fun = chegirma(10)
print(chegirma_fun(10000))

# 12: Mahsulotlarni ko'paytiruvchi funksiya
def kopaytiruvchi():
    natija = 1
    def kopaytir(son):
        nonlocal natija
        natija *= son
        return natija
    return kopaytir
kopaytir_fun = kopaytiruvchi()
print(kopaytir_fun(2))
print(kopaytir_fun(3))

# 13: String qatoriga qo'shish
def qatorni_qosh():
    matn = ""
    def qosh(qator):
        nonlocal matn
        matn += qator
        return matn
    return qosh
qosh_fun = qatorni_qosh()
print(qosh_fun("Salom "))
print(qosh_fun("Dunyo!"))

# 14: Sonlarni filtrlash
def toq_sonlarni_filtrlash():
    def filtrlash(sonlar):
        return [son for son in sonlar if son % 2 != 0]
    return filtrlash
filtr_fun = toq_sonlarni_filtrlash()
print(filtr_fun([1, 2, 3, 4, 5, 6, 7]))

# 15: Exponent funksiyasi
def exponent(daraja):
    def hisobla(asos):
        return asos ** daraja
    return hisobla
kvadrat = exponent(2)
print(kvadrat(4))

# 16: Stringni teskari o'girish
def teskari_qil():
    def teskari(matn):
        return matn[::-1]
    return teskari
teskari_fun = teskari_qil()
print(teskari_fun("Python"))

# 17: Do'kon savati
def savat():
    mahsulotlar = []
    def savatga_qosh(mahsulot, narx):
        mahsulotlar.append((mahsulot, narx))
        return sum(narx for _, narx in mahsulotlar)
    return savatga_qosh
savat_fun = savat()
print(savat_fun("Olma", 5000))
print(savat_fun("Banana", 6000))

# 18: Mahsulot narxlari
def narxlar_royxati():
    narxlar = []
    def qosh_narx(narx):
        narxlar.append(narx)
        return narxlar
    return qosh_narx
narx_fun = narxlar_royxati()
print(narx_fun(10000))
print(narx_fun(15000))
