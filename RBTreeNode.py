from RBTree import RBTree

BLACK = True
RED   = False

class RBTreeNode:

    # construtor do nó #
    def __init__(self, item, parent, left=None, right=None):
        self.parent = parent
        self.left = left
        self.right = right
        self.color = False
        self.item = item

    # representação do nó como uma string #
    def __str__(self):
        if self.color == True:
            return str(self.item) + '\tBLACK'
        else:
            return str(self.item) + '\tRED'


    # retorna o avo do nó #
    def avo(self):
        if self.parent != None:
            return self.parent.parent
        return None

    # retorna o tio do nó #
    def tio(self):
        # se o avo existir #
        if self.avo() != None:

            # se o pai for filho esquerdo #
            if self.avo().left == self.parent:
                
                # retorna o filho direito #
                return self.avo().right 

            # se o pai for o filho direito #
            elif self.avo().right == self.parent:

                # retorna o filho esquerdo #
                return self.avo().left
        
        
        return None


    # método resposável por recolorir o nó #
    def recolorir(self):
        if self.color == RED:
            self.color = BLACK
        else:
            self.color = RED

    def rotacaoDireita(self):
        self.parent.right = self.left
        
        if self.left is not None:
            self.left.parent = self.parent
        
        self.left = self.parent
        self.parent = self.left.parent
        self.left.parent = self
        
        return self

    def rotacaoEsquerda(self):
        self.parent.left = self.right
        
        if self.right is not None:
            self.right.parent = self.parent
        
        self.right = self.parent
        self.parent = self.right.parent
        self.right.parent = self

        return self