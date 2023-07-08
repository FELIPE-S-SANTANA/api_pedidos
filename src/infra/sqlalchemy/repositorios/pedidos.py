from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models
from .produtos import RepositorioProduto



class RepositorioPedidos():



    def __init__(self, db: Session):
        self.db = db
    

    def criar(self, pedido: schemas.Order):
        print(pedido)
        db_pedido = models.Pedido(
                        quantidade = pedido.quantidade,
                        entrega = pedido.entrega,
                        endereco = pedido.endereco,
                        observacoes = pedido.observacoes,
                        produto = pedido.id_produto
                    )

        self.db.add(db_pedido)
        self.db.commit()
        self.db.refresh(db_pedido)

        return db_pedido
    

    def listar(self):
        pedidos = self.db.query(models.Pedido).all()
        list_dict_pedidos = []
        for item in pedidos:
            dict_pedido = dict(item.__dict__)
            dict_pedido.pop('_sa_instance_state', None)
            dict_pedido['produtos'] = RepositorioProduto(self.db).obter(item.id_produto)
            list_dict_pedidos.append(dict_pedido)

        return list_dict_pedidos


    def obter(self, id):
        pedido = self.db.query(models.Pedido).get(id)

        return pedido

    def remover(self):
        pass