import numpy as np
import pandas as pd
from datetime import datetime
from Tubo import Tubo
from Dado_Geral import Dado_Geral
from Cliente import Cliente
from Ordem import Ordem
from Produto import Produto
from Barra_Progresso import Barra_Progresso

banco_dados = pd.read_csv(r'dados.csv', encoding='utf-8')
dataframe = Tubo(banco_dados)

dado_geral = Dado_Geral()
cliente = Cliente(dado_geral)
ordem = Ordem(dado_geral)
produto = Produto(dado_geral)

barra_progresso = Barra_Progresso()

len_barra_progresso = barra_progresso.definir_barra_progresso(len(banco_dados))
#for x in range(5):
while not dataframe.dados.empty:
    linha = dataframe.separar_dado_lifo()
    linha = Dado_Geral.substituir_valor_coluna(linha)

    dado_geral.customer_id = linha['customer_id']
    dado_geral.customer_zip_code_prefix = int(linha['customer_zip_code_prefix'])
    dado_geral.customer_city = linha['customer_city']
    dado_geral.customer_state = linha['customer_state']

    dado_geral.order_id = linha['order_id']
    dado_geral.order_purchase_timestamp = datetime.strptime(linha['order_purchase_timestamp'], '%Y-%m-%d %H:%M:%S')
    dado_geral.order_approved_at = datetime.strptime(linha['order_approved_at'], '%Y-%m-%d %H:%M:%S')

    dado_geral.product_id = linha['product_id']
    dado_geral.product_category_name = linha['product_category_name']
    dado_geral.product_weight_g = float(linha['product_weight_g'])
    dado_geral.product_length_cm = float(linha['product_length_cm'])
    dado_geral.product_height_cm = float(linha['product_height_cm'])
    dado_geral.product_width_cm = float(linha['product_width_cm'])


    # cliente.exibir_dados()
    # cliente.verificar_vazio()
    # cliente.pegar_dados_cep(cliente.customer_zip_code_prefix)
    # cliente.validar_uf_cidade(cliente.customer_zip_code_prefix, cliente.customer_city, cliente.customer_state)


    # ordem.exibir_dados()
    # ordem.verificar_vazio()
    # ordem.delay_aprovacao(ordem.order_purchase_timestamp, ordem.order_approved_at)


    # produto.exibir_dados()
    # produto.verificar_vazio()
    # produto.cubagem(produto.product_height_cm, produto.product_width_cm, produto.product_length_cm)


    dataframe.remover_dado_dataframe()
    barra_progresso.update(len_barra_progresso)

print('\n\nvitória! obrigado Jesus')