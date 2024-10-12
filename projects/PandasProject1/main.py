import pandas as pd
from Barra_Progresso import Barra_Progresso
from Dado_Geral import Dado_Geral

bprogresso = Barra_Progresso()
df_servicos = pd.read_excel('BaseServiçosPrestados.xlsx')
df_clientes = pd.read_csv('CadastroClientes.csv', sep=';', decimal=',', index_col=0)
df_funcionarios = pd.read_csv('CadastroFuncionarios.csv', sep=';', decimal=',', index_col=0)

# soma_salario = df_funcionarios['Salario Base'].sum()
# soma_impostos = df_funcionarios['Impostos'].sum()
# soma_beneficios = df_funcionarios['Beneficios'].sum()
# soma_vt = df_funcionarios['VT'].sum()
# soma_vr = df_funcionarios['VR'].sum()
# total_salario = soma_salario + soma_impostos + soma_beneficios + soma_vt + soma_vr
# print('Gasto total com salários de funcionários:', total_salario)

# df_faturamento = pd.DataFrame(columns=['faturamento'])
# for _, servico in df_servicos.iterrows():
#     cliente_servico_id = servico['ID Cliente']
#     faturamento_servico = servico['Tempo Total de Contrato (Meses)'] * df_clientes.loc[cliente_servico_id, 'Valor Contrato Mensal']
#     df_faturamento.loc[_] = faturamento_servico
# total_faturamento = df_faturamento['faturamento'].sum()
# print('Faturamento da empresa:', total_faturamento)

# num_funcionarios_servicos = len(df_servicos['ID Funcionário'].unique())
# num_funcionarios = len(df_funcionarios)
# porc_funcionarios_servicos = (num_funcionarios_servicos / num_funcionarios) * 100
# print(r' % de funcionários que já fechou algum contrato:', porc_funcionarios_servicos)