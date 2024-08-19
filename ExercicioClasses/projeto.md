# Exercicio de Classes
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

## Abordagem:

Definir a classe genérica e suas subclasses com seus atributos e métodos e relacioná-los

### Abordagem futura:

Trabalhar em cima de um dataset, para aliar o desafio com o exercitar do uso da biblioteca pandas

Vou ter uma Classe de Indicadores com métodos para coletar dados indicadores a partir do dataset 
ex: maior, menor, média, frequência

Fambém fazer augmentation a partir do dataset
Montar a pilha com a planilhas 
ex: usar o pandas pra gerar um outro dataset de "compras" com dados mesclados