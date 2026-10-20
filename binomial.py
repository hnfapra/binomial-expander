import math
from fractions import Fraction
from rich.console import Console, Group
from rich.panel import Panel
from rich.align import Align

console = Console()

def expand (n, term, b):
    r = 0
    coefficient = 1.0
    coefficients = [coefficient]
    
    for i in range(term-1):
        coefficient *= (n-r)/(r+1)*b
        coefficients.append(coefficient)
        r = r + 1
        
    return coefficients
        

def convertfrac (decimals):
    answers = []
    for number in decimals:
        frac = Fraction(number).limit_denominator()
        if frac.denominator == 1:
            stringres = f"{frac.numerator}"
        else:
            stringres = f"{frac.numerator}/{frac.denominator}"
        answers.append(stringres)
        # print(f"{result.numerator}/{result.denominator}")
    return answers

def format_expansion(coefficients):
    terms = []
    for power, coefficient in enumerate(coefficients):
        if power == 0:
            terms.append('[bold yellow]1[/bold yellow]')
        elif power == 1:
            terms.append(f"[bold yellow]{coefficient}[/bold yellow]x")
        else:
            terms.append(f"[bold yellow]{coefficient}[/bold yellow]x^{power}")
    return ' + '.join(terms)

def binExpand(power, term, coef):
    return format_expansion(convertfrac(expand(power, term, coef)))

def main():
    
    console.print(
        Align.center(
            
        Panel(
            Group(     
            Align.center(
                "Welcome to Binomial Expansion Calculator!"
            ),
            Align.center(
                Panel(  
                "(1+[bold cyan]k[/bold cyan]x)^[bold red]n[/bold red]", 
                padding=(1,8),
                )
            ),
            ),
            
        width=console.width-50
        )
        )
    )

    console.print(
        Align.center(
                Panel(
                    Group(     
                            Align.center(
                                "How many [bold yellow] terms [/bold yellow] do you want? "
                            ),
                            Align.center( 
                                "What is the [bold cyan]coefficient[/bold cyan] of x? ", 
                            ),
                            Align.center(
                                "How many[bold red] power[/bold red] the binomial expression raised? ", 
                            ),
                            ),
                    title="Input",
                    padding=(1,2),
                    width=console.width-50
                )
        )
    )

    term = int(console.input("[bold cyan]term > [/bold cyan]"))
    k = float(console.input("[bold cyan]k > [/bold cyan]"))
    n = float((console.input("[bold cyan]n > [/bold cyan]")))



    console.print(
        Align.center(
                    Panel(
                        Group(     
                                Align.center(
                                    binExpand(n, term, k)
                                ),
                                ),
                        title="Expanded Form",
                        padding=(1,2),
                        width=console.width-50
                )
        )
    )


if __name__ == "__main__":
    main()