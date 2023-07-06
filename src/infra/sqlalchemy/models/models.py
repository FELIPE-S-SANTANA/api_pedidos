from sqlalchemy import Column, Integer, String, Boolean
from src.infra.sqlalchemy.config.database import Base


class Produto(Base):

    __tablename__ = 'produto'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    preco = Column(float)
    detalhes = Column(String)
    disponivel = Column(Boolean)

    