from produto import Produto

class ProdutoCarrinho(Produto):
    def __init__(self, nome, val, qtd):
        super().__init__(nome, val, qtd)
