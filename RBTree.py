from RBTreeNode import RBTreeNode

BLACK = True
RED   = False

class RBTree:

    def __init__(self):
        self.root = None


    def __str__(self):
        return self.printTree(self.root)

    def printTree(self, node):
        str = ''
        if node.left is not None:
            str += self.printTree(node.left)

        str += node.__str__() + '\n'

        if node.right is not None:
            str += self.printTree(node.right)
        
        return str
        
        
    def insert(self, item, key, node=None):
        if node is None:
            node = self.root
            
        # se a arvore não estiver vazia #
        if node is not None:
            
            # se tiver filho direito #
            if node.right != None:
                
                # compara o valor das chaves #
                if key >= node.key:
                    self.insert(item, key, node.right)

            # se tiver filho esquerdo #
            if node.left != None:
                
                # compara o valor das chaves #
                if key < node.key:
                    self.insert(item, key, node.left)
            
            # se for folha #
            if node.left is None and node.right is None:
                
                # cria um novo nó #
                newNode = RBTreeNode(item, key, parent=node)

                # define se é filho direito ou esquerdo #
                if key >= node.key:
                    node.right = newNode
                else:
                    node.left = newNode

                self.corrigir(newNode)

        # se a arvore estiver vazia #
        else:
                # cria um novo nó #
                newNode = RBTreeNode(item, key, parent=None)

                self.root = newNode

                self.corrigir(newNode)
        

    def corrigir(self, node):
        # caso 1 #
        if node.parent is None:
            node.color = BLACK
        
        # caso 2 #
        else:
            avo = node.avo()
            tio = node.tio()
            pai = node.parent

            if tio != None and tio.color == RED:
                node.recolorir()
                avo.recolorir()
                tio.recolorir()
            
            # caso 3 #
            else:

                # subcaso 1 #
                
                # Caso o nó inserido seja filho esquerdo e o pai do nó também seja filho esquerdo
                
                if avo is not None:
                    if avo.left == pai and node == pai.left:
                        
                        # se a cor do avô for preto e do pai for vermelho
                        if avo.color == BLACK and pai.color == RED:
                            
                            # recolore o pai e o avô
                            pai.recolorir()
                            avo.recolorir()

                            # faz-se uma rotação a direita
                            if avo.parent is not None:
                                if avo.parent.left == avo:
                                    avo.parent.left = pai.rotacaoDireita()
                                else:
                                    avo.parent.right = pai.rotacaoDireita()
                            else:
                                self.root = pai.rotacaoEsquerda()
                            

                    # subcaso 2 #

                    # Caso o nó inserido seja filho direito e o pai do nó também seja filho direito
                    elif avo.right == pai and node == pai.right:
                        
                        # se a cor do avô for preto e do pai for vermelho
                        if avo.color == BLACK and pai.color == RED:
                            
                            # recolore o pai e o avô
                            pai.recolorir()
                            avo.recolorir()

                            # faz-se uma rotação a esquerda
                            if avo.parent is not None:
                                if avo.parent.left == avo:
                                    avo.parent.left = pai.rotacaoEsquerda()
                                else:
                                    avo.parent.right = pai.rotacaoEsquerda()
                            else:
                                self.root = pai.rotacaoEsquerda()

                    # subcaso 3 #

                    # Caso o nó inserido seja filho esquedro e o pai seja filho direito   
                    elif avo.right == pai and node == pai.left:

                        # se a cor do avô for preto e do pai for vermelho
                        if avo.color == BLACK and pai.color == RED:
                            
                            # recolore o pai e o avô
                            pai.recolorir()
                            avo.recolorir()

                            # realiza-se uma rotação simples a direita
                            avo.right = node.rotacaoDireita()

                            if avo.parent is not None:
                                if avo.parent.left == avo:
                                    avo.parent.left = pai.rotacaoEsquerda()
                                else:
                                    avo.parent.right = pai.rotacaoEsquerda()
                            else:
                                self.root = pai.rotacaoEsquerda()

                    # subcaso 4 #

                    # Caso o nó inserido seja filho esquedro e o pai seja filho direito   
                    elif avo.left == pai and node == pai.right:

                        # se a cor do avô for preto e do pai for vermelho
                        if avo.color == BLACK and pai.color == RED:
                            
                            # recolore o pai e o avô
                            pai.recolorir()
                            avo.recolorir()

                            # realiza-se uma rotação simples a esqueda
                            avo.left = node.rotacaoEsquerda()

                            if avo.parent is not None:
                                if avo.parent.left == avo:
                                    avo.parent.left = pai.rotacaoDireita()
                                else:
                                    avo.parent.right = pai.rotacaoDireita()
                            else:
                                self.root = pai.rotacaoDireita()