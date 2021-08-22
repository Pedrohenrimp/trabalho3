from estoqueProdutos import EstoqueProdutos
from produtoEstoque import ProdutoEstoque
from produtoCarrinho import ProdutoCarrinho

class CarrinhoCompra:
    __carrinho = []
    def __init__(self, estq):
        self.__estoque = estq
    def adicionaItem(self, nome, qtd):
        produto = self.__estoque.getProduto(nome)
        self.__carrinho.append(ProdutoCarrinho(nome, produto.getValor(), qtd))
    def finalizaCompra(self):
        for prodCarrinho in self.__carrinho:
            for prodEstoque in self.__estoque.getListaProdutos():
                if prodEstoque.getNome() == prodCarrinho.getNome():
                    prodEstoque.atualizaQuantidade(-prodCarrinho.getQuantidade())

    def calculaTotal(self):
        total = 0
        for produto in self.__carrinho:
            total += produto.getValor() * produto.getQuantidade()
        return total
