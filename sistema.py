produtos = {'Caderno':[12.99,'Caderno Tilibra 10 matérias', 10],'Caneta':[1.99,'Caneta FaberCastel Azul',10],'Lapis':[1.50,'Lapis FaberCastel HB',10],'Dicionario':[19.99,'Dicionário Aurélio 2024',10],'Borracha':[2.99,'Borracha FaberCastel branca',10]}
carrinho = {}
historico = {}
numeroDeCompras = 0
totalHistorico = 0

usuarios = {'admin@admin.com':['admin','senha123']}

while True:
    a = input("1 - Login \n2 - Cadastrar \n3 - Sair\n")
    acesso = False
    
    if a == '3':
        break
    
    while a == '1':
        login = input("Digite seu email: ")
        senha = input("Digite sua senha: ")
        
        if (login in usuarios) and (senha == usuarios[login][1]):
            acesso = True
            break
        
        else:
            print("Login ou senha inválidos! Digite novamente")           
    
    while a == '2':
        email = input("Cadastre seu email: ")
        nome = input("Cadastre seu login: ")
        senha = input("Cadastre sua senha: ")
        usuarios[email] = [nome,senha]
        print('Cadastro realizado! ')
        break   
        
    if acesso:
        print("Login realizado!")     
    
    while acesso:
              
        b = input("1 - Visualizar catálogo\n2 - Visualizar carrinho de compra\n3 - Finalizar compra\n4 - Histórico de compras\n5 - Sair\n")

        if b == '5':
            break

        if b == '1':
            subtotal = 0
            print("Catálogo de produtos: ")
            for i in produtos:
                print(f"Produto: {i}\nPreço: R${produtos[i][0]:.2f}\nDescrição: {produtos[i][1]}\nQuantidade: {produtos[i][2]}\n--------------")
                
            while True:
                c = input("Deseja adicionar algum produto ao carrinho (S/N)?: ")

                if c == 'N':
                    break

                if c == 'S':
                    p = input("Digite o nome do produto: ")
                    if p in produtos:
                        q = int(input("Digite a quantidade do produto que deseja: "))
                        if q > produtos[p][2]:
                            print("Quantidade indisponível, tente novamente!")
                        else:
                            carrinho[p] = [produtos[p][0],produtos[p][1],q]
                            produtos[p][2] -= q
                            print("Produto adicionado ao carrinho!")
                    else:
                        print("Produto não existe!")

        if b == '2':
            print("Seu carrinho de compras: ")
            for i in carrinho:
                print(f"Produto: {i}\nPreço: R${carrinho[i][0]:.2f}\nDescrição: {carrinho[i][1]}\nQuantidade: {carrinho[i][2]}")
                subtotal += carrinho[i][0]*carrinho[i][2]
            
            print(f"Seu subtotal é de R${subtotal:.2f}")
            
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
                total += carrinho[i][0]*carrinho[i][2]
            
            print(f"Total R${total:.2f}")
            pagamento = input("Forma de pagamento\n1 - Dinheiro\n2 - Cartão de crédito\n3 - PIX\n")

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
                        print(f'Seu troco é de R${valor-total:.2f}')
                        print("Compra finalizada com sucesso!")
                        numeroDeCompras += 1
                        for i in carrinho:
                            historico[numeroDeCompras] = carrinho
                        carrinho = {}
                        break


            if pagamento == '2':
                cartao = [input("Insira o número do cartão"),input("Insira a validade do cartão"), input("Insira o CVV")]
                print("Compra finalizada com sucesso!")
                numeroDeCompras += 1
                for i in carrinho:
                    historico[numeroDeCompras] = carrinho
                carrinho = {}
            
            if pagamento == '3':
                print("Copie a seguitne chave pix e realize o pagamento: 111.222.333-44")
                pa = input("Confirme o pagamento (S/N)? ")
                if pa == 'S':
                    print("Compra finalizada com sucesso!")
                    numeroDeCompras += 1
                    for i in carrinho:
                        historico[numeroDeCompras] = carrinho
                    carrinho = {}
                
                else:
                    cancelar = input("Deseja cancelar a compra (S/N)? ")
                    if cancelar == 'S':
                        print('Compra cancelada!')
                        
        if b == '4':

            for i in historico:
                total2 = 0
                print(f'Sua compra de número {i}')
                for j in historico[i]:
                    print(f'{historico[i][j][2]} - {j} por R$ {historico[i][j][0]*historico[i][j][2]:.2f}')
                    total2 += historico[i][j][0]*historico[i][j][2]
                    totalHistorico += total2
                print(f'Total da compra {i} R$ {total2:.2f}\n--------------------')
            
            print(f"Total de todas as compras R$ {totalHistorico:.2f}\n-----------")
                    
    break