
from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import date, datetime

# Base compartida
class VehiculoBase(BaseModel):
    vehiculo_id: int
    cliente_id: int
    placa: str 
    marca: str 
    modelo: str 
    anio: int
    color: str 
    vin: str
    
# Datos requeridos al crear un Clientes (POST)
class VehiculoCreate(VehiculoBase):
    pass

# Formato de respuesta que envía la API (incluye el id asignado por Supabase)
class VehiculoResponse(VehiculoBase):
    vehiculo_id: int

    model_config = ConfigDict(from_attributes=True)
    