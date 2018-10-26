from RBTreeNode import RBTreeNode

BLACK = True
RED   = False


class RBTree:

    def __init__(self):
        self.root = None


    def __str__(self):
        return self.printNode(self.root)

    def printNode(self, node):
        return self.printNode(node.left) + '\n' + str(node) + self.printNode(node.right)
        
        
    def insert(self, node, item, key):
        
        # se a arvore não estiver vazia #
        if self.root is None:
            
            # se tiver filho direito #
            if node.right != None:
                
                # compara o valor das chaves #
                if key >= node.item.key:
                    self.insert(node.right, item, key)

            # se tiver filho esquerdo #
            elif node.left != None:
                
                # compara o valor das chaves #
                if key < node.item.key:
                    self.insert(node.right, item, key)
            
            # se for folha #
            else:
                
                # cria um novo nó #
                newNode = RBTreeNode(item, parent=node)

                # define se é filho direito ou esquerdo #
                if key >= node.item.key:
                    node.right = newNode
                else:
                    node.left = newNode

        # se a arvore estiver vazia #
        else:
                # cria um novo nó #
                newNode = RBTreeNode(item, parent=None)

                self.root = newNode

        self.corrigir(newNode)
        

    def corrigir(self, node):
        # caso 1 #
        if node.parent is None:
            node.color = BLACK
        
        # caso 2 #
        else:
            if node.tio() != None and node.tio().color == RED:
                node.recolorir()
                node.avo().recolorir()
                node.tio().recolorir()
            
            # caso 3 #
            else:

                # subcaso 1 #
                if node.avo().left == node.parent:
                    if node == node.parent.left:
                        node.parent.rotacaoDireita()

