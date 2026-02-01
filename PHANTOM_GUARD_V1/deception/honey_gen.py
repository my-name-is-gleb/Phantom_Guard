from mimesis import Person, Internet
from rich.console import Console
from rich.table import Table
from core.guardian import log_event

console = Console()
person = Person("ru")
net = Internet()

def get_detailed_user():
    """Генерирует полную карточку пользователя"""
    return {
        "name": person.full_name(),
        "password": person.password(length=10),
        "phone": person.phone_number(),
        "email": person.email(),
        "ip": net.ip_v4()
    }

def face_admin():
    log_event("Наченаем поток диз-инфы")
    console.print("[bold yellow]Здравствуйте, админ![/bold yellow]\n")

    # Проходим по 3 уровням доступа
    for level in range(1, 4):
        table = Table(title=f"Уровень доступа: {level}", style="cyan", header_style="bold magenta")
        
        # Заголовки таблицы
        table.add_column("Тип", style="dim", width=12)
        table.add_column("Данные пользователя", style="white")

        # 1. Генерируем 2 детальных пользователей
        for _ in range(2):
            u = get_detailed_user()
            info = f"ФИО: {u['name']} | Pass: {u['password']} | IP: {u['ip']}\nEmail: {u['email']} | Тел: {u['phone']}"
            table.add_row("ПОЛНЫЙ ДОСТУП", info)
            table.add_section() # Разделительная линия

        # 2. Генерируем 3 пользователей только с именами
        for _ in range(3):
            table.add_row("ОГРАНИЧЕН", f"Имя: {person.full_name()} [red](скрыто)[/red]")

        console.print(table)
        console.print("\n")

    console.print("[bold green]Инфо:[/bold green] Если хотите подробнее узнать о конкретном человеке, напишите его уровень доступа и имя.")
    console.print("[bold green]Инфо:[/bold green] Также если вы просто напишите уровень доступа мы предложим вам игры по этому уровню!")
