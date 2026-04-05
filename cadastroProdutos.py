produtos = []

def listarProdutos():
    
    if (len(produtos)== 0):
        print ("Não tem produtos a serem listados")

    for p in produtos:
        print(f'{p['nome']} ... R$ {p['preco']:.2f}')


def adicionarProduto (produto):
    produtos.append
    return true


def buscarProduto (nome_produto):
    for p in range (len (produtos)):
        if produtos [n]["nome"] == nome_produto:
            return p
        return None




