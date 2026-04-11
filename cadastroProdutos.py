produtos = []

def listarProdutos():
    
    if (len(produtos)== 0):
        print ("Não tem produtos a serem listados")

    for p in produtos:
        print(f'{p['nome']} ... R$ {p['preco']:.2f}')


def adicionarProduto (produto):
    produtos.append(produto)
    return True


def buscarProduto (nome_produto):
    for p in range (len (produtos)):
        if produtos [p]["nome"] == nome_produto:
            return p
    return None    

def atualizarProduto (indice, produto):
    if indice >=0 and indice < len (produtos):
        produtos [indice] = produto
        return True
    return False

def removerProduto (indice):
     if indice >=0 and indice < len (produtos):
         produtos.pop(indice)
         return True
     return False
     
        




