produtos = {'Caderno':[12.99,'Caderno Tilibra 10 matérias']}
carrinho = {}
historico = {}
numeroDeCompras = 0

while True:
    
    b = input("1 - Visualizar catálogo\n2 - Visualizar carrinho de compra\n3 - Finalizar compra\n4 - Histórico de compras\n5 - Sair")

    if b == '5':
        break

    if b == '1':
        print("Catálogo de produtos: ")
        for i in produtos:
            print(f"Produto: {i}\nPreço: R${produtos[i][0]:.2f}\nDescrição: {produtos[i][1]}")
        
        
        while True:
            c = input("Deseja adicionar algum produto ao carrinho (S/N)?: ")

            if c == 'N':
                break

            if c == 'S':
                p = input("Digite o nome do produto: ")
                if p in produtos:
                    carrinho[p] = [produtos[p][0],produtos[p][1]]
                else:
                    print("Produto não existe!")

    if b == '2':
        print("Seu carrinho de compras: ")
        for i in carrinho:
            print(f"Produto: {i}\nPreço: R${carrinho[i][0]:.2f}\nDescrição: {carrinho[i][1]}")
        
        while True:

            r = input("Deseja remover algum item do carrinho (S/N)?: ")
            if r == 'N':
                break

            if r == 'S':
                item = input("Digite o nome do item que deseja remover: ")
                if item in carrinho:
                    del carrinho[item]
                else:
                    print("Produto não está no carrinho! ")
            
        b = input("Deseja finalizar a compra(S/N)? ")
        if b == 'S':
            b = '3'

    
    if b == '3':
        total = 0
        for i in carrinho:
            total += carrinho[i][0]
        
        print(f"Total R${total:.2f}")
        pagamento = input("Forma de pagamento\n1 - Dinheiro\n2 - Cartão de crédito\n3 - PIX")

        if pagamento == '1':

            while True:
                valor = float(input("Digite o valor que possui R$ "))
                if valor < total:
                    print("Valor insuficiente!")
                    cancelar = input("Deseja cancelar a compra (S/N)? ")
                    if cancelar == 'S':
                        print('Compra cancelada!')
                        break

                else:
                    print("Compra finalizada com sucesso!")
                    numeroDeCompras += 1
                    for i in carrinho:
                        historico[numeroDeCompras] = carrinho
                    carrinho = {}
                    break


        if pagamento == '2':
            cartao = [input("Insira o número do cartão"),input("Insira a validade do cartão"), input("Insira o CVV")]
            print("Compra finalizada com sucesso!")
            historico = carrinho
            carrinho = {}
        
        if pagamento == '3':
            print("Copie a seguitne chave pix e realize o pagamento: 111.222.333-44")
            pa = input("Confirme o pagamento (S/N)? ")
            if pa == 'S':
                print("Compra finalizada com sucesso!")
            
            else:
                cancelar = input("Deseja cancelar a compra (S/N)? ")
                if cancelar == 'S':
                    print('Compra cancelada!')
                        