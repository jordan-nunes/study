import pandas as pd
from Tubo import Tubo
from Dado_Geral import Dado_Geral
from Ordem import Ordem
from Produto import Produto
from Cliente import Cliente

banco_dados = pd.read_csv(r'dados.csv', encoding='utf-8')
dataframe = Tubo(banco_dados)

dado_geral = Dado_Geral()
cliente = Cliente()
ordem = Ordem()
produto = Produto()

for x in range(10):
#while not dataframe.dados.empty:
    dataframe.separar_dado_lifo()
    linha = dataframe.separar_dado_lifo()

    dado_geral.customer_id = linha['customer_id']
    dado_geral.customer_zip_code_prefix = linha['customer_zip_code_prefix']
    dado_geral.customer_city = linha['customer_city']
    dado_geral.customer_state = linha['customer_state']

    dado_geral.order_id = linha['order_id']
    dado_geral.order_purchase_timestamp = linha['order_purchase_timestamp']
    dado_geral.order_approved_at = linha['order_approved_at']

    dado_geral.product_id = linha['product_id']
    dado_geral.product_category_name = linha['product_category_name']
    dado_geral.product_weight_g = linha['product_weight_g']
    dado_geral.product_length_cm = linha['product_length_cm']
    dado_geral.product_height_cm = linha['product_height_cm']
    dado_geral.product_width_cm = linha['product_width_cm']


    # cliente.exibir_dados()
    # cliente.verificar_vazio()

    #TODO: Aplicar mais métodos, exemplo:
    #cliente.método1()
    #cliente.método2()
    #cliente.método3()

    # ordem.exibir_dados()
    # ordem.verificar_vazio()

    #TODO: Aqui também, exemplo:
    #ordem.método()...


    # produto.exibir_dados()
    # produto.verificar_vazio

    #TODO: Aqui também, exemplo:
    #produto.método()...

    #removendo a linha da pilha
    dataframe.remover_dado_dataframe()

print('vitória! obrigado Jesus')