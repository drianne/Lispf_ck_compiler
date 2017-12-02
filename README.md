<h1>Lispf_ck Compiler</h4> <br>
<p align="center">    
    <img src="http://i66.tinypic.com/72zho7.jpg" width=130 height=130>
</p>

## Contribuidores
| Nome	| Matrícula	|
|--|--|
| Adrianne Alves da Silva | 16/0047595 |
| Letícia de Souza | 15/0015160 |


## Apresentação

Este repositório apresenta um compilador para a linguagem lispf_ck que gera código brainf_ck, escrito em linguagem python, correpondente a uma atividade apresentada como avaliação parcial da disciplina de Compiladores do curso de Engenharia de software da Universidade de Brasília (UnB), Campus de Engenharias - Faculdade do Gama (FGA).

## Sobre a Linguagem

Lisp é uma linguagem de programação formal, matemática, que foi projetada a fim de realizar processamento de dados simbólicos. A representação do código se dá como lista, de maneira que os elementos são separados por espaços através de uma notação prefixa, em que o primeiro elemento representa uma função e os demais são argumentos da mesma. Essa linguagem foi utilizada por um tempo pela comunidade de inteligência artificial. Entretanto, nesse repositório será desenvolvido um parser para a linguagem Lispf_ck, uma variante da linguagem brainf_ck que combina a semântica do brainfuck com outros recursos.

De maneira simplista, a Lispf_ck é o mesmo que a brainf_ck em termos de limitações, mas em uma notação diferente. Ex:

BrainFuck : ,+[.-]

Lispf_ck: (do read inc (loop print dec))


### Caracteres

Como é uma linguagem diretamente relacionada com brainf_ck, podemos utilizar o alfabeto de brainfuck para demonstrar o de Lispf_ck. Tal que, temos em brainf_ck:

| Caractere | Significado  |
|---|---|
| > | Incremento do ponteiro  |
| < | Decremento do pronteiro  |
| + | Incremento do byte |
| - | Decremento do byte |
| . | Imprimir o dado |
| , | Entrada de um byte |
| [ | Início de um Laço |
| ] | Fim de um laço de repetição |

E em Lispf_ck teriamos:

| brainfuck | Lispfuck  |
|---|---|
| [...] | (loop ...)  |
| > | right |
| < | left |
| + |  inc |
| - | dec |
| . | print |
| , | read |

Em posse dessas informações, é possível perceber a semelhança entre as linguagens, tornando mais simples o processo de criação do compilador.

## Como Contribuir

Para contribuir com o desenvolvimento, é preciso que o colaborador crie o seu próprio Fork e envie um pull request com a contribuição para a branch master do projeto. As alterações serão analisadas e incorporadas ao compilador em caso de aprovação.
