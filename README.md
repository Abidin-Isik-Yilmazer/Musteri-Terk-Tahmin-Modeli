# 📊 Müşteri Terk Tahmin Modeli 

Bu proje, telekomünikasyon sektöründeki müşterilerin hizmeti bırakma (churn) eğilimlerini önceden tespit etmek amacıyla geliştirilmişbir makine öğrenmesi projesidir. 
Sistem, **Nesne Yönelimli Programlama (OOP)** prensiplerine sadık kalınarak, modüler, ölçeklenebilir ve sürdürülebilir bir mimaride tasarlanmıştır.

## 🛠️ Kullanılan Teknolojiler

* **Dil:** Python 3.12
* **Kütüphaneler:** Pandas, Scikit-Learn
* **Geliştirme Ortamı:** PyCharm IDE

## 🏗️ Mimari ve Tasarım Yaklaşımı (OOP)

Spagetti kod yazımından kaçınılmış; veri ön işleme, model eğitimi ve ana çalışma mantığı birbirinden izole edilerek **Tek Sorumluluk Prensibi (Single Responsibility Principle)** uygulanmıştır.

* **DataProcessor Sınıfı:** Ham verinin okunması, gereksiz özelliklerin temizlenmesi, kategorik değişkenlerin dönüştürülmesi (One-Hot & Label Encoding) ve verinin eğitim/test setlerine ayrılmasından sorumludur.
* **ModelTrainer Sınıfı:** Makine öğrenmesi algoritmasının (Random Forest) başlatılması, eğitilmesi ve modelin hiç görmediği test verisi üzerinde performans metriklerinin hesaplanmasından sorumludur.

## 📂 Proje Dizin Yapısı

* 📁 **data/** (Sentetik müşteri veri setini barındırır)
* 📁 **src/** (OOP sınıflarını barındıran kaynak kod dizini)
  * 📄 `__init__.py` 
  * 📄 `data_processor.py` (Veri işleme sınıfı)
  * 📄 `model_trainer.py` (Model eğitim sınıfı)
* 📄 `create_data.py` (Analiz için sentetik veri üretim betiği)
* 📄 `main.py` (Sınıfları entegre eden ana yürütücü dosya)
* 📄 `requirements.txt` (Bağımlılık listesi)

## 🚀 Kurulum ve Çalıştırma

Projeyi kendi bilgisayarınızda test etmek için terminalinizde sırasıyla aşağıdaki komutları çalıştırabilirsiniz:

**1. Depoyu İndirin:**
> git clone https://github.com/Abidin-Isik-Yilmazer/Musteri-Terk-Tahmin-Modeli.git
> cd Musteri-Terk-Tahmin-Modeli

**2. Kütüphaneleri Yükleyin:**
> pip install -r requirements.txt

**3. Veri Setini Üretin:**
> python create_data.py

**4. Modeli Eğitin ve Test Edin:**
> python main.py

## 📈 Model Performansı ve Değerlendirme

Sistem, sınıflandırma için **Random Forest (Rastgele Orman)** algoritmasını kullanmaktadır. Modelin test verisi üzerindeki performansı aşağıdadır:

* **Genel Doğruluk (Accuracy):** %75.00
* **Ayrılan Müşterileri (Churn) Tespit Etme Başarısı:**
  * **Precision (Kesinlik):** 0.64
  * **Recall (Duyarlılık):** 0.50
  * **F1-Score:** 0.56

