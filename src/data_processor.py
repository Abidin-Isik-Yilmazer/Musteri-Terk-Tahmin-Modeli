import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder


class DataProcessor:
    def __init__(self, file_path):
        """
        Sınıf başlatıldığında (objesi oluşturulduğunda) çalışacak kurucu (constructor) metod.
        Dosya yolunu alır ve dataframe (df) değişkenini hazırlar.
        """
        self.file_path = file_path
        self.df = None

    def load_data(self):
        """Veriyi CSV dosyasından okuyup hafızaya alır."""
        self.df = pd.read_csv(self.file_path)
        print(f"Veri '{self.file_path}' konumundan başarıyla yüklendi. (Toplam {len(self.df)} satır)")
        return self.df

    def preprocess_data(self):
        """
        Makine öğrenmesi modelleri metin ("Yes", "Month-to-month") anlamaz, sayı ister.
        Bu metod veriyi sayısallaştırır.
        """
        if self.df is None:
            raise ValueError("Hata: Önce load_data() metodunu çağırarak veriyi yüklemelisiniz!")

        # Modelin öğrenmesinde hiçbir etkisi olmayan 'customerID' sütununu siliyoruz
        df_processed = self.df.drop('customerID', axis=1)

        # 'Contract' sütununu One-Hot Encoding ile sayısallaştırıyoruz
        # (Örn: Contract_One year: 1 veya 0 gibi sütunlara ayırır)
        df_processed = pd.get_dummies(df_processed, columns=['Contract'], drop_first=True)

        # 'Churn' hedef sütunumuzu (Yes/No) 1 ve 0'a çeviriyoruz
        label_encoder = LabelEncoder()
        df_processed['Churn'] = label_encoder.fit_transform(df_processed['Churn'])

        print("Veri ön işleme (sayısallaştırma) tamamlandı.")
        return df_processed

    def split_data(self, df_processed, test_size=0.2, random_state=42):
        """
        Veriyi bağımsız değişkenler (X) ve hedef/bağımlı değişken (y) olarak ayırır.
        Daha sonra modeli eğitmek (Train) ve test etmek (Test) için böler.
        """
        # Hedef değişken 'Churn', geri kalan her şey özellik (X)
        X = df_processed.drop('Churn', axis=1)
        y = df_processed['Churn']

        # Verinin %80'i eğitim, %20'si test için ayrılır
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=test_size, random_state=random_state
        )

        print(f"Veri bölündü -> Eğitim seti: {X_train.shape[0]} satır, Test seti: {X_test.shape[0]} satır.")
        return X_train, X_test, y_train, y_test