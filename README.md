# 📺 Televisa Ratings Intelligence Dashboard

<div align="center">

![Televisa](https://img.shields.io/badge/Industry-Broadcast%20Media-003087?style=for-the-badge)
![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![Python](https://img.shields.io/badge/Python-ETL-3776AB?style=for-the-badge&logo=python&logoColor=white)

**Plataforma de análisis de audiencias, rating y competitividad para contenido televisivo**

</div>

---

## 🎯 Contexto del Proyecto

En la industria de la televisión abierta, **cada décima de rating representa millones de pesos en inversión publicitaria**. La capacidad de leer, visualizar y anticipar el comportamiento de las audiencias no es un diferenciador — es una necesidad operativa.

Este proyecto simula la infraestructura analítica que un equipo de **Inteligencia Operativa y Visualización de Datos** necesita para tomar decisiones editoriales, comerciales y de programación basadas en evidencia.

---

## 📊 Alcance del Dashboard

| Página | Nombre | Preguntas que responde |
|--------|--------|------------------------|
| 1 | **Executive Overview** | ¿Cómo cerró la semana? ¿Qué tendencia lleva el año? |
| 2 | **Program Performance** | ¿Cómo evoluciona cada programa episodio a episodio? |
| 3 | **Audience Intelligence** | ¿Quién nos ve, cuándo y qué tan leales son? |
| 4 | **Competitive Landscape** | ¿Cómo estamos vs Azteca y cable en cada franja? |

---

## 🔢 Métricas Clave

| Métrica | Definición | Fuente |
|---------|-----------|--------|
| **Rating** | % de hogares con TV sintonizados al canal | Estándar IBOPE/Nielsen |
| **Share** | % de audiencia activa que ve el programa | Calculado sobre total de TV encendida |
| **Audiencia (mm)** | Millones de personas estimadas viendo | Rating × cobertura estimada |
| **Demo 18-34 / 35-54 / 55+** | Distribución porcentual por grupo de edad | Segmentación estándar de mercado |
| **Rating MA4** | Promedio móvil 4 semanas (suaviza ruido) | Calculado en SQL / DAX |
| **Ventaja vs Azteca** | Diferencial de rating punto a punto | Comparativa directa |

---

## 🗄️ Arquitectura de Datos

```
televisa_ratings (tabla principal)
│
├── 520 registros  →  52 semanas × 10 programas
├── 18 columnas    →  dimensiones + métricas + demos
│
├── vw_kpis_ejecutivos     →  agregados por trimestre/canal/franja
├── vw_tendencia_semanal   →  serie temporal + promedio móvil 4sem
└── vw_competencia         →  Televisa vs Azteca vs Canal 5
```

**Stack tecnológico:**
- `Python` — generación del dataset mock con lógica de negocio realista
- `PostgreSQL` — almacenamiento, ETL views y queries analíticos
- `Power BI Desktop` — modelo de datos, DAX measures, dashboard final
- `DAX` — 20+ medidas calculadas para KPIs dinámicos

---

## 📁 Estructura del Repositorio

```
📁 televisa-ratings-dashboard/
├── 📁 data/
│   ├── televisa_ratings_mock.csv       # Dataset principal (520 registros)
│   └── data_dictionary.md             # Diccionario de métricas
├── 📁 sql/
│   └── televisa_queries.sql           # 16 queries + 3 ETL views (310 líneas)
├── 📁 python/
│   └── generate_dataset.py            # Script ETL de generación de datos
├── 📁 powerbi/
│   └── televisa_dashboard.pbix        # Dashboard Power BI (4 páginas)
├── 📁 assets/
│   └── dashboard_preview.png          # Screenshot del dashboard
└── 📄 README.md
```

---

## 📈 Insights Destacados del Análisis

- **La Rosa de Guadalupe** lidera con rating promedio de **8.2** — el programa más consistente del portafolio
- El **Prime Time (20:00–22:30)** concentra el **68% de la audiencia total** acumulada en el año  
- Televisa mantiene una **ventaja de +2.4 puntos** sobre Azteca Uno en Prime Time como promedio anual
- El segmento **55+** representa el **46% del perfil demográfico** promedio — audiencia leal y predecible
- **Q4 (oct-dic)** registra el pico de rating anual, consistente con el ciclo televisivo estándar

---

## 🚀 Cómo Ejecutar

### 1. Generar el dataset
```bash
pip install pandas numpy
python python/generate_dataset.py
```

### 2. Cargar en PostgreSQL
```sql
-- Crear tabla con el script de setup en sql/televisa_queries.sql
-- Importar CSV con COPY o pgAdmin Import/Export
\copy televisa_ratings FROM 'data/televisa_ratings_mock.csv' CSV HEADER;
```

### 3. Conectar Power BI
- Fuente de datos → PostgreSQL
- Server: `localhost` / Database: `[tu_db]`
- Importar tablas: `televisa_ratings` + las 3 vistas `vw_*`

---

## 👤 Autor

**Hugo Ernesto Aguilar Gallardo**  
Data Analyst Jr. | SQL · Python · Power BI · DAX  

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Perfil-0077B5?style=flat&logo=linkedin)](https://linkedin.com/in/hugo-ernesto-aguilar-gallardo-2359263a5)
[![GitHub](https://img.shields.io/badge/GitHub-Portfolio-181717?style=flat&logo=github)](https://github.com/Ernestoaguiga)

---

> *Dataset simulado con estructura basada en métricas estándar de medición de audiencias televisivas (IBOPE/Nielsen México). Los valores son representativos del comportamiento del mercado televisivo mexicano.*
