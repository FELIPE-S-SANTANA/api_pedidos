from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey
from typing import List
from src.infra.sqlalchemy.config.database import Base
from sqlalchemy.orm import relationship, Mapped, mapped_column

class Produto(Base):

    __tablename__ = 'produto'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    preco = Column(Float)
    detalhes = Column(String)
    disponivel = Column(Boolean)


class Pedido(Base):

    __tablename__ = 'pedidos'

    id = Column(Integer, primary_key=True, index=True)
    quantidade = Column(Integer)
    entrega = Column(Boolean)
    endereco = Column(String)
    observacoes = Column(String)
    id_produto = Column(ForeignKey("produto.id"))

class Vendas(Base):

    __tablename__ = 'vendas'

    id = Column(Integer, primary_key=True, index=True)
    quantidade = Column(Integer)
    entrega = Column(Boolean)
    endereco = Column(String)
    observacoes = Column(String)
    id_produto = Column(ForeignKey("produto.id"))

