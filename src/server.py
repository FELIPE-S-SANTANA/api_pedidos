from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from src.schemas.schemas import Product
from src.infra.sqlalchemy.config.database import get_db, criar_bd
from src.infra.sqlalchemy.repositorios.produtos import RepositorioProduto


criar_bd()

app = FastAPI()


@app.post('/produtos')
def criar_produto(produto: Product, db: Session = Depends(get_db)):
    produto_criado = RepositorioProduto(db).criar(produto)
    return produto_criado


@app.get('/produtos')
def list_produtos():
    return {'msg':'Lista_produtos'}