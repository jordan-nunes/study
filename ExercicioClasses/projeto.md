# Titulo
Considere que uma empresa tem múltiplos processos executando ao mesmo tempo em diferentes máquinas, porém parte deles são parecidos, 
principalmente nos padrões de requisição, resposta e estrutura.
Sua missão então é criar uma pilha de execução que aceite qualquer trabalho, 
processe e retorne esse dados, contudo você não pode duplicar códigos, ou seja, a parte de requisição, processamento e resposta deverão ser realizados por uma estrutura comum a todos os processos.
Requisitos para uso da atividade:
Interfaces;
Polimorfismo;
Hierarquia;
Para melhorar o entendimento, imagine que você tem três processos, identificação de mãos, face e pés.
Crie Interfaces das partes em comum desses processos (Classes), 
e utilize o polimorfismo para a identificação das operações, e a hierarquia para uso de métodos comuns (ou específicos).


#utilizar classes abstratas

#estudar markdown

----------- abordagem:

Classe Indicadores
    classe principal com funções que são comuns à todas outras

    -pegar o dado mais e menos frequente
    -pegar o maior e menor dado

 Classes IndicadorCliente, IndicadorProduto, IndicadorLoja
    subclasses que vão tomar ações a partir de funções da classe principal

    Cliente
    -Ofertar fidelidade
    -Ofertar cupom
    -Mensagem de atendimento personalizado

    Produto
    -Promover
    -Reduzir preço
    -Retirar do catálogo

    Loja
    -Bonificar funcionários
    -Abrir mais lojas
    -Fechar loja







Montar pilha com planilhas
    usar o pandas pra gerar um outro dataset de "compras" com dados mesclados