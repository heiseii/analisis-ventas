import pandas as pd
import matplotlib.pyplot as plt

#Leer dataset
df = pd.read_csv("datos/ventas.csv")

#Calcular ventas totales
ventas_totales = df["amount"].sum()

#Producto más vendido
producto_mas_vendido = df.groupby("producto")["cantidad"].sum().idxmax()

#Ventas por mes
df["fecha"] = pd.to_datetime(df["fecha"])
df["mes"] = df["fecha"].dt.month

ventas_mes = df.groupby("mes")["amount"].sum()

#Mostrar resultados
print("Ventas totales:", ventas_totales)
print("Producto más vendido:", producto_mas_vendido)

#Generar gráfico
ventas_mes.plot(kind="bar")

plt.title("Ventas por mes")
plt.xlabel("Mes")
plt.ylabel("Ventas")

#Guardar gráfico
plt.savefig("resultados/grafico_ventas.png")