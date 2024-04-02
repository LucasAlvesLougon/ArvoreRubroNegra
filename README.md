# Implementação de uma Árvore Rubro-Negra em Python

Este código implementa uma árvore Rubro-Negra (ArvoreRubroNegra) em Python. A árvore é usada para armazenar elementos ordenados de forma eficiente, permitindo a inserção, remoção e busca de elementos de forma eficiente.

## Estrutura do Código

O código é dividido em duas classes principais:

- `No`: representa um nó da árvore, contendo uma chave, uma cor e referências para o nó pai, filho esquerdo e filho direito.
- `ArvoreRubroNegra`: representa a árvore Rubro-Negra em si, contendo a raiz da árvore e métodos para inserir, remover e percorrer a árvore.

### Observações

- Crie uma venv - `py -m venv .venv`
- Ative a mesma para poder instalar as dependências do logger na venv - `.\.venv\Scripts\activate`.
- Execute o comando `pip install loguru` no terminal, após a instalação, o código estará printando normalmente o resultado das execuções.
os imports para o logger já estão sendo feitos