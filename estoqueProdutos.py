from produtoEstoque import ProdutoEstoque

class EstoqueProdutos:
    __listaProdutos = []
    def adicionaProduto(self, produto):
        self.__listaProdutos.append(produto)
    def getProduto(self, nome):
        for produto in self.__listaProdutos:
            if produto.getNome() == nome:
                return produto
    def getListaProdutos(self):
        return self.__listaProdutos