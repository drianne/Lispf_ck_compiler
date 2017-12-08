import ox
import click
from getch import getche

#making lexer
lexer = ox.make_lexer([
    ('NUMBER', r'\d+'),
    ('NAME', r'[-a-zA-Z]+'),
    ('COMMENT', r';.*'),
    ('NEWLINE', r'\n'),
    ('SPACE', r'\s+'),
    ('RIGHT', r'right'),
    ('LEFT', r'left'),
    ('INC', r'inc'),
    ('DEC', r'dec'),
    ('ADD',r'add'),
    ('SUB',r'sub'),
    ('PRINT', r'print'),
    ('READ', r'read'),
    ('DO',r'do'),
    ('LOOP', r'loop'),
    ('DEF', r'def'),
    ('PARENTHESIS_B', r'\('),
    ('PARENTHESIS_A', r'\)')
])

#Seting tokens
tokens = ['NUMBER','INC', 'DEC','SUB', 'ADD','RIGHT', 'LEFT','PRINT','DO','NAME','LOOP',
            'READ','DEF','PARENTHESIS_A','PARENTHESIS_B']

op = lambda op: (op)
operator = lambda type_op: (type_op)

#making parser
parser = ox.make_parser([
    ('program : PARENTHESIS_B expr PARENTHESIS_A', lambda x,y,z: y),
    ('program : PARENTHESIS_B PARENTHESIS_A', lambda x,y: '()'),
    ('expr : operator expr', lambda x,y: (x,) + y),
    ('expr : operator', lambda x: (x,)),
    ('operator : program', op),
    ('operator : LOOP', operator),
    ('operator : DO', operator),
    ('operator : RIGHT', operator),
    ('operator : LEFT', operator),
    ('operator : READ', operator),
    ('operator : INC', operator),
    ('operator : DEC', operator),
    ('operator : DEF', operator),
    ('operator : PRINT', operator),
    ('operator : ADD', operator),
    ('operator : SUB', operator),
    ('operator : NAME', operator),
    ('operator : NUMBER', operator),
], tokens)

#Enter the file
@click.command()
@click.argument('lispf_ck',type=click.File('r'))
@click.option('-o', nargs=1, type=click.File('w'))

#Constructor
def constructor(lispf_ck, o):
    #Reading the program
    source = lispf_ck.read()

    #Geting tokens of source code
    tokens = lexer(source)

    #Removing comments and spaces of tokens to make the tree
    parser_tokens = [token for token in tokens if token.type != 'COMMENT' and token.type != 'SPACE']

    #Generating tree
    tree = parser(parser_tokens)

    brain_code = ''
    brain_code = eval(tree, brain_code)

    o.write(brain_code)

dictionary = {}

#Defining main functions

def add(value, brain_code):
    for i in range(0,value):
        brain_code = brain_code + '+'
    return brain_code

def subtract(value, brain_code):
    for i in range(0,value):
        brain_code = brain_code + '-'
    return brain_code

def eval(ast, brain_code):

    #Running ast nodes
    for node in ast:

        #Defining actions to compiler

        if isinstance(node, tuple):
            brain_code = eval(node, brain_code)

        elif node == 'add':
            brain_code = add(int(ast[1]), brain_code)

        elif node == 'sub':
            brain_code = subtract(int(ast[1]), brain_code)

        elif node == 'inc':
            brain_code = brain_code + '+'

        elif node == 'dec':
            brain_code = brain_code + '-'

        elif node == 'right':
            brain_code = brain_code + '>'

        elif node == 'left':
            brain_code = brain_code + '<'

        elif node == 'print':
            brain_code = brain_code + '.'

        elif node == 'read':
            brain_code = brain_code + ','

        elif node == 'loop':
            brain_code = brain_code + '['
            brain_code = eval(ast[1:len(ast)], brain_code)
            brain_code = brain_code + ']'
            break

        elif node == 'do-after':
            i = 0
            while i < len(ast[2]):
                lis = ('do', ast[2][i], ast[1])
                brain_code = eval(lis, brain_code)
                i = i + 1
            break

        elif node == 'do-before':
            i = 0
            while i < len(ast[2]):
                lis = ('do', ast[1], ast[2][i])
                brain_code = eval(lis, brain_code)
                i = i + 1
            break

        elif node == 'def':
            dictionary[ast[1]] = (ast[2], ast[3])

        elif node in dictionary:
            lis = dictionary[node][1]
            brain_code = eval(lis, brain_code)

    return brain_code

if __name__ == '__main__':
   constructor()
