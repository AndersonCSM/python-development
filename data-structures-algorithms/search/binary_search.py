def pesquisa_binaria(lista, item):
    """
    A função pesquisa_binaria pega um array ordenado e um item. Se o item
    está no array, a função retorna a sua posição.

    :param lista: Descrição
    """
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]

        print(f"Baixo: {baixo}")
        print(f"meio : {meio}")
        # print(f"Chute: {chute}")
        print(f"Maior: {alto}\n")
        if chute == item:
            print("Sucesso!")
            return item

        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1
    return None


def main():
    lista_1 = [1, 3, 5, 7, 9]
    item_1 = 3

    pesquisa_binaria(lista_1, item_1)


main()
