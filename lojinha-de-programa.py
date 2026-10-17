# Loginha de Programa - versão simples (só Python, sem HTML)

# Cada produto: nome, preço, quantidade atual e estoque inicial
produtos = [
    {"nome": "Teclado", "preco": 120.00, "qtd": 5, "inicial": 5},
    {"nome": "Mouse", "preco": 60.00, "qtd": 8, "inicial": 8},
    {"nome": "Microfone", "preco": 250.00, "qtd": 3, "inicial": 3},
    {"nome": "Headset", "preco": 180.00, "qtd": 4, "inicial": 4},
    {"nome": "Webcam", "preco": 200.00, "qtd": 2, "inicial": 2},
]

carrinho = []  # lista de (produto, quantidade)


def mostrar_produtos():
    print("\n--- PRODUTOS ---")
    for i in range(len(produtos)):
        p = produtos[i]
        if p["qtd"] > 0:
            print(f"{i + 1} - {p['nome']} | R$ {p['preco']:.2f} | {p['qtd']} em estoque")
        else:
            print(f"{i + 1} - {p['nome']} | R$ {p['preco']:.2f} | Não disponível")


def quantidade_no_carrinho(produto):
    total = 0
    for item, qtd in carrinho:
        if item is produto:
            total += qtd
    return total


def adicionar_ao_carrinho():
    mostrar_produtos()
    escolha = input("\nNúmero do produto: ")
    if not escolha.isdigit() or int(escolha) < 1 or int(escolha) > len(produtos):
        print("Produto inválido!")
        return

    produto = produtos[int(escolha) - 1]

    if produto["qtd"] == 0:
        print(f"{produto['nome']} não está disponível.")
        return

    quantidade = input("Quantidade: ")
    if not quantidade.isdigit() or int(quantidade) < 1:
        print("Quantidade inválida!")
        return
    quantidade = int(quantidade)

    livre = produto["qtd"] - quantidade_no_carrinho(produto)
    if quantidade > livre:
        print(f"Só temos {livre} unidade(s) de {produto['nome']} disponíveis.")
        return

    carrinho.append((produto, quantidade))
    print(f"{quantidade}x {produto['nome']} adicionado ao carrinho.")


def ver_carrinho():
    print("\n--- CARRINHO ---")
    if len(carrinho) == 0:
        print("O carrinho está vazio.")
        return 0
    total = 0
    for produto, qtd in carrinho:
        subtotal = produto["preco"] * qtd
        total += subtotal
        print(f"{qtd}x {produto['nome']} = R$ {subtotal:.2f}")
    print(f"Total: R$ {total:.2f}")
    return total


def finalizar_compra():
    total = ver_carrinho()
    if total == 0:
        return

    confirma = input("\nFinalizar compra? (s/n): ").lower()
    if confirma != "s":
        print("Compra não finalizada.")
        return

    for produto, qtd in carrinho:
        antes = produto["qtd"]
        produto["qtd"] -= qtd
        print(f"{produto['nome']}: estoque reduzido de {antes} para {produto['qtd']}.")

        # Quando o estoque zera, reinicia
        if produto["qtd"] == 0:
            print(f"{produto['nome']} esgotou! Reabastecendo...")
            produto["qtd"] = produto["inicial"]
            print(f"{produto['nome']} voltou ao estoque: {produto['qtd']} unidade(s).")

    carrinho.clear()
    print(f"\nCompra finalizada! Total pago: R$ {total:.2f}. Obrigado!")


while True:
    print("\n=== LOGINHA DE PROGRAMA ===")
    print("1 - Ver produtos")
    print("2 - Adicionar ao carrinho")
    print("3 - Ver carrinho")
    print("4 - Finalizar compra")
    print("0 - Sair")
    opcao = input("Escolha: ")

    if opcao == "1":
        mostrar_produtos()
    elif opcao == "2":
        adicionar_ao_carrinho()
    elif opcao == "3":
        ver_carrinho()
    elif opcao == "4":
        finalizar_compra()
    elif opcao == "0":
        print("Até a próxima!")
        break
    else:
        print("Opção inválida!")