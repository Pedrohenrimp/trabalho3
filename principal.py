from carrinhoCompra import CarrinhoCompra
from estoqueProdutos import EstoqueProdutos
from produtoEstoque import ProdutoEstoque

class Principal:
    def executar():
        estoque = EstoqueProdutos()
        estoque.adicionaProduto(ProdutoEstoque("monitor", 500, 100))
        estoque.adicionaProduto(ProdutoEstoque("telefone", 150, 300))
        estoque.adicionaProduto(ProdutoEstoque("teclado", 70, 50))
        estoque.adicionaProduto(ProdutoEstoque("mouse", 50, 50))

        carrinho = CarrinhoCompra(estoque)
        carrinho.adicionaItem("monitor", 2)
        carrinho.adicionaItem("telefone", 5)
        carrinho.adicionaItem("teclado", 2)

        carrinho.finalizaCompra()

        print("A soma dos produtos é:", carrinho.calculaTotal())



Principal.executar()
