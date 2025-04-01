import os

class VendingMachine:
    def __init__(self, num_items, item_price):
        self.num_items = num_items  # Número de itens disponíveis
        self.item_price = item_price  # Preço de um item

    def buy(self, req_items, money):
        # Verifica se há itens suficientes
        if req_items > self.num_items:
            raise ValueError("Not enough items in the machine")
        
        # Verifica se o dinheiro é suficiente
        total_cost = req_items * self.item_price
        if money < total_cost:
            raise ValueError("Not enough coins")
        
        # Se as condições são atendidas, atualiza o número de itens e retorna o troco
        self.num_items -= req_items
        change = money - total_cost
        return change


if __name__ == '__main__':
    # Cria o arquivo de saída
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    # Lê o número de itens e o preço de cada item
    num_items, item_coins = map(int, input().split())
    machine = VendingMachine(num_items, item_coins)

    # Lê o número de transações
    n = int(input())
    
    # Processa cada transação
    for _ in range(n):
        req_items, money = map(int, input().split())
        try:
            change = machine.buy(req_items, money)
            fptr.write(str(change) + "\n")
        except ValueError as e:
            fptr.write(str(e) + "\n")

    # Fecha o arquivo de saída
    fptr.close()
