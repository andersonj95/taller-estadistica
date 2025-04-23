import matplotlib.pyplot as plt

# Datos
odontologia = {
    "intervalo": [(15, 19), (20, 24), (25, 29), (30, 34), (35, 39), (40, 44), (45, 49)],
    "frecuencia": [4, 6, 10, 14, 8, 6, 2],
    "marca_clase": [17, 22, 27, 32, 37, 42, 47],
}

servicio_social = {
    "intervalo": [(15, 19), (20, 24), (25, 29), (30, 34), (35, 39), (40, 44), (45, 49)],
    "frecuencia": [6, 8, 12, 10, 6, 4, 2],
    "marca_clase": [17, 22, 27, 32, 37, 42, 47],
}

def calcular_estadisticas(datos):
    f = datos["frecuencia"]
    xi = datos["marca_clase"]
    fx = [f[i] * xi[i] for i in range(len(f))]

    total_f = sum(f)
    total_fx = sum(fx)
    media = total_fx / total_f

    # Moda
    max_f = max(f)
    modal_index = f.index(max_f)
    Li = datos["intervalo"][modal_index][0]
    f1 = f[modal_index]
    f0 = f[modal_index - 1] if modal_index > 0 else 0
    f2 = f[modal_index + 1] if modal_index < len(f) - 1 else 0
    h = datos["intervalo"][0][1] - datos["intervalo"][0][0]
    moda = Li + ((f1 - f0) / ((f1 - f0) + (f1 - f2))) * h if (f1 - f0 + f1 - f2) != 0 else Li

    # Rango y amplitud
    min_val = datos["intervalo"][0][0]
    max_val = datos["intervalo"][-1][1]
    rango = max_val - min_val
    k = len(datos["intervalo"])
    amplitud = rango / k

    return {
        "media": round(media, 2),
        "moda": round(moda, 2),
        "rango": rango,
        "clases": k,
        "amplitud": round(amplitud, 2),
        "fx": fx
    }

def graficar_histograma(datos, titulo):
    etiquetas = [f"{a}-{b}" for a, b in datos["intervalo"]]
    plt.bar(etiquetas, datos["frecuencia"], color='skyblue', edgecolor='black')
    plt.title(f"Histograma - {titulo}")
    plt.xlabel("Intervalo de Edad")
    plt.ylabel("Frecuencia")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Resultados
print("Estadísticas - Odontología")
res_odont = calcular_estadisticas(odontologia)
print(res_odont)
graficar_histograma(odontologia, "Odontología")

print("\nEstadísticas - Servicio Social")
res_servicio = calcular_estadisticas(servicio_social)
print(res_servicio)
graficar_histograma(servicio_social, "Servicio Social")
