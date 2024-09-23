#Cálculos de ventas con librería statistics.
import csv, os, statistics

os.system('clear')

path = 'monthly_sales.csv'
monthly_sales = []

with open(path, mode='r') as file:
    reader = csv.DictReader(file)

    for month in reader:
        monthly_sales.append(float(month['sales']))

#Cálculo de media.
sales_mean = statistics.mean(monthly_sales)
print(f"La media de ventas es de: {sales_mean:.2f}")

#Cálculo de mediana.
sales_median = statistics.median(monthly_sales)
print(f"La mediana de ventas es de: {sales_median:.2f}")

#Cálculo de moda.
sales_mode = statistics.mode(monthly_sales)
print(f"La moda de ventas es de: {sales_mode:.2f}")

#Cálculo de desviación.
sales_stdev = statistics.stdev(monthly_sales)
print(f"La desviación estándar de las ventas es de: {sales_stdev:.2f}")

#Cálculo de varianza.
sales_variance = statistics.variance(monthly_sales)
print(f"La varianza de las ventas es de: {sales_variance:.2f}")

#Cálculo de máximos, mínimos y rango.
sales_max, sales_min = max(monthly_sales), min(monthly_sales)
sales_range = sales_max - sales_min
print(f"El máximo de ventas fue: {sales_max:.2f}, el mínimo: {sales_min:.2f}. El rango de ventas: {sales_range:.2f}")
