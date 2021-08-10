import matplotlib
from pathlib import Path
import matplotlib.pyplot as plt
import click
from colorama import init
from termcolor import colored
from pyfiglet import Figlet


class board():

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.state = []
        for n in range(y):
            self.state.append([0 for z in range(x)])

    def seed_cell(self, x, y):
        self.state[y][x] = 1

    def kill_cell(self, x, y):
        self.state[y][x] = 0


class universe():

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.data = board(x, y)
        self.gen = 0
        self.pop = 0

    def load_pattern(self, pattern):
        for point in pattern:
            if point != ():
                self.data.seed_cell(*point)

    def next(self):
        self.gen += 1
        new = board(self.x, self.y)

        for n in range(self.x):
            self.data.kill_cell(n, 0)
            self.data.kill_cell(n, self.y-1)
        for n in range(new.y):
            self.data.kill_cell(0, n)
            self.data.kill_cell(self.x-1, n)

        for j in range(1, new.y-1):
            for i in range(1, new.x-1):
                neighbours = []
                for l in range(-1, 2):
                    for k in range(-1, 2):
                        neighbours.append(self.data.state[i+k][j+l])
                if sum(neighbours) < 2 or sum(neighbours) > 3:
                    new.kill_cell(i, j)
                elif sum(neighbours) == 3 or sum(neighbours) == 2:
                    new.seed_cell(i, j)

        self.data = new
        plt.imshow(self.data.state, cmap='summer')
        plt.savefig(f'{self.gen}.png', bbox_inches='tight')


@click.group(
	invoke_without_command=True,
)
@click.pass_context
def cli(ctx):
	'''
	Generate patterns with modified Game of Life rules.
	'''
	if ctx.invoked_subcommand is None:
		fig = Figlet(font="slant")
		click.echo(colored(fig.renderText("shrigma"), "red", attrs=["bold"]))
		click.echo("shrigma v0.1.0\nGenerate patterns with modified Game of Life rules")
	else:
		pass


@cli.command()
@click.argument("X", type=click.INT)
@click.argument("Y", type=click.INT)
@click.option("-g", "--generations", type=click.INT, help="Generations to run")
@click.option("-p", "--pattern", type=Path, help="Initial pattern file")
@click.option("-o", "--output", help="Output image folder")
# @click.option("-a", "--animate", is_flag=True, help="Generate a gif")
def generate(x,y,pattern,output,generations):
    '''
    Run a simulation for a certain number of generations.

    \b
    X is the width of the board
    Y is the height of the board

    The initial pattern can be read from a file
    with the pattern option otherwise a prompt
    will be given.
    '''
    pat = []
    if not pattern:
        for num in range(10):
            point = click.prompt(colored(">>", "yellow"),prompt_suffix="")
            if point == "q":
                break
            pat.append(tuple([int(num.rstrip()) if num != "" else 0 for num in point.split(",") if len(point.split(",")) == 2]))
    else:
        with open(pattern) as f:
            for line in f.readlines():
                if "#" not in line:
                    pat.append(tuple([int(num.rstrip()) if num != "" else 0 for num in line.split(",") if len(line.split(",")) == 2]))
    click.echo(f"""
    Dimensions:  X = {x}
                 Y = {y}

    Generations: {generations if generations else "CONTINUOUS"}
               """)
    field = universe(x,y)
    field.load_pattern(pat)
    if not generations:
        while True:
            # check = click.prompt(colored(f"{field.gen}?", "blue"),prompt_suffix="")
            check = input(colored(f"{field.gen}?", "blue"))
            if check == "q":
                quit()
            field.next()
    else:
        with click.progressbar(range(generations)) as bar:
            for x in bar:
                field.next()


if __name__ == "__main__":
    cli()
