from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import Optional
from datetime import datetime

# Crear una conexión a la base de datos MySQL con SQLAlchemy
SQLALCHEMY_DATABASE_URL = 'mysql://root:acceso123@localhost:3306/person'
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Declarar una base de clase para las clases de modelo
Base = declarative_base()

# Definir el modelo de la tabla persona
class Persona(Base):
    __tablename__ = "tbperson"

    co_person = Column(Integer, primary_key=True, index=True)
    fe_regist = Column(DateTime, index=True)
    co_docide = Column(String, index=True)
    no_apepat = Column(String, index=True)
    no_apemat = Column(String, index=True)
    no_nombre = Column(String, index=True)
    ti_genero = Column(String, index=True)
    fe_nacimi = Column(DateTime, index=True)
    no_corper = Column(String, index=True)
    
# Crear todas las tablas en la base de datos
Base.metadata.create_all(bind=engine)

# Crear una sesión de SQLAlchemy
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()

# Inicializar la aplicación FastAPI
app = FastAPI()
# Asegúrate de tener un directorio llamado "templates" donde se encuentren tus archivos HTML.
templates = Jinja2Templates(directory="templates") 

# Montar archivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/persona/{co_person}", response_class=HTMLResponse)
@app.get("/persona", response_class=HTMLResponse)
async def editar_persona(request: Request, co_person: Optional[int] = None):
    session = SessionLocal()
    
    v_ls_tbperson = session.query(Persona).all()
    
    if co_person:
        v_rg_persona = session.query(Persona).filter(Persona.co_person == co_person).first()
    else:
        v_rg_persona = None
    
    session.close()
    
    return templates.TemplateResponse("persona.html", {"request": request, "v_rg_persona": v_rg_persona, "p_ls_person": v_ls_tbperson})

@app.post("/persona")
async def guardar_persona(request: Request):
    
    form_data = await request.form()
    
    co_docide = form_data.get("co_docide")
    no_apepat = form_data.get("no_apepat")
    no_apemat = form_data.get("no_apemat")
    no_nombre = form_data.get("no_nombre")
    ti_genero = form_data.get("ti_genero")
    fe_nacimi = form_data.get("fe_nacimi")
    no_corper = form_data.get("no_corper")

    # Crear una nueva sesión
    
    session = SessionLocal()
    # Obtener la fecha y hora actual
    fecha_actual = datetime.now()
    # Crear una instancia de Persona con los datos recibidos
    nueva_persona = Persona(
        fe_regist=fecha_actual,
        co_docide=co_docide,
        no_apepat=no_apepat,
        no_apemat=no_apemat,
        no_nombre=no_nombre,
        ti_genero=ti_genero,
        fe_nacimi=fe_nacimi,
        no_corper=no_corper
    )
    
    # Agregar la nueva persona a la sesión y guardar los cambios en la base de datos
    session.add(nueva_persona)
    session.commit()
    session.close()
    
    v_ls_tbperson = session.query(Persona).all()
    session.close()
    return templates.TemplateResponse("persona.html", {"request": request, "v_rg_persona": None, "p_ls_person": v_ls_tbperson})

@app.put("/persona/{co_person}")
async def actualizar_persona(co_person: int, request: Request):
    # Obtener los datos del formulario
    form_data = await request.form()
    
    # Obtener los valores de los campos del formulario
    co_docide = form_data.get("co_docide")
    no_apepat = form_data.get("no_apepat")
    no_apemat = form_data.get("no_apemat")
    no_nombre = form_data.get("no_nombre")
    ti_genero = form_data.get("ti_genero")
    fe_nacimi = form_data.get("fe_nacimi")
    no_corper = form_data.get("no_corper")
    
    # Buscar la persona en la base de datos por su ID
    persona = session.query(Persona).filter(Persona.co_person == co_person).first()
    
    # Si no se encuentra la persona, lanzar una excepción HTTP 404
    if not persona:
        raise HTTPException(status_code=404, detail="La persona no existe")

    # Actualizar los campos de la persona con los nuevos valores
    persona.co_docide = co_docide
    persona.no_apepat = no_apepat
    persona.no_apemat = no_apemat
    persona.no_nombre = no_nombre
    persona.ti_genero = ti_genero
    persona.fe_nacimi = fe_nacimi
    persona.no_corper = no_corper

    # Guardar los cambios en la base de datos
    session.commit()
    v_ls_tbperson = session.query(Persona).all()
    
    # Cerrar la sesión
    session.close()

    return templates.TemplateResponse("persona.html", {"request": request, "v_rg_persona": None, "p_ls_person": v_ls_tbperson})

@app.delete("/persona/{co_person}")
async def eliminar_persona(co_person: int, request: Request):
    session = SessionLocal()
    persona = session.query(Persona).filter(Persona.co_person == co_person).first()
    if persona:
        session.delete(persona)
        session.commit()
        v_ls_tbperson = session.query(Persona).all()
        session.close()
        
        return templates.TemplateResponse("persona.html", {"request": request, "v_rg_persona": None, "p_ls_person": v_ls_tbperson})
    else:
        raise HTTPException(status_code=404, detail=f"Persona con ID {co_person} no encontrada")
    db.close()
    