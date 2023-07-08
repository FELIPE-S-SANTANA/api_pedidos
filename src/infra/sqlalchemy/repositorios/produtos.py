from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models



class RepositorioProduto():



    def __init__(self, db: Session):
        self.db = db
    

    def criar(self, produto: schemas.Product):
        db_produto = models.Produto(
                        nome = produto.nome,
                        detalhes = produto.detalhes,
                        preco = produto.preco,
                        disponivel = produto.disponivel
                    )

        self.db.add(db_produto)
        self.db.commit()
        self.db.refresh(db_produto)

        return db_produto
    

    def listar(self):
        produtos = self.db.query(models.Produto).all()
        list_dict_produtos = []
        for item in produtos:
            dict_produto = dict(item.__dict__)
            dict_produto.pop('_sa_instance_state', None)
            list_dict_produtos.append(dict_produto)

        return list_dict_produtos


    def obter(self, id):
        produto = self.db.query(models.Produto).get(id)

        return produto

    def remover(self):
        pass