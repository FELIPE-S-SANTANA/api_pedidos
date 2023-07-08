from pydantic import BaseModel
from typing import Optional, List






class Product(BaseModel):
    id: Optional[str] = None
    nome: str
    detalhes: str
    preco: float
    disponivel: bool = False

    class Config():
        orm_mode = True


class Order(BaseModel):
    id: Optional[str] = None
    quantidade: int
    entrega: bool = True
    endereco: str
    observacoes: Optional[str] = 'Sem observações'
    id_produto: int

    class Config():
        orm_mode = True


class User(BaseModel):
    id: Optional[str] = None
    nome: str
    telefone: str
    minhas_vendas: List[Order]
    meus_pedidos: List[Order]


