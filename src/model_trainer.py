from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report


class ModelTrainer:
    def __init__(self, n_estimators=100, random_state=42):
        """
        ModelTrainer sınıfı başlatıldığında (objesi oluşturulduğunda) çalışır.
        Random Forest sınıflandırıcı modelini tanımlar.
        - n_estimators: Ormandaki karar ağacı sayısı.
        """
        self.model = RandomForestClassifier(n_estimators=n_estimators, random_state=random_state)
        self.is_trained = False

    def train(self, X_train, y_train):
        """
        Modeli, eğitim verilerini (X_train, y_train) kullanarak eğitir.
        """
        print("Random Forest modeli eğitimi başlıyor...")
        self.model.fit(X_train, y_train)
        self.is_trained = True
        print("Model başarıyla eğitildi!")

    def evaluate(self, X_test, y_test):
        """
        Eğitilmiş modelin başarısını test verileri üzerinde ölçer.
        Doğruluk (Accuracy) ve Sınıflandırma Raporu çıktıları üretir.
        """
        if not self.is_trained:
            raise ValueError("Hata: Model henüz eğitilmedi! Önce train() metodunu çağırmalısınız.")

        print("Model test verisi üzerinde değerlendiriliyor...\n")
        y_pred = self.model.predict(X_test)

        # Başarı metriklerini hesaplama
        accuracy = accuracy_score(y_test, y_pred)
        report = classification_report(y_test, y_pred)

        print("--- Model Başarı Sonuçları ---")
        print(f"Doğruluk (Accuracy) Oranı: {accuracy * 100:.2f}%")
        print("Sınıflandırma Raporu:\n", report)

        return accuracy, report