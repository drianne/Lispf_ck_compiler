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

#Defining tape of lispf_ck and necessary pointers
tape = [0]
ptr = 0
breakpoints = []

#Enter the file
@click.command()
@click.argument('program', type=click.File('r'))

#Constructor
def constructor(program):
    #Reading the program
    source = program.read()

    print("\nSource Code : ")
    print(source)

    #Geting tokens of source code
    tokens = lexer(source)
    print("\nTokens:\n ")
    print(tokens)

    #Removing comments and spaces of tokens to make the tree
    parser_tokens = [token for token in tokens if token.type != 'COMMENT' and token.type != 'SPACE']

    #Generating tree
    tree = parser(parser_tokens)
    print("\nTree : \n")
    print(tree)

    #printing result of interpretation
    print("\n\nResult: \n")
    value = eval(tree, ptr)

    print(value)

dictionary = {}

def eval(ast, ptr):

    #Running ast nodes
    for node in ast:
        #Defining actions in tape
        if node[0] == 'add':
            tape[ptr] = (tape[ptr] + int(node[1])) % 256
        elif node[0] == 'sub':
            tape[ptr] = (tape[ptr] - int(node[1])) % 256
        elif node == 'inc':
            tape[ptr] = (tape[ptr] + 1) % 256
        elif node == 'dec':
            tape[ptr] = (tape[ptr] - 1) % 256
        elif node == 'right':
            ptr += 1
            if ptr == len(tape):
                tape.append(0)
        elif node == 'left':
            ptr -= 1
        elif node == 'print':
            print(chr(tape[ptr]), end='')
        elif node == 'read':
            tape[ptr] = ord(getche())
        elif node[0] == 'loop':
            if tape[ptr]!= 0:
                i = 1
                while i < len(node):
                    eval(node,ptr)
                    i = i + 1
                    if tape[ptr] == 0:
                        break
        elif node[0] == 'do-after':
            _,cmd,command_list = node
            expansion = ['do']
            for command in command_list:
                expansion.extend([command, cmd])
            eval(tuple(expansion), ptr)
        elif node[0] == 'do-before':
            _,cmd,command_list = node
            expansion = ['do']
            for command in command_list:
                expansion.extend([cmd, command])
            eval(tuple(expansion), ptr)

if __name__ == '__main__':
   constructor()
