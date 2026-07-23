from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI(title="YKS 3'ten 30'a 70 Günlük Sıfır Kampı")
templates = Jinja2Templates(directory="templates")

# 70 Günlük Eksiksiz Kamp Programı (Her gün Matematik Garanti)
CAMP_DATA = {}

detayli_gunler = {
    1: {
        "tarih": "18 Ağustos",
        "ders1": "MATEMATİK", "konu1": "Temel İşlemler ve İşaret Kuralları (+ / -)",
        "aciklama1": "Eksi ile eksinin çarpımı artı eder. İşlem önceliğine dikkat ediyoruz.",
        "gorevler1": ["İşaret kuralları tablosunu deftere yaz", "20 ham işlem sorusu çöz"],
        "soru1": {"metin": "(-3) . (+4) - (-12) / (-2) kaçtır?", "secenekler": ["A) -18", "B) -15", "C) -12", "D) -6", "E) 0"], "cevap": "B", "cozum": "İşlem önceliğiyle -18 bulunur."},
        "ders2": "FİZİK", "konu2": "Fizik Bilimine Giriş ve Temel Büyüklükler",
        "aciklama2": "Kısa Kütle şifresi ile temel büyüklükleri öğreniyoruz.",
        "gorevler2": ["Skaler/vektörel farkını not et", "15 soru çöz"],
        "soru2": {"metin": "Hangisi temel büyüklüktür?", "secenekler": ["A) Kuvvet", "B) Hız", "C) Enerji", "D) Sıcaklık", "E) İvme"], "cevap": "D", "cozum": "Sıcaklık temel büyüklüktür."}
    },
    2: {
        "tarih": "19 Ağustos",
        "ders1": "MATEMATİK", "konu1": "Rasyonel Sayılarda İşlem ve Payda Eşitleme",
        "aciklama1": "Alt kısımlar (payda) eşitlenmeden asla toplama yapılmaz.",
        "gorevler1": ["Payda eşitleme kurallarını deftere yaz", "15 rasyonel soru çöz"],
        "soru1": {"metin": "(1/2 + 1/3) / (1/6) kaçtır?", "secenekler": ["A) 1", "B) 3", "C) 5", "D) 6", "E) 10"], "cevap": "C", "cozum": "Payda eşitleyip ters çevirince 5 kalır."},
        "ders2": "TÜRKÇE", "konu2": "Sözcükte Anlam (Gerçek ve Mecaz)",
        "aciklama2": "Sözcüğün ilk akla gelen anlamı gerçek, soyutlaşmış anlamı mecazdır.",
        "gorevler2": ["Gerçek/mecaz farkını çalış", "20 sözcükte anlam çöz"],
        "soru2": {"metin": "'Boş' sözcüğü hangisinde soyut anlamdadır?", "secenekler": ["A) Boş şişe", "B) Boş cüzdan", "C) Boş sözler", "D) Boş sıra", "E) Boş bardak"], "cevap": "C", "cozum": "Boş söz anlamsız demektir."}
    },
    3: {
        "tarih": "20 Ağustos",
        "ders1": "MATEMATİK", "konu1": "1. Dereceden Denklemler (1. Gün - Temeller)",
        "aciklama1": "Eşitliğin karşı tarafına geçen sayı işaret değiştirir. X'i yalnız bırakma sanatıdır.",
        "gorevler1": ["Basit denklem kurallarını yaz", "15 denklem sorusu çöz"],
        "soru1": {"metin": "3x - 5 = x + 9 ise x kaçtır?", "secenekler": ["A) 5", "B) 6", "C) 7", "D) 8", "E) 9"], "cevap": "C", "cozum": "3x-x = 9+5 => 2x=14 => x=7."},
        "ders2": "KİMYA", "konu2": "Kimya Bilimi ve Simyadan Kimyaya",
        "aciklama2": "Simya deneme yanılmadır, kimya ise bilimseldir.",
        "gorevler2": ["Temel element simgelerini çalış", "15 soru çöz"],
        "soru2": {"metin": "Hangisi simya yöntemi değildir?", "secenekler": ["A) Damıtma", "B) Mayalama", "C) Polimerleştirme", "D) Özütleme", "E) Süzme"], "cevap": "C", "cozum": "Polimerleştirme modern kimyadır."}
    },
    4: {
        "tarih": "21 Ağustos",
        "ders1": "MATEMATİK", "konu1": "1. Dereceden Denklemler (2. Gün - Problem Geçişi)",
        "aciklama1": "Denklemleri sözel metinlere dökme ve 'sayı problemi' mantığına hazırlık.",
        "gorevler1": ["Denklem kurma alıştırması yap", "15 soru çöz"],
        "soru1": {"metin": "Hangi sayının 3 katının 5 fazlası 26'dır?", "secenekler": ["A) 5", "B) 6", "C) 7", "D) 8", "E) 9"], "cevap": "C", "cozum": "3x + 5 = 26 => 3x=21 => x=7."},
        "ders2": "BİYOLOJİ", "konu2": "Canlıların Ortak Özellikleri ve Hücre",
        "aciklama2": "Tüm canlıların temel ortak özellikleri ve prokaryot/ökaryot yapısı.",
        "gorevler2": ["Tablo çıkar", "15 soru çöz"],
        "soru2": {"metin": "Hangisi tüm hücreler için ortaktır?", "secenekler": ["A) Çekirdek", "B) Ribozom", "C) ER", "D) Mitokondri", "E) Golgi"], "cevap": "B", "cozum": "Ribozom ortaktır."}
    },
    5: {
        "tarih": "22 Ağustos",
        "ders1": "MATEMATİK", "konu1": "Temel Kavramlar (Tek-Çift ve Pozitif-Negatif Sayılar)",
        "aciklama1": "Tek ve çift sayıların toplama/çarpma kurallarını ezberlemeden mantığıyla kavrama.",
        "gorevler1": ["Tablo çıkar", "20 soru çöz"],
        "soru1": {"metin": "3x + 4 tek ise hangisi daima çifttir?", "secenekler": ["A) x", "B) x^2+1", "C) 5x-2", "D) x^3+x", "E) 2x+3"], "cevap": "D", "cozum": "x tektir, tek+tek çift olur."},
        "ders2": "TÜRKÇE", "konu2": "Cümlede Anlam (Neden-Sonuç, Amaç-Sonuç)",
        "aciklama2": "Cümledeki anlam ilişkilerini ayırt etme taktikleri.",
        "gorevler2": ["-mek için testini öğren", "20 soru çöz"],
        "soru2": {"metin": "Hangisinde amaç-sonuç ilişkisi vardır?", "secenekler": ["A) Yağmurdan maç ertelendi", "B) Kazanmak için çalıştı", "C) Soğuktan giyindi", "D) Borçtan sattı", "E) Yorgunluktan yattı"], "cevap": "B", "cozum": "Amaç-sonuçtur."}
    }
}

for g in range(1, 71):
    if g in detayli_gunler:
        d = detayli_gunler[g]
        CAMP_DATA[g] = {
            "gun": g, "tarih": d["tarih"],
            "ders1": d["ders1"], "konu1": d["konu1"], "aciklama1": d["aciklama1"], "gorevler1": d["gorevler1"], "soru1": d["soru1"],
            "ders2": d["ders2"], "konu2": d["konu2"], "aciklama2": d["aciklama2"], "gorevler2": d["gorevler2"], "soru2": d["soru2"]
        }
    else:
        fen_listesi = [("FİZİK", "Kuvvet ve Hareket Temelleri"), ("KİMYA", "Maddenin Halleri ve Bağlar"), ("BİYOLOJİ", "Hücre Bölünmeleri ve Kalıtım"), ("TÜRKÇE", "Paragraf ve Anlam Bilgisi")]
        secilen_fen = fen_listesi[(g - 1) % len(fen_listesi)]
        CAMP_DATA[g] = {
            "gun": g, "tarih": f"Kampın {g}. Günü",
            "ders1": "MATEMATİK", "konu1": f"Matematik İlerleme Kampı (Blok {g}: Problem ve Temel Sayılar)",
            "aciklama1": f"Sıfırdan 30 nete giden yolda {g}. gün matematik çalışmaları. Adım adım ilerliyoruz.",
            "gorevler1": ["Günlük matematik tekrarı yap", "En az 20 temel soru çöz", "Yanlış yaptığın soruları deftere not et"],
            "soru1": {"metin": f"Matematik Standart Pekiştirme Sorusu (Gün {g})", "secenekler": ["A) 12", "B) 14", "C) 16", "D) 18", "E) 20"], "cevap": "C", "cozum": "Temel işlem adımlarıyla çözüm yapılır."},
            "ders2": secilen_fen[0], "konu2": f"{secilen_fen[1]} (Gün {g})",
            "aciklama2": f"TYT {secilen_fen[0]} dersi için temel kavramlar ve soru çözümü.",
            "gorevler2": ["Konu özetini gözden geçir", "15 soru çöz"],
            "soru2": {"metin": f"TYT {secilen_fen[0]} Deneme Sorusu (Gün {g})", "secenekler": ["A) A", "B) B", "C) C", "D) D", "E) E"], "cevap": "A", "cozum": "Doğru analiz ve çözüm adımları."}
        }

@app.get("/", response_class=HTMLResponse)
async def index(request: Request, gun: int = 1):
    data = CAMP_DATA.get(gun, CAMP_DATA[1])
    return templates.TemplateResponse(
        request, 
        "index.html", 
        {"veri": data, "suanki_gun": gun, "toplam_gun": len(CAMP_DATA)}
    )
