# League of Labyrinths

O projeto da displina EDL - consiste em criar um labirinto com interface gráfica, utilizar estrutura de dados stack e o algoritmo backtracking para resolver o labirinto.🐀🧀

## Requisitos do projeto:
- O labirinto é denominado por 1 = paredes, 0 = caminhos, M = Twitch(Inicio) e E = Lulu(saída)
- O M(Twitch) deve percorrer todos os caminhos possivéis no labirinto
- Marcar as posições visitadas
- Pintar o caminho visitado de **vermelho** e o caminho correto de **verde**
- Mostrar as duas pilhas de caminhos visitados e caminho correto.

## Executar

1. Crie um ambiente virtual e ative
   ```bash
   python -m venv venv
   source venv/Scripts/activate
   ```

3. Instale as dependências necessárias executando:

    ```bash
    pip install -r requirements.txt
    ```

4. Execute o programa:

    ```bash
    python main.py
    ```

## Estrutura de Arquivos

- **assets**: Contém imagens e arquivos de som usados no programa.
- **functions**: Inclui módulos para carregar o labirinto e encontrar as posições do Twitch e Lulu.
- **settings.py**: Contém constantes de configurações

## Passo a Passo
- 1 - A biblioteca Pygame é inicializada.
- 2 - A imagens e arquivos são carregados pelo Pygame.
- 3 - A função **load_maze** é chamada para ler as linhas do arquivo.txt que contém as dimensões e coordenadas do labirinto.
- 4 - Após a função **draw_maze** é chamada para desenhar o labirinto de acordo com os dados armazenados.
- 5 - O algoritmo Backtracking é implementado para solucionar o labirinto

