from produtoEstoque import ProdutoEstoque

class EstoqueProdutos:
    listaProdutos = []
    def adicionaProduto(self, produto):
        self.listaProdutos.append(produto)
    def getProduto(self, nome):
        for produto in self.listaProdutos:
            if produto.nome == nome:
                return produto