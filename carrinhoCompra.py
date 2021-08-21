from estoqueProdutos import EstoqueProdutos
from produtoEstoque import ProdutoEstoque
from produtoCarrinho import ProdutoCarrinho

class CarrinhoCompra:
    carrinho = []
    def __init__(self, estq):
        self.estoque = estq
    def adicionaItem(self, nome, qtd):
        produto = self.estoque.getProduto(nome)
        self.carrinho.append(ProdutoCarrinho(nome, produto.valor, qtd))
    def finalizaCompra(self):
        for prodCarrinho in self.carrinho:
            for prodEstoque in self.estoque.listaProdutos:
                if prodEstoque.nome == prodCarrinho.nome:
                    prodEstoque.atualizaProduto(prodCarrinho.quantidade)

    def calculaTotal(self):
        total = 0
        for produto in self.carrinho:
            total += produto.valor * produto.quantidade
        return total
