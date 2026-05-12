import pandas as pd
import numpy as np
from datetime import date, timedelta
import random

random.seed(42)
np.random.seed(42)

# Programas Televisa realistas
programas = [
    {"nombre": "La Rosa de Guadalupe", "genero": "Drama", "canal": "Las Estrellas", "horario": "20:00", "franja": "Prime Time"},
    {"nombre": "Hoy", "genero": "Magazine", "canal": "Las Estrellas", "horario": "09:00", "franja": "Matutino"},
    {"nombre": "Netas Divinas", "genero": "Talk Show", "canal": "Unicable", "horario": "21:00", "franja": "Prime Time"},
    {"nombre": "Exatlón México", "genero": "Reality", "canal": "TUDN", "horario": "19:30", "franja": "Prime Time"},
    {"nombre": "Vencer el Pasado", "genero": "Telenovela", "canal": "Las Estrellas", "horario": "21:30", "franja": "Prime Time"},
    {"nombre": "Al Extremo", "genero": "Entretenimiento", "canal": "Las Estrellas", "horario": "23:00", "franja": "Late Night"},
    {"nombre": "Noticieros Televisa", "genero": "Noticias", "canal": "Las Estrellas", "horario": "22:30", "franja": "Late Night"},
    {"nombre": "Me Caigo de Risa", "genero": "Comedia", "canal": "Las Estrellas", "horario": "20:30", "franja": "Prime Time"},
    {"nombre": "Fútbol Total", "genero": "Deportes", "canal": "TUDN", "horario": "21:00", "franja": "Prime Time"},
    {"nombre": "Diseñando Tu Amor", "genero": "Telenovela", "canal": "Las Estrellas", "horario": "18:00", "franja": "Vespertino"},
]

# Base ratings por programa
base_ratings = {
    "La Rosa de Guadalupe": 8.2,
    "Hoy": 5.1,
    "Netas Divinas": 3.4,
    "Exatlón México": 6.8,
    "Vencer el Pasado": 7.3,
    "Al Extremo": 2.1,
    "Noticieros Televisa": 4.9,
    "Me Caigo de Risa": 6.1,
    "Fútbol Total": 5.7,
    "Diseñando Tu Amor": 4.3,
}

# Competidores por franja
competidores = {
    "Prime Time": {"Azteca Uno": 5.8, "Canal 5": 2.1, "Cable": 1.9},
    "Matutino": {"Azteca Uno": 3.2, "Canal 5": 1.4, "Cable": 0.8},
    "Vespertino": {"Azteca Uno": 2.8, "Canal 5": 1.1, "Cable": 0.6},
    "Late Night": {"Azteca Uno": 1.5, "Canal 5": 0.8, "Cable": 1.2},
}

# Generar 52 semanas (1 año) de datos
start_date = date(2024, 1, 1)
records = []

for week in range(52):
    semana_inicio = start_date + timedelta(weeks=week)
    semana_num = week + 1
    trimestre = (week // 13) + 1

    for prog in programas:
        nombre = prog["nombre"]
        base = base_ratings[nombre]
        franja = prog["franja"]
        comp = competidores[franja]

        # Variación semanal + tendencia temporal leve
        tendencia = 1 + (week * 0.001) * random.choice([-1, 1])
        variacion = np.random.normal(0, 0.3)
        rating = round(max(0.5, base * tendencia + variacion), 2)

        # Share = rating / total mercado estimado
        total_mercado = rating + sum(comp.values()) + np.random.normal(0, 0.5)
        share = round((rating / max(total_mercado, 1)) * 100, 2)

        # Audiencia en millones (correlacionada con rating)
        audiencia = round(rating * 1.35 + np.random.normal(0, 0.4), 2)

        # Demos demográficos (suman ~100%)
        demo_1834 = round(random.uniform(20, 40), 1)
        demo_3554 = round(random.uniform(25, 40), 1)
        demo_55plus = round(100 - demo_1834 - demo_3554, 1)

        # Rating competidores con variación
        comp_azteca = round(comp["Azteca Uno"] + np.random.normal(0, 0.4), 2)
        comp_canal5 = round(comp["Canal 5"] + np.random.normal(0, 0.2), 2)

        # Episodio (reinicia por temporada)
        temporada = (week // 13) + 1
        episodio = (week % 13) + 1

        records.append({
            "semana": semana_num,
            "fecha_inicio_semana": semana_inicio.strftime("%Y-%m-%d"),
            "trimestre": f"Q{trimestre}",
            "programa": nombre,
            "genero": prog["genero"],
            "canal": prog["canal"],
            "horario": prog["horario"],
            "franja_horaria": franja,
            "temporada": temporada,
            "episodio": episodio,
            "rating": rating,
            "share_pct": share,
            "audiencia_millones": audiencia,
            "rating_azteca": max(0.1, comp_azteca),
            "rating_canal5": max(0.1, comp_canal5),
            "demo_18_34_pct": demo_1834,
            "demo_35_54_pct": demo_3554,
            "demo_55plus_pct": demo_55plus,
        })

df = pd.DataFrame(records)
df.to_csv("/home/claude/televisa_ratings_mock.csv", index=False)
print(f"Dataset generado: {len(df)} filas x {len(df.columns)} columnas")
print(df.head(3).to_string())
print("\nEstadísticas básicas:")
print(df[["rating","share_pct","audiencia_millones"]].describe().round(2))
