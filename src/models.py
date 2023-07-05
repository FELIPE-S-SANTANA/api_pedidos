from pydantic import BaseModel
from typing import Optional, List



class User(BaseModel):
    id: Optional[str] = None
    nome: str
    telefone: str
    minhas_vendas: List[Order]
    meus_pedidos: List[Order]


class Product(BaseModel):
    id: Optional[str] = None
    nome: str
    detalhes: str
    preco: float
    disponivel: bool = False


class Order(BaseModel):
    id: Optional[str] = None
    usuario: User
    produto: Product
    quatidade: int
    entrega: bool = True
    endereco: str
    observacoes: Optional[str] = 'Sem observações'





