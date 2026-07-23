from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

kamp_programi = {
    1: {"tarih": "17 Ağustos", "ders": "Matematik", "konu": "Temel Kavramlar ve Sayı Kümeleri", "detay": "Pozitif-negatif sayılar, tek-çift sayılar ve temel kurallar."},
    2: {"tarih": "18 Ağustos", "ders": "Türkçe", "konu": "Sözcükte ve Söz Öbeklerinde Anlam", "detay": "Anlam bilimi ve paragrafın şifreleri giriş."},
    3: {"tarih": "19 Ağustos", "ders": "Matematik", "konu": "Bölme ve Bölünebilme Kuralları", "detay": "Asal çarpanlar, EBOB - EKOK."},
    4: {"tarih": "20 Ağustos", "ders": "Geometri", "konu": "Üçgende Açılar", "detay": "Temel açı özellikleri ve üçgende açılar soru çözümü."},
    5: {"tarih": "21 Ağustos", "ders": "Fen (Fizik)", "konu": "Fizik Bilimine Giriş", "detay": "Fiziksel nicelikler, temel ve türetilmiş büyüklükler."},
    6: {"tarih": "22 Ağustos", "ders": "Matematik", "konu": "Rasyonel ve Ondalık Sayılar", "detay": "İşlem yeteneği ve ÖSYM tarzı kesir problemleri."},
    7: {"tarih": "23 Ağustos", "ders": "İzin Günü", "konu": "Dinlenme ve Haftalık Tekrar", "detay": "Aküleri şarj etme molası, eksik kalan soruların gözden geçirilmesi."},
    8: {"tarih": "24 Ağustos", "ders": "Türkçe", "konu": "Cümlede Anlam", "detay": "Cümle yorumlama, çıkarım yapma ve paragraf denemesi."},
    9: {"tarih": "25 Ağustos", "ders": "Matematik", "konu": "Birinci Dereceden Denklemler ve Eşitsizlikler", "detay": "Bilinmeyenli denklemler ve çözüm kümeleri."},
    10: {"tarih": "26 Ağustos", "ders": "Geometri", "konu": "Özel Üçgenler", "detay": "Dik üçgen, ikizkenar ve eşkenar üçgen özellikleri."},
    11: {"tarih": "27 Ağustos", "ders": "Fen (Kimya)", "konu": "Kimya Bilimi", "detay": "Simyadan kimyaya, kimya disiplinleri ve güvenlik kuralları."},
    12: {"tarih": "28 Ağustos", "ders": "Matematik", "konu": "Mutlak Değer", "detay": "Mutlak değerli denklemler ve özellikler."},
    13: {"tarih": "29 Ağustos", "ders": "Türkçe", "konu": "Paragrafın Yapısı", "detay": "Akışı bozan cümle, paragrafı ikiye bölme."},
    14: {"tarih": "30 Ağustos", "ders": "İzin Günü", "konu": "Dinlenme / Zafer Bayramı", "detay": "Haftalık dinlenme ve zihinsel rahatlama."},
    15: {"tarih": "31 Ağustos", "ders": "Matematik", "konu": "Üslü Sayılar", "detay": "Üslü ifadelerde denklem çözme ve kurallar."},
    16: {"tarih": "1 Eylül", "ders": "Fen (Biyoloji)", "konu": "Canlıların Ortak Özellikleri", "detay": "İnorganik ve organik bileşikler giriş."},
    17: {"tarih": "2 Eylül", "ders": "Türkçe", "konu": "Paragrafta Anlam ve Ana Düşünce", "detay": "Yazarın amacı, ana düşünce ve yardımcı düşünce soruları."},
    18: {"tarih": "3 Eylül", "ders": "Matematik", "konu": "Köklü Sayılar", "detay": "Köklü ifadelerde işlemler ve eşlenik mantığı."},
    19: {"tarih": "4 Eylül", "ders": "Geometri", "konu": "Üçgende Eşlik ve Benzerlik", "detay": "Benzerlik teoremleri ve bol soru çözümü."},
    20: {"tarih": "5 Eylül", "ders": "Matematik (Problem)", "konu": "Sayı ve Kesir Problemleri", "detay": "Problem rutinlerine resmi başlangıç."},
    21: {"tarih": "6 Eylül", "ders": "Fen (Fizik)", "konu": "Madde ve Özellikleri", "detay": "Özkütle, dayanıklılık, adezyon ve kohezyon."},
    22: {"tarih": "7 Eylül", "ders": "İzin Günü", "konu": "Dinlenme", "detay": "Haftalık pazar molası."},
    23: {"tarih": "8 Eylül", "ders": "Türkçe", "konu": "Ses Bilgisi", "detay": "Ünsüz yumuşaması, benzeşmesi ve ses olayları."},
    24: {"tarih": "9 Eylül", "ders": "Matematik", "konu": "Çarpanlara Ayırma ve Özdeşlikler", "detay": "İki kare farkı, tam kare ifadeler."},
    25: {"tarih": "10 Eylül", "ders": "Geometri", "konu": "Üçgende Alan ve Açıortay-Kenarortay", "detay": "Alan bağıntıları ve yardımcı elemanlar."},
    26: {"tarih": "11 Eylül", "ders": "Matematik (Problem)", "konu": "Yaş Problemleri", "detay": "Yaş farkı sabitliği ve pratik denklem kurma."},
    27: {"tarih": "12 Eylül", "ders": "Fen (Kimya)", "konu": "Atom ve Periyodik Sistem", "detay": "Atom modelleri ve periyodik özellikler."},
    28: {"tarih": "13 Eylül", "ders": "Türkçe", "konu": "Yazım Kuralları", "detay": "Büyük harflerin kullanımı, de/da ve ki'nin yazımı."},
    29: {"tarih": "14 Eylül", "ders": "İzin Günü", "konu": "Dinlenme", "detay": "Haftalık pazar molası."},
    30: {"tarih": "15 Eylül", "ders": "Matematik (Problem)", "konu": "Yüzde, Kâr-Zarar Problemleri", "detay": "Alış-satış ve kar oranları hesaplamaları."}
}

@app.get("/")
def ana_sayfa(request: Request, gun: int = 1):
    aktif_gun = kamp_programi.get(gun, kamp_programi[1])
    return templates.TemplateResponse("index.html", {
        "request": request, 
        "gun": gun, 
        "aktif_gun": aktif_gun,
        "toplam_gun": len(kamp_programi)
    })
