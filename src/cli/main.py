import typer
from rich import print
from typing_extensions import Annotated

app = typer.Typer()

@app.command(help="Utilize esse comando para buscar vagas informando palavra-chave")
def fetch(term: Annotated[str, typer.Argument()] = ""):
    term = term.strip()

    if not term:
        print("[bold red]Por favor, digite um cargo/palavra chave para seguir.[/bold red]")
        raise typer.Exit(code=1)
    
    if len(term) < 2:
        print("[bold red]A palavra chave/cargo deve ter pelo menos 2 caracteres.[/bold red]")
        raise typer.Exit(code=1)
    
     
    print(f'[bold]Buscando por "[bold green]{term}[/bold green]" na base de dados...[/bold]')
    print('[yellow](DEBUG) API será chamada aqui depois. [/yellow]')


@app.command(help="Utilize esse comando para exibir as informações das vagas salvas.")
def show():
    print("[bold yellow]Exibindo vagas salvas na base de dados...[/bold yellow]")
    print("[italic]→ (DEBUG) Implementação completa virá na Mark 2.[/italic]")
    

if __name__ == "__main__":
   app()


# [] Adicionar descrição no HELP para descrever os comandos
