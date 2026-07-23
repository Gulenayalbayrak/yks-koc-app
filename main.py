from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

kamp_programi = {
    1: {"tarih": "17 Agustos", "ders": "Matematik", "konu": "Temel Kavramlar", "detay": "Pozitif-negatif sayilar, tek-cift sayilar."},
    2: {"tarih": "18 Agustos", "ders": "Turkce", "konu": "Sozcukte Anlam", "detay": "Anlam bilimi ve paragraf giris."},
    3: {"tarih": "19 Agustos", "ders": "Matematik", "konu": "Bolme ve Bolunebilme", "detay": "Asal carpanlar, EBOB - EKOK."},
    4: {"tarih": "20 Agustos", "ders": "Geometri", "konu": "Uctende Acilar", "detay": "Temel aci ozellikleri."},
    5: {"tarih": "21 Agustos", "ders": "Fen (Fizik)", "konu": "Fizik Bilimine Giris", "detay": "Fiziksel nicelikler."},
    6: {"tarih": "22 Agustos", "ders": "Matematik", "konu": "Rasyonel Sayilar", "detay": "Islem yetenegi ve kesir problemleri."},
    7: {"tarih": "23 Agustos", "ders": "Izin Gunu", "konu": "Dinlenme", "detay": "Haftalik tekrar ve dinlenme."},
    8: {"tarih": "24 Agustos", "ders": "Turkce", "konu": "Cumlede Anlam", "detay": "Cumle yorumlama."},
    9: {"tarih": "25 Agustos", "ders": "Matematik", "konu": "Denklemler ve Esitsizlikler", "detay": "Bilinmeyenli denklemler."},
    10: {"tarih": "26 Agustos", "ders": "Geometri", "konu": "Ozel Ucgenler", "detay": "Dik ucgen ve ozellikleri."},
    11: {"tarih": "27 Agustos", "ders": "Fen (Kimya)", "konu": "Kimya Bilimi", "detay": "Guvenlik kurallari."},
    12: {"tarih": "28 Agustos", "ders": "Matematik", "konu": "Mutlak Deger", "detay": "Mutlak degerli denklemler."},
    13: {"tarih": "29 Agustos", "ders": "Turkce", "konu": "Paragrafin Yapisi", "detay": " Akisi bozan cumle."},
    14: {"tarih": "30 Agustos", "ders": "Izin Gunu", "konu": "Zafer Bayrami", "detay": "Dinlenme gunu."},
    15: {"tarih": "31 Agustos", "ders": "Matematik", "konu": "Uslu Sayilar", "detay": "Uslu ifadeler ve kurallar."}
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
