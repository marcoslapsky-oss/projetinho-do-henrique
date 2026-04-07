Projeto desenvolvido em Python para coletar e processar dados de tempo de 20 atletas. O script realiza cálculos estatísticos e categoriza o desempenho individual com base na média do grupo.

## Funcionalidades
* **Melhor e Pior tempo**: Identificação dos extremos de performance.
* **Diferença de tempo**: Cálculo da amplitude entre o primeiro e o último colocado.
* **Média Geral**: Cálculo do tempo médio de todos os participantes.
* **Dispersão**: Quantidade de atletas que ficaram acima ou abaixo da média.
* **Identificação**: Número da camisa (posição) do melhor atleta.
* **Classificação**: Divisão em grupos de *Elite*, *Regular* e *Iniciante*.

## Funcionamento
O sistema opera através de uma interface de linha de comando seguindo este fluxo:

1. **Entrada de Dados**: O usuário deve inserir o tempo (em segundos) de 20 atletas individualmente.
2. **Cálculo de Métricas**: O script processa a média aritmética, identifica o menor tempo e o maior tempo.
3. **Análise Estatística**: O código calcula a dispersão dos atletas em relação à média e a diferença exata entre os extremos.
4. **Categorização**: Os atletas são agrupados utilizando um intervalo de tolerância de 10 segundos para mais ou para menos em relação à média.

## Instalação
Para executar este projeto, é necessário ter o **Python 3** instalado em seu sistema operacional.

1. Clone o repositório:
```bash
git clone https://github.com


Acesse o diretório do projeto:
cd nome-do-repositorio


Execute o script:
python nome_do_arquivo.py

Exemplo de Uso
Ao rodar o script, o sistema solicitará as entradas conforme o exemplo abaixo:
Entrada de dados:
Digite o tempo do atleta 1 (em segundos): 105.5
Digite o tempo do atleta 2 (em segundos): 120.0

Relatório de saída:
--- RESULTADOS ---
Tempo médio: 112.40 segundos
Atletas acima da média: 9
Atletas abaixo da média: 11
Melhor tempo: 98.0 segundos
Pior tempo: 130.0 segundos
Diferença entre melhor e pior: 32.0 segundos
Posição do melhor atleta: 7

Classificação:
Elite: 4
Regular: 10
Iniciante: 6

Requisitos Técnicos

Linguagem: Python 3.x
Ambiente: Terminal ou Prompt de Comando
Dependências: Nenhuma (Standard Library apenas)
'''
---


## Contribuidores

Este projeto foi desenvolvido pelos seguintes membros:

* **Kevin**
* **Marcos**
* **Pedro**
* **Ana**

