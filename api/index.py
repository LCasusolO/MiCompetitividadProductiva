from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
from api.benchmarks import SECTORES_BASE, REGIONES_PERU, obtener_benchmark_sector_region

app = FastAPI(title="Motor de Benchmarking Sectorial y Regional")

class DiagnosticPayload(BaseModel):
    sector_id: str = Field(..., example="SEC_16")
    region: str = Field(..., example="Lima Metropolitana")
    ventas_totales: float = Field(..., gt=0)
    consumo_intermedio: float = Field(..., ge=0)
    trabajadores: float = Field(..., gt=0)
    stock_capital: float = Field(..., gt=0)
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

@app.get("/api/catalogo")
def obtener_catalogo():
    """Retorna la lista de sectores y regiones para poblar los selectores del frontend."""
    sectores = [{"id": k, "nombre": v["nombre"]} for k, v in SECTORES_BASE.items()]
    return {
        "sectores": sectores,
        "regiones": REGIONES_PERU
    }

@app.post("/api/diagnostico")
def procesar_diagnostico(data: DiagnosticPayload):
    bench = obtener_benchmark_sector_region(data.sector_id, data.region)
    if not bench:
        raise HTTPException(status_code=400, detail="Sector económico no encontrado.")

    # 1. Valor Agregado Bruto (VAB)
    vab = data.ventas_totales - data.consumo_intermedio
    if vab <= 0:
        raise HTTPException(status_code=422, detail="El Consumo Intermedio no puede ser mayor o igual a las Ventas Totales.")

    # 2. Productividad Laboral
    pl = vab / data.trabajadores

    # 3. PTF Cobb-Douglas
    ptf = vab / ((data.stock_capital ** bench["alpha"]) * (data.trabajadores ** bench["beta"]))

    resultado = {
        "vab": round(vab, 2),
        "sector_nombre": bench["nombre"],
        "region_consultada": data.region,
        "productividad_laboral": calcular_brecha(pl, bench["pl"]),
        "ptf": calcular_brecha(ptf, bench["ptf"]),
        "financiero": None
    }

    # 4. Ratios Financieros
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