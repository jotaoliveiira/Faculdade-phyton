
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
     
produtos = [
     {"nome": "Arroz", "preco": 20.00},
    {"nome": "Feijão", "preco": 10.00},
    {"nome": "Farofa", "preco": 7.00},
    {"nome": "Brocolis", "preco": 6.00},
    {"nome": "Cereal", "preco": 8.00},
] 

opcao = None
while opcao != "0":
    print()
    print("========================================")
    print("               MENU")
    print("========================================")
    print("1 - Listar Produtos")
    print("2 - Adicionar Produto")
    print("3 - Buscar Produto")
    print("4 - Atualizar Produto")
    print("5 - Remover Produto")
    print("0 - Sair")
    print("========================================")

    if opcao == "1":
        print()
        print("LISTA DE PRODUTOS ======================")
        listarProdutos()

    elif opcao == "2":
        print()
        print("ADICIONAR DE PRODUTOS ==================")
        nome = input("Nome:")
        preco = float(input("Preço:"))
        if adicionarProduto({"nome": nome, "preco": preco}):
            print()
            print("LISTA DE PRODUTOS ======================")
            listarProdutos()
            print("Produto adicionado com sucesso")
        else:
            print("Erro ao cadastrar produto")

    elif opcao == "3":
        print()
        print("BUSCAR PRODUTO =========================")
        busca = input("Informe o nome do produto: ")
        produtoEncontrado = buscarProduto(busca)

        if produtoEncontrado == None:
            print("Produto não encontrado")
        else:
            print("Produto encontrado", produtos[produtoEncontrado])

    elif opcao == "4":
        print("ATUALIZAR PRODUTO ======================")
        print()
        busca = input("Informe o nome do produto: ")
        produtoEncontrado = buscarProduto(busca)
        if produtoEncontrado == None:
            print("Produto não encontrado")
        else:
            nome = input("nome: ")
            preco = float(input("preco: "))
            atualizarProduto(produtoEncontrado, {"nome": nome, "preco": preco})
        print()
        listarProdutos()

    elif opcao == "5":
        print("REMOVER PRODUTO ========================")
        print()
        remover = input("informe o produto para remover: ")
        produtoEncontrado = buscarProduto(remover)
        if produtoEncontrado == None:
            print("Produto não encontrado")
        else:
            removerProduto(produtoEncontrado)
            print("produto removido com sucesso")

        print()
        listarProdutos()

    elif opcao != None:
        print("Opção não existe")

    print()
    opcao = input("Opção desejada:")