import requests
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.status import Status
from rich.table import Table

console = Console()

citi = ["Kyiv", "Odesa", "Kharkiv", "Lviv", "Dnipro", "Donetsk", "Zaporizhzhia"]

def show_weather_app():
    console.print(Panel("[bold cyan]METEO-SYSTEM v2.0[/bold cyan]\n[dim]Доступ к спутниковым данным разрешен[/dim]", expand=False))

    while True:
        # 1. Выбор города через Rich Prompt (он сам умеет проверять ввод!)
        user_citi = Prompt.ask(
            f"[yellow]Введите город[/yellow]", 
            choices=citi, 
            default="Odesa"
        )

        url = f"https://wttr.in/{user_citi}?format=%t|%C"
        try:
            with console.status("[bold green]Связь со спутником...[/bold green]"):
                response = requests.get(url, timeout=5)
                response.raise_for_status()
                

                temp, desc = response.text.split("|")
                
                res_table = Table(show_header=False, border_style="blue")
                res_table.add_row("[cyan]Локация:[/cyan]", f"[bold]{user_citi}[/bold]")
                res_table.add_row("[cyan]Температура:[/cyan]", f"[bold yellow]{temp}[/bold yellow]")
                res_table.add_row("[cyan]Состояние:[/cyan]", f"[bold white]{desc}[/bold white]")
                
                console.print(Panel(res_table, title="[bold green]ДАННЫЕ ПОЛУЧЕНЫ[/bold green]", expand=False))

        except Exception as e:
            console.print(f"[bold red]ОШИБКА СВЯЗИ:[/bold red] {e}")

        should_continue = Prompt.ask(
            "\n[bold magenta]Продолжить мониторинг?[/bold magenta]", 
            choices=["да", "нет"], 
            default="да"
        ) == "да"

        if not should_continue:
            console.print("[bold red]Отключение от системы...[/bold red]")
            break

if __name__ == "__main__":
    show_weather_app()