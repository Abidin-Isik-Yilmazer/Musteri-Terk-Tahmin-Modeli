from src.data_processor import DataProcessor
from src.model_trainer import ModelTrainer


def run_project():
    # 1. Veri İşleme Aşaması
    # DataProcessor sınıfından bir nesne (obje) oluşturuyoruz
    data_path = "data/churn_data.csv"
    processor = DataProcessor(file_path=data_path)

    # Oluşturduğumuz nesnenin metotlarını sırayla çağırıyoruz
    processor.load_data()
    processed_df = processor.preprocess_data()
    X_train, X_test, y_train, y_test = processor.split_data(processed_df)

    print("-" * 50)

    # 2. Model Eğitimi Aşaması
    # ModelTrainer sınıfından bir nesne oluşturuyoruz
    trainer = ModelTrainer(n_estimators=100)

    # Modelimizi eğitim verileriyle eğitiyoruz
    trainer.train(X_train, y_train)

    # Eğitilen modeli test verileriyle değerlendiriyoruz
    trainer.evaluate(X_test, y_test)


if __name__ == "__main__":
    print("Müşteri Kayıp (Churn) Analizi Projesi Başlıyor...")
    print("-" * 50)
    run_project()