import json
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from core.guardian import verification

console = Console()


if not verification:
    console.print("[bold red]⚠ ОБНАРУЖЕН ХАКЕР![/bold red] Данные дезинформированы. Логи в 'vault'.")

console.print(Panel.fit("🛡 PHANTOM GUARD - ADMIN PANEL v1.0", style="bold cyan"))

while True:
    try:
        level_input = console.input("[bold yellow]Введите уровень доступа (1, 2, 3): [/bold yellow]")
        level = int(level_input)
        if level in [1, 2, 3]:
            break
        console.print("[red]Ошибка: Введите числа 1-3![/red]")
    except ValueError:
        console.print("[red]Ошибка: Нужно ввести цифру![/red]")

# 4. Загрузка и вывод данных из users.json
try:
    with open("vault/users.json", "r", encoding="utf-8") as f:
        users = json.load(f)

    # Создаем таблицу через rich
    table = Table(title="Список пользователей системы", style="magenta")

    table.add_column("Логин", style="cyan", no_wrap=True)
    table.add_column("Пароль", style="green")
    table.add_column("Уровень", style="bold white")

    for username, info in users.items():
        # Достаем уровень, если его нет (как у admin), ставим "N/A" или 3
        u_level = str(info.get("level", "3 (Root)"))
        u_password = info.get("password")
        
        # Добавляем строку в таблицу
        table.add_row(username, u_password, u_level)

    console.print(table)

except FileNotFoundError:
    console.print("[bold red]Ошибка: Файл vault/users.json не найден![/bold red]")