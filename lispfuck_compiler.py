import click

@click.command()
@click.argument('lispf_ck',type=click.File('r'))
@click.option('-o', nargs=1, type=click.File('w'))

def cGenerator(lispf_ck, o):

    # Dicionário analisador entre lispf_ck e brainf_ck

    parseDictionary = { "right" : ">",
	            "left" : "<",
	            "inc" : "+",
	            "dec" : "-",
	            "print" : ".",
	            "read" : ",",
	            "(loop" : "[",
	            "(" : "]" }

    # Convertendo de lispfuk para brainfuck
    brainfuck_file = """ """
    print(brainfuck_file)


if __name__ == "__main__":
    cGenerator()
