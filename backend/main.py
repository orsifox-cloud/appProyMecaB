
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List

import models
import schemas
from database import engine, get_db

# Crea la tabla en Supabase automáticamente si aún no existe
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API de VEHICULOS del Taller Mecanico",
    version="1.0.0",
    description="Servicio Backend conectado a PostgreSQL en Supabase"
)

# Habilitar CORS para permitir llamadas desde Vercel o desarrollo local
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # En Vehiculos puedes acotarlo al dominio de Vercel
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 1. Obtener todos los productos
@app.get("/api/v1/vehiculos", response_model=List[schemas.VehiculoResponse], tags=["vehiculos"])
def list_vehiculos(db: Session = Depends(get_db)):
    return db.query(models.Vehiculo).all()

# 2. Registrar un nuevo Vehiculo
@app.post("/api/v1/vehiculos", response_model=schemas.VehiculoResponse, status_code=status.HTTP_201_CREATED, tags=["Vehiculos"])
def create_vehiculos(vehiculos: schemas.VehiculoCreate, db: Session = Depends(get_db)):
    nuevo_vehiculos = models.Vehiculo(**vehiculos.model_dump())
    db.add(nuevo_vehiculos)
    db.commit()
    db.refresh(nuevo_vehiculos)
    return nuevo_vehiculos
