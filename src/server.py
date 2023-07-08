from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from src.schemas.schemas import Product, Order
from src.infra.sqlalchemy.config.database import get_db, criar_bd
from src.infra.sqlalchemy.repositorios.produtos import RepositorioProduto
from src.infra.sqlalchemy.repositorios.pedidos import RepositorioPedidos


criar_bd()

app = FastAPI()


@app.post('/produtos')
def criar_produto(produto: Product, db: Session = Depends(get_db)):
    produto_criado = RepositorioProduto(db).criar(produto)
    return produto_criado


@app.get('/produtos')
def list_produtos(db: Session = Depends(get_db)):
    lista_produtos = RepositorioProduto(db).listar()
    return lista_produtos


@app.post('/pedidos')
def criar_pedido(pedido: Order, db: Session = Depends(get_db)):
    pedido_criado = RepositorioPedidos(db).criar(pedido)
    return pedido_criado


@app.get('/pedidos')
def list_pedidos(db: Session = Depends(get_db)):
    lista_pedidos = RepositorioPedidos(db).listar()
    

    return lista_pedidos
