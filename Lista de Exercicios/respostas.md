1. d

2. a

3. d

4. a

5. e

6. b

7. e

8. c

9. b

10. d

11. a

12. d

13. e

14. b

15. Uma árvore enraizada T, ou simplesmente árvore, é um conjunto finito de elementos denominados nós ou vértices
tais que T = Ø, e a árvore é dita vazia, ou existe um nó especial chamado raiz de T(r(T)); os restantes constituem um único conjunto vazio ou são divididos em m ≥ 1 conjuntos disjuntos não vazios, as subárvores de r(T), ou simplesmente subárvores, cada qual, por sua vez, uma árvore.

- Raiz: O nó superior da árvore.
- Nós: Elementos da árvore que contêm dados.
- Filhos: Nós que descendem de um nó específico.
- Folhas: Nós que não têm filhos.

16. 
- Grau de uma árvore: O grau de um nó é o número de filhos que ele tem. Por exemplo, se um nó tem dois filhos, seu grau é 2.
- Altura de uma árvore: A altura de uma árvore é a distância máxima da raiz até uma folha. Por exemplo, em uma árvore com raiz R e três níveis, a altura é 3.

17. 
- Árvores Binárias: Cada nó tem no máximo dois filhos.
- Árvores de Busca Binária: Cada nó segue a propriedade de que o filho à esquerda é menor e o filho à direita é maior que o nó pai.
- Árvores AVL: Uma árvore de busca binária balanceada onde a diferença de altura entre as subárvores esquerda e direita de qualquer nó não é mais que 1.

18. 
- Exemplo 1: Sistemas de arquivos em sistemas operacionais, onde diretórios e subdiretórios são representados como uma árvore.
- Exemplo 2: Estruturas de organização empresarial, onde cada funcionário é um nó e os subordinados diretos são filhos do nó.

19. 
- Pré-ordem (preorder): root => esquerda => direita
- Em-ordem (inorder): esquerda => root => direita
- Pós-ordem (postorder): esquerda => direita => root

20. 

```py
def in_order(root):
    if root:
        return self.in_order(root.left) + [root.value] + self.in_order(root.right)
    else:
        return []

def pre_order(root):
    if root:
        return [root.value] + self.pre_order(root.left) + self.pre_order(root.right)
    else:
        return []

def post_order(root):
    if root:
        return self.post_order(root.left) + self.post_order(root.right) + [root.value]
    else:
        return []
```

21. Os percursos em árvores podem ser usados para resolver problemas como a impressão dos nós em uma ordem específica, a avaliação de expressões aritméticas, e a geração de código de compiladores.

22. Uma árvore AVL é uma árvore de busca binária auto-balanceada, onde a diferença de altura entre as subárvores esquerda e direita de qualquer nó é no máximo 1.

23. O balanceamento é a diferença do grau do nó máximo da arvore da direta com a esquerda. Para estar balanceado é necessário que o resultado seja um desses valores: -1, 0, 1.

24. 
- Rotação à direita: Usada quando a subárvore esquerda de um nó está desbalanceada.
- Rotação à esquerda: Usada quando a subárvore direita de um nó está desbalanceada.
- Rotação dupla à direita: Usada quando a subárvore esquerda do filho direito de um nó está desbalanceada.
- Rotação dupla à esquerda: Usada quando a subárvore direita do filho esquerdo de um nó está desbalanceada.

25. 
- Sistemas de bancos de dados para manter índices balanceados; 
- Implementação de dicionários e conjuntos em bibliotecas de programação que exigem operações rápidas de pesquisa, inserção e deleção; 
- Sistema de arquivos; 
- Sistema de roteamento e aplicação de redes

26. Estruturas de dados chave-valor são coleções de pares chave-valor, onde cada chave única mapeia para um valor. Elas se diferenciam de listas e tuplas por permitir acesso eficiente aos valores com base em suas chaves.

27. Uma estrutura chave-valor armazena dados em pares, onde uma chave é usada para identificar e acessar o valor correspondente de forma eficiente.

28. A principal diferença é que o JSON apenas aceita os tipos de dados string; número; objeto; array; booleano; null.

29. Grafos são estruturas de dados usadas para representar relações entre pares de objetos. Eles podem ser usados para modelar redes de transporte, redes sociais, sistemas de recomendação, entre outros.

30. 
- **shortest path:** 
    - Achar o caminho mais curto entre dois nodes.
    - Pode ser usado para definir caminhos no gps
    - Complexidade temporal de Dijkstra: O((V+E)logV)
    - O algoritmo de Bellman-Ford é O(VE)
    - Complexidade espacial: O(V) para armazenar os vértices e O(E) para armazenar as arestas, onde V é o número de vértices e E o número de arestas no grafo.
- **CPP:**
- Encontrar o caminho que visita cada aresta de um grafo (ou pelo menos uma vez em grafos não direcionados) exatamente uma vez e retorna ao ponto de partida, minimizando a distância total percorrida.
- Complexidade Temporal: O algoritmo hierholzer para grafos eulerianos é linear, O(E).
Para grafos não eulerianos, o algoritmo tem complexidade O(E logV).
Complexidade Espacial: O(V+E) para armazenar vértices e arestas.
- **TSP:**
    - Encontrar o ciclo hamiltoniano de menor custo em um grafo completo, onde cada vértice é visitado exatamente uma vez e o ciclo retorna ao vértice de partida.
    - Complexidade Temporal: complexidade exponencial O(n!), onde nnn é o número de vértices.
    - Complexidade Espacial: A complexidade espacial depende do algoritmo usado, variando de O(n2) a O(n!)