from fastapi import FastAPI, Query, Depends
from sqlalchemy.orm import Session
from .database import get_db
from .schemas import AtletaResponse, AtletaCreate
from .models import Atleta
from fastapi_pagination import Page, add_pagination, paginate

app = FastAPI()

@app.get("/atletas/", response_model=Page[AtletaResponse])
def read_atletas(nome: str = Query(None), cpf: str = Query(None), db: Session = Depends(get_db)):
    query = db.query(Atleta)
    if nome:
        query = query.filter(Atleta.nome == nome)
    if cpf:
        query = query.filter(Atleta.cpf == cpf)
    return paginate(query.all())

@app.post("/atletas/")
def create_atleta(atleta: AtletaCreate, db: Session = Depends(get_db)):
    try:
        db_atleta = Atleta(**atleta.dict())
        db.add(db_atleta)
        db.commit()
        db.refresh(db_atleta)
        return db_atleta
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=303, detail=f"Já existe um atleta cadastrado com o cpf: {atleta.cpf}")

add_pagination(app)
