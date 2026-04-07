Projeto criado para receber 20 valores em forma de segundos de atletas que participaram da última corrida. Separar os dados em :
* Melhor tempo | Pior tempo
* Diferença entre o Melhor tempo e Pior tempo
* Tempo médio
* Quantidade de atletas acima da media e abaixo
* Número da camisa do melhor atleta
* Classificar em grupos de Elite, Regular e Iniciante.

Funcionamento
O sistema opera através de uma interface de linha de comando seguindo este fluxo:
Entrada de Dados: O usuário deve inserir o tempo (em segundos) de 20 atletas individualmente.
Cálculo de Métricas: O script processa a média aritmética, identifica o menor tempo (melhor performance) e o maior tempo (pior performance).
Análise Estatística: O código calcula a dispersão dos atletas em relação à média e a diferença exata entre o primeiro e o último colocado.
Categorização: Os atletas são agrupados em Elite, Regular ou Iniciante, utilizando um intervalo de tolerância de 10 segundos para mais ou para menos em relação à média do grupo.

Instalação
Para executar este projeto, é necessário ter o Python 3 instalado em seu sistema operacional.
Clone o repositório:
bash
git clone https://github.com

Use o código com cuidado.

Acesse o diretório do projeto:
bash
cd nome-do-repositorio


Execute o script:
bash
python nome_do_arquivo.py



Exemplo de Uso
Ao rodar o script, o sistema solicitará as entradas conforme o exemplo abaixo:
Entrada de dados:

text
Digite o tempo do atleta 1 (em segundos): 105.5
Digite o tempo do atleta 2 (em segundos): 120.0
...


Relatório de saída:

text
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
Python 3.x.
Ambiente de terminal ou prompt de comando.
Não requer dependências ou bibliotecas externas.
