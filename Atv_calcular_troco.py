
cedulas = [{"R":100, "R": 50, "R": 20, "R": 10, "R": 5, "R": 2, "R": 1, "R": 0.50, "R": 0.25, "R": 0.10, "R": 0.05, "R": 0.01}]

def calcular_troco():
    
    total_compra  = float(input("Valor total da compra: "))
    valor_pago = float(input("Valor pago pelo cliente: "))
    
    if valor_pago == total_compra:
        print("Pagamento efetuado, não houve necessidade de troco")
        
    elif valor_pago < total_compra:
        print("Erro, valor pago pelo cliente é insuficiente")
        
    else:
        troco = valor_pago - total_compra
        print(f"O valor do troco é de R$ {troco} reais")

calcular_troco()




