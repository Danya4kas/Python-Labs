import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('csv_file')          
args = parser.parse_args()                

df = pd.read_csv(args.csv_file)

mean_price = np.mean(df['price_per_unit'])
median_quantity = np.median(df['quantity'])
standard_deviation = np.std(df['price_per_unit'])

df['total_price'] = df['quantity'] * df['price_per_unit']
top_supplier = df.loc[df['total_price'].idxmax(), 'supplier']
category_totals = df.groupby('category')['quantity'].sum()

low_supply = df[df['quantity'] < 100]
low_supply.to_csv('low_supply.csv')

print(df.sort_values('total_price', ascending=False).head(3))

with open('report.txt', 'w') as f:
    f.write(f"Середня ціна: {mean_price}\n")
    f.write(f"Медіана кількості: {median_quantity}\n")
    f.write(f"Стандартне відхилення ціни: {standard_deviation}\n")
    f.write(f"Постачальник з найбільшим прибутком: {top_supplier}\n")
    f.write("Файл з дефіцитними поставками: low_supply.csv\n")

category_totals.plot(kind='bar')
plt.xlabel('Категорія')
plt.ylabel('Кількість')
plt.title('Розподіл кількості препаратів за категоріями')
plt.savefig('categories.png')