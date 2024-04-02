from loguru import logger

# Defina as cores para os nós
PRETO = True
VERMELHO = False

# Defina o nó para a Árvore Rubro-Negra
class No:
    def __init__(self, chave, cor=PRETO, pai=None):
        self.chave = chave
        self.cor = cor
        self.esquerda = None
        self.direita = None
        self.pai = pai

# Defina a Árvore Rubro-Negra
class ArvoreRubroNegra:
    def __init__(self):
        self.raiz = None

    # Função auxiliar para girar à esquerda
    def girar_esquerda(self, no):
        y = no.direita
        no.direita = y.esquerda
        if y.esquerda is not None:
            y.esquerda.pai = no
        y.pai = no.pai
        if no.pai is None:
            self.raiz = y
        elif no == no.pai.esquerda:
            no.pai.esquerda = y
        else:
            no.pai.direita = y
        y.esquerda = no
        no.pai = y

    # Função auxiliar para girar à direita
    def girar_direita(self, no):
        y = no.esquerda
        no.esquerda = y.direita
        if y.direita is not None:
            y.direita.pai = no
        y.pai = no.pai
        if no.pai is None:
            self.raiz = y
        elif no == no.pai.esquerda:
            no.pai.esquerda = y
        else:
            no.pai.direita = y
        y.direita = no
        no.pai = y

    # Função auxiliar para corrigir a cor após a inserção
    def corrigir_insercao(self, no):
        while no.pai.cor == VERMELHO:
            if no.pai == no.pai.pai.esquerda:
                if no.pai.pai.direita.cor == VERMELHO:
                    no.pai.cor = PRETO
                    no.pai.pai.direita.cor = PRETO
                    no.pai.pai.cor = VERMELHO
                    no = no.pai.pai
                else:
                    if no == no.pai.direita:
                        no = no.pai
                        self.girar_esquerda(no)
                    no.pai.cor = PRETO
                    no.pai.pai.cor = VERMELHO
                    self.girar_direita(no.pai.pai)
            else:
                if no.pai.pai.esquerda.cor == VERMELHO:
                    no.pai.cor = PRETO
                    no.pai.pai.esquerda.cor = PRETO
                    no.pai.pai.cor = VERMELHO
                    no = no.pai.pai
                else:
                    if no == no.pai.esquerda:
                        no = no.pai
                        self.girar_direita(no)
                    no.pai.cor = PRETO
                    no.pai.pai.cor = VERMELHO
                    self.girar_esquerda(no.pai.pai)
        self.raiz.cor = PRETO

    # Função para inserir um nó
    def inserir(self, chave):
        no = No(chave)
        if self.raiz is None:
            self.raiz = no
            no.cor = PRETO
        else:
            self._inserir_auxiliar(self.raiz, no)
            self.corrigir_insercao(no)  # Chamada corrigida para fix_insert após a inserção

    # Função auxiliar para inserir um nó
    def _inserir_auxiliar(self, raiz, no):
        if raiz is None:
            return no
        if no.chave < raiz.chave:
            raiz.esquerda = self._inserir_auxiliar(raiz.esquerda, no)
            if raiz.esquerda:
                raiz.esquerda.pai = raiz
        else:
            raiz.direita = self._inserir_auxiliar(raiz.direita, no)
            if raiz.direita:
                raiz.direita.pai = raiz
        return raiz

    # Função para imprimir a Árvore Rubro-Negra em ordem
    def imprimir_arvore(self):
        self._imprimir_arvore_auxiliar(self.raiz)

    # Função para imprimir a Árvore Rubro-Negra auxiliar
    def _imprimir_arvore_auxiliar(self, no):
        if no is not None:
            self._imprimir_arvore_auxiliar(no.esquerda)
            cor = 'Vermelho' if no.cor == VERMELHO else 'Preto'  # Verifica a cor do nó
            logger.info(f"Chave: {no.chave}, Cor: {cor}")
            self._imprimir_arvore_auxiliar(no.direita)

# Crie uma Árvore Rubro-Negra e insira elementos
arvore_rubro_negra = ArvoreRubroNegra()
arvore_rubro_negra.inserir(10)
arvore_rubro_negra.inserir(20)
arvore_rubro_negra.inserir(30)

# Chame o método imprimir_arvore na Árvore Rubro-Negra
arvore_rubro_negra.imprimir_arvore()
