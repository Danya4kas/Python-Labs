from models import Antibiotic, Vitamin, Vaccine

def medicines(meds):
    for med in meds:
        print(med.info())
    
meds = [
    Antibiotic('Асперин', 30, 78.1),
    Vitamin('Магне-В6', 75,  56.8),
    Vaccine('Пфайзер', 45, 62.1)
]
medicines(meds)