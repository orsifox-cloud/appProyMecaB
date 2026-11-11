
from sqlalchemy import Column, Integer, String 
from database import Base

class Vehiculo(Base):
    __tablename__ = "vehiculos" #  Nombre de la tabla de SupaBase

    vehiculo_id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer, nullable=False)
    placa = Column(String, nullable=False) 
    marca = Column(String, nullable=False)
    modelo = Column(String, nullable=False)
    anio = Column(Integer, nullable=False)
    color = Column(String, nullable=False)
    vin = Column(String, nullable=False)
