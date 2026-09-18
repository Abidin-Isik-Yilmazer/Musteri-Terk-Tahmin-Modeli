import pandas as pd
import random
import os


def create_synthetic_churn_data():
    # data klasörü yoksa oluştur
    if not os.path.exists('data'):
        os.makedirs('data')

    data = []
    # 1000 adet örnek müşteri verisi oluşturuyoruz
    for i in range(1000):
        tenure = random.randint(1, 72)  # Müşterinin şirkette kalma süresi (ay)
        monthly_charges = round(random.uniform(20.0, 120.0), 2)  # Aylık fatura
        contract = random.choice(['Month-to-month', 'One year', 'Two year'])  # Kontrat tipi

        # Müşterinin ayrılma (Churn) ihtimalini gerçeğe uygun simüle edelim:
        # Kısa süreli kontratı olanlar ve aylık faturası yüksek olanlar daha kolay ayrılır.
        churn_prob = 0.1
        if contract == 'Month-to-month':
            churn_prob += 0.3
        if monthly_charges > 80:
            churn_prob += 0.2
        if tenure < 12:
            churn_prob += 0.2

        churn = 'Yes' if random.random() < churn_prob else 'No'

        data.append({
            'customerID': f'CUST_{i:04d}',
            'tenure': tenure,
            'MonthlyCharges': monthly_charges,
            'Contract': contract,
            'Churn': churn
        })

    # Veriyi Pandas DataFrame'e çevirip CSV olarak kaydet
    df = pd.DataFrame(data)
    df.to_csv('data/churn_data.csv', index=False)
    print("Veri seti başarıyla oluşturuldu: data/churn_data.csv")


if __name__ == "__main__":
    create_synthetic_churn_data()