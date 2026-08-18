from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional, Dict

app = FastAPI(title="API Benchmarking de Productividad")

# Matriz de parámetros Cobb-Douglas y benchmarks sector-región
BENCHMARK_DATABASE = {
    "CIIU_C": {
        "nombre": "Manufactura",
        "alpha": 0.35,
        "beta": 0.65,
        "regiones": {
            "Lima": {"pl": 42000.0, "ptf": 125.4, "rc": 1.65, "roa": 0.082, "roe": 0.145},
            "Arequipa": {"pl": 38500.0, "ptf": 118.2, "rc": 1.58, "roa": 0.078, "roe": 0.138},
            "Nacional": {"pl": 36000.0, "ptf": 112.0, "rc": 1.50, "roa": 0.072, "roe": 0.129}
        }
    },
    "CIIU_G": {
        "nombre": "Comercio",
        "alpha": 0.25,
        "beta": 0.75,
        "regiones": {
            "Lima": {"pl": 31000.0, "ptf": 98.6, "rc": 1.45, "roa": 0.065, "roe": 0.120},
            "Arequipa": {"pl": 28000.0, "ptf": 92.1, "rc": 1.40, "roa": 0.060, "roe": 0.112},
            "Nacional": {"pl": 27000.0, "ptf": 89.5, "rc": 1.38, "roa": 0.058, "roe": 0.108}
        }
    },
    "CIIU_M": {
        "nombre": "Servicios Profesionales",
        "alpha": 0.18,
        "beta": 0.82,
        "regiones": {
            "Lima": {"pl": 55000.0, "ptf": 142.0, "rc": 1.80, "roa": 0.115, "roe": 0.190},
            "Arequipa": {"pl": 48000.0, "ptf": 130.5, "rc": 1.72, "roa": 0.102, "roe": 0.175},
            "Nacional": {"pl": 46000.0, "ptf": 124.0, "rc": 1.68, "roa": 0.098, "roe": 0.165}
        }
    }
}

class DiagnosticPayload(BaseModel):
    ciiu_division: str
    region: str
    ventas_totales: float = Field(..., gt=0)
    consumo_intermedio: float = Field(..., ge=0)
    trabajadores: float = Field(..., gt=0)
    stock_capital: float = Field(..., gt=0)
    # Ratios Financieros Opcionales
    activo_corriente: Optional[float] = None
    pasivo_corriente: Optional[float] = None
    activo_total: Optional[float] = None
    patrimonio: Optional[float] = None
    utilidad_neta: Optional[float] = None

def calcular_brecha(empresa_val: float, benchmark_val: float) -> dict:
    gap = ((empresa_val - benchmark_val) / benchmark_val) * 100.0 if benchmark_val != 0 else 0.0
    return {
        "valor": round(empresa_val, 2),
        "benchmark": round(benchmark_val, 2),
        "brecha": round(gap, 1)
    }

@app.post("/api/diagnostico")
def procesar_diagnostico(data: DiagnosticPayload):
    sector = BENCHMARK_DATABASE.get(data.ciiu_division)
    if not sector:
        raise HTTPException(status_code=400, detail="Sector CIIU no registrado en el sistema")
    
    bench = sector["regiones"].get(data.region) or sector["regiones"]["Nacional"]

    # 1. Valor Agregado Bruto (VAB)
    vab = data.ventas_totales - data.consumo_intermedio
    if vab <= 0:
        raise HTTPException(status_code=422, detail="El Consumo Intermedio no puede ser mayor o igual a las Ventas Totales.")

    # 2. Productividad Laboral
    pl = vab / data.trabajadores

    # 3. PTF (Función Cobb-Douglas: VAB / (K^alpha * L^beta))
    ptf = vab / ((data.stock_capital ** sector["alpha"]) * (data.trabajadores ** sector["beta"]))

    resultado = {
        "vab": round(vab, 2),
        "productividad_laboral": calcular_brecha(pl, bench["pl"]),
        "ptf": calcular_brecha(ptf, bench["ptf"]),
        "financiero": None
    }

    # 4. Ratios Financieros (si se proporcionaron)
    fin_dict = {}
    if data.activo_corriente is not None and data.pasivo_corriente and data.pasivo_corriente > 0:
        rc = data.activo_corriente / data.pasivo_corriente
        fin_dict["razon_corriente"] = calcular_brecha(rc, bench["rc"])

    if data.utilidad_neta is not None and data.activo_total and data.activo_total > 0:
        roa = (data.utilidad_neta / data.activo_total) * 100.0
        fin_dict["roa_pct"] = calcular_brecha(roa, bench["roa"] * 100.0)

    if data.utilidad_neta is not None and data.patrimonio and data.patrimonio > 0:
        roe = (data.utilidad_neta / data.patrimonio) * 100.0
        fin_dict["roe_pct"] = calcular_brecha(roe, bench["roe"] * 100.0)

    if fin_dict:
        resultado["financiero"] = fin_dict

    return resultado