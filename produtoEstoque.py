from produto import Produto

class ProdutoEstoque(Produto):
    def __init__(self, nome, val, qtd):
        super().__init__(nome, val, qtd)
    def atualizaQuantidade(self, qtd):
        self.quantidade += qtd