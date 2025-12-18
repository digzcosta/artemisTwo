import typer
from rich import print
from typing_extensions import Annotated
from src.api.adzuna_client import search_jobs
from src.logger import log
from src.services.job_mapper import cleaning_dict_jobs
from src.services.job_service import save_job

app = typer.Typer()

@app.command(help="Fetch job listings using a search term.")
def fetch(term: Annotated[str, typer.Argument()] = ""):
    
    term = term.strip()

    if not term:
        print("[bold red]Please provide a job title or keyword.[/bold red]")
        raise typer.Exit(code=1)
    
    if len(term) < 2:
        print("[bold red]Keyword must have at least 2 characters.[/bold red]")
        raise typer.Exit(code=1)
    
     
    print(f'[bold]Searching for "[bold green]{term}[/bold green]"...[/bold]')
    log.info("CLI fetch started with term={}", term)

    data = search_jobs(term)

    if not data:
        print("[bold red]API request failed or returned no data.[/bold red]")
        return

    count = data.get("count", 0)
    print(f"[cyan]Found {count} jobs.[/cyan]")

    results = data.get("results", [])
    
    saved = 0
    ignored = 0

    for job_json in results:
        cleaned = cleaning_dict_jobs(job_json)
        if save_job(cleaned):
            saved += 1
        else:
            ignored += 1

    print(f"[green]Saved jobs:[/green] {saved}")
    print(f"[yellow]Ignored duplicates:[/yellow] {ignored}")


@app.command(help="Display saved jobs (Mark 2 feature).")
def show():
    print("[bold yellow]Showing saved jobs...[/bold yellow]")
    print("[italic]→ Feature coming in Mark 2.[/italic]")
    

if __name__ == "__main__":
   app()


