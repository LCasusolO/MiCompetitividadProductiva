"""
Matriz de Benchmarks Sectoriales y Regionales para el Perú
- 32 Sectores Económicos desagregados
- 26 Unidades Geográficas (24 departamentos + Lima Metropolitana + Lima Provincias) + Promedio Nacional
- Parámetros Cobb-Douglas calibrados: alpha (capital), beta (trabajo = 1 - alpha)
"""

REGIONES_PERU = [
    "Lima Metropolitana",
    "Lima Provincias",
    "Callao",
    "Amazonas",
    "Áncash",
    "Apurímac",
    "Arequipa",
    "Ayacucho",
    "Cajamarca",
    "Cusco",
    "Huancavelica",
    "Huánuco",
    "Ica",
    "Junín",
    "La Libertad",
    "Lambayeque",
    "Loreto",
    "Madre de Dios",
    "Moquegua",
    "Pasco",
    "Piura",
    "Puno",
    "San Martín",
    "Tacna",
    "Tumbes",
    "Ucayali",
    "Nacional"
]

# Factores de ajuste relativo regional frente al promedio nacional (PL base)
FACTORES_REGIONALES = {
    "Lima Metropolitana": 1.35,
    "Moquegua": 1.40,      # Alta intensidad minera
    "Arequipa": 1.15,
    "Ica": 1.12,
    "Callao": 1.18,
    "Áncash": 1.10,
    "La Libertad": 1.02,
    "Piura": 0.98,
    "Tacna": 0.95,
    "Cusco": 0.96,
    "Lima Provincias": 0.90,
    "Lambayeque": 0.88,
    "Junín": 0.85,
    "Pasco": 0.86,
    "Tumbes": 0.82,
    "San Martín": 0.75,
    "Ucayali": 0.74,
    "Cajamarca": 0.72,
    "Puno": 0.70,
    "Loreto": 0.73,
    "Madre de Dios": 0.78,
    "Ayacucho": 0.65,
    "Amazonas": 0.62,
    "Huánuco": 0.60,
    "Apurímac": 0.68,
    "Huancavelica": 0.55,
    "Nacional": 1.00
}

# 32 Sectores Económicos con parámetros base nacionales (en Soles S/.)
SECTORES_BASE = {
    "SEC_01": {
        "nombre": "Actividades artísticas, de entretenimiento y recreativas",
        "alpha": 0.24, "beta": 0.76,
        "pl_base": 26500.0, "ptf_base": 88.0, "rc": 1.45, "roa": 0.055, "roe": 0.105
    },
    "SEC_02": {
        "nombre": "Actividades de alojamiento",
        "alpha": 0.42, "beta": 0.58,
        "pl_base": 24000.0, "ptf_base": 72.5, "rc": 1.35, "roa": 0.048, "roe": 0.092
    },
    "SEC_03": {
        "nombre": "Actividades de atención de la salud humana y de asistencia social",
        "alpha": 0.22, "beta": 0.78,
        "pl_base": 38000.0, "ptf_base": 115.0, "rc": 1.70, "roa": 0.085, "roe": 0.150
    },
    "SEC_04": {
        "nombre": "Actividades de construcción especializada",
        "alpha": 0.26, "beta": 0.74,
        "pl_base": 32000.0, "ptf_base": 98.0, "rc": 1.40, "roa": 0.068, "roe": 0.130
    },
    "SEC_05": {
        "nombre": "Actividades de servicio de comidas y bebidas (restaurantes)",
        "alpha": 0.20, "beta": 0.80,
        "pl_base": 21000.0, "ptf_base": 76.0, "rc": 1.25, "roa": 0.062, "roe": 0.118
    },
    "SEC_06": {
        "nombre": "Actividades financieras y de seguros",
        "alpha": 0.28, "beta": 0.72,
        "pl_base": 85000.0, "ptf_base": 185.0, "rc": 1.95, "roa": 0.130, "roe": 0.210
    },
    "SEC_07": {
        "nombre": "Actividades inmobiliarias",
        "alpha": 0.55, "beta": 0.45,
        "pl_base": 62000.0, "ptf_base": 110.0, "rc": 1.60, "roa": 0.075, "roe": 0.125
    },
    "SEC_08": {
        "nombre": "Actividades profesionales y técnicas",
        "alpha": 0.16, "beta": 0.84,
        "pl_base": 48000.0, "ptf_base": 135.0, "rc": 1.75, "roa": 0.105, "roe": 0.180
    },
    "SEC_09": {
        "nombre": "Administración pública y defensa; planes de seguridad social",
        "alpha": 0.15, "beta": 0.85,
        "pl_base": 42000.0, "ptf_base": 120.0, "rc": 1.50, "roa": 0.050, "roe": 0.090
    },
    "SEC_10": {
        "nombre": "Almacenamiento y actividades de apoyo al transporte",
        "alpha": 0.36, "beta": 0.64,
        "pl_base": 39000.0, "ptf_base": 105.0, "rc": 1.55, "roa": 0.072, "roe": 0.135
    },
    "SEC_11": {
        "nombre": "Comercio al por mayor",
        "alpha": 0.24, "beta": 0.76,
        "pl_base": 34000.0, "ptf_base": 102.0, "rc": 1.50, "roa": 0.068, "roe": 0.128
    },
    "SEC_12": {
        "nombre": "Comercio al por menor",
        "alpha": 0.18, "beta": 0.82,
        "pl_base": 23500.0, "ptf_base": 84.0, "rc": 1.35, "roa": 0.058, "roe": 0.112
    },
    "SEC_13": {
        "nombre": "Construcción de edificios y obras de ingeniería civil",
        "alpha": 0.30, "beta": 0.70,
        "pl_base": 36000.0, "ptf_base": 104.0, "rc": 1.42, "roa": 0.070, "roe": 0.138
    },
    "SEC_14": {
        "nombre": "Cría de animales y ganadería",
        "alpha": 0.25, "beta": 0.75,
        "pl_base": 19500.0, "ptf_base": 68.0, "rc": 1.40, "roa": 0.052, "roe": 0.098
    },
    "SEC_15": {
        "nombre": "Cultivo de productos agrícolas",
        "alpha": 0.22, "beta": 0.78,
        "pl_base": 18000.0, "ptf_base": 64.0, "rc": 1.38, "roa": 0.050, "roe": 0.095
    },
    "SEC_16": {
        "nombre": "Elaboración de productos alimenticios y bebidas",
        "alpha": 0.35, "beta": 0.65,
        "pl_base": 38000.0, "ptf_base": 118.0, "rc": 1.55, "roa": 0.076, "roe": 0.142
    },
    "SEC_17": {
        "nombre": "Electricidad, gas y agua",
        "alpha": 0.58, "beta": 0.42,
        "pl_base": 92000.0, "ptf_base": 160.0, "rc": 1.85, "roa": 0.095, "roe": 0.165
    },
    "SEC_18": {
        "nombre": "Enseñanza",
        "alpha": 0.14, "beta": 0.86,
        "pl_base": 28000.0, "ptf_base": 95.0, "rc": 1.60, "roa": 0.065, "roe": 0.120
    },
    "SEC_19": {
        "nombre": "Extracción de minerales metalíferos",
        "alpha": 0.62, "beta": 0.38,
        "pl_base": 145000.0, "ptf_base": 210.0, "rc": 1.90, "roa": 0.145, "roe": 0.240
    },
    "SEC_20": {
        "nombre": "Extracción de otras minas y canteras",
        "alpha": 0.45, "beta": 0.55,
        "pl_base": 48000.0, "ptf_base": 112.0, "rc": 1.52, "roa": 0.078, "roe": 0.140
    },
    "SEC_21": {
        "nombre": "Extracción de petróleo crudo y gas natural",
        "alpha": 0.65, "beta": 0.35,
        "pl_base": 160000.0, "ptf_base": 225.0, "rc": 1.85, "roa": 0.138, "roe": 0.230
    },
    "SEC_22": {
        "nombre": "Fabricación de maquinaria, aparatos y equipos",
        "alpha": 0.32, "beta": 0.68,
        "pl_base": 44000.0, "ptf_base": 126.0, "rc": 1.62, "roa": 0.082, "roe": 0.152
    },
    "SEC_23": {
        "nombre": "Fabricación de prendas de vestir y productos textiles",
        "alpha": 0.22, "beta": 0.78,
        "pl_base": 22500.0, "ptf_base": 82.0, "rc": 1.40, "roa": 0.055, "roe": 0.108
    },
    "SEC_24": {
        "nombre": "Fabricación de productos minerales no metálicos y metales",
        "alpha": 0.45, "beta": 0.55,
        "pl_base": 46000.0, "ptf_base": 122.0, "rc": 1.58, "roa": 0.079, "roe": 0.145
    },
    "SEC_25": {
        "nombre": "Fabricación de productos químicos, farmacéuticos y plásticos",
        "alpha": 0.42, "beta": 0.58,
        "pl_base": 52000.0, "ptf_base": 138.0, "rc": 1.68, "roa": 0.088, "roe": 0.160
    },
    "SEC_26": {
        "nombre": "Industria de la madera, papel e imprenta",
        "alpha": 0.28, "beta": 0.72,
        "pl_base": 27000.0, "ptf_base": 90.0, "rc": 1.44, "roa": 0.060, "roe": 0.115
    },
    "SEC_27": {
        "nombre": "Información y comunicaciones",
        "alpha": 0.30, "beta": 0.70,
        "pl_base": 58000.0, "ptf_base": 150.0, "rc": 1.72, "roa": 0.098, "roe": 0.175
    },
    "SEC_28": {
        "nombre": "Pesca y acuicultura",
        "alpha": 0.38, "beta": 0.62,
        "pl_base": 41000.0, "ptf_base": 108.0, "rc": 1.48, "roa": 0.074, "roe": 0.136
    },
    "SEC_29": {
        "nombre": "Silvicultura y extracción de madera",
        "alpha": 0.28, "beta": 0.72,
        "pl_base": 23000.0, "ptf_base": 78.0, "rc": 1.38, "roa": 0.054, "roe": 0.102
    },
    "SEC_30": {
        "nombre": "Transporte por vía acuática y aérea",
        "alpha": 0.52, "beta": 0.48,
        "pl_base": 70000.0, "ptf_base": 140.0, "rc": 1.65, "roa": 0.080, "roe": 0.148
    },
    "SEC_31": {
        "nombre": "Transporte por vía terrestre y tuberías",
        "alpha": 0.40, "beta": 0.60,
        "pl_base": 33000.0, "ptf_base": 96.0, "rc": 1.42, "roa": 0.065, "roe": 0.122
    },
    "SEC_32": {
        "nombre": "Venta y reparación de vehículos automotores",
        "alpha": 0.22, "beta": 0.78,
        "pl_base": 29000.0, "ptf_base": 94.0, "rc": 1.46, "roa": 0.064, "roe": 0.120
    }
}

def obtener_benchmark_sector_region(sector_id: str, region: str) -> dict:
    """Devuelve los parámetros del sector ajustados por el multiplicador regional."""
    sector = SECTORES_BASE.get(sector_id)
    if not sector:
        return None
    
    factor = FACTORES_REGIONALES.get(region, 1.00)
    
    return {
        "nombre": sector["nombre"],
        "alpha": sector["alpha"],
        "beta": sector["beta"],
        "pl": round(sector["pl_base"] * factor, 2),
        "ptf": round(sector["ptf_base"] * factor, 2),
        "rc": sector["rc"],
        "roa": sector["roa"],
        "roe": sector["roe"]
    }