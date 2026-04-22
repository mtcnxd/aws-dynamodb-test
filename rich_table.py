from rich import print
from rich.table import Table
from rich.console import Console
from rich.progress import Progress
from rich.panel import Panel
from rich.live import Live
import httpx
import json
import time

def get_data() -> dict | None:
   response = httpx.get("https://mecanicarubio.com/api/investments/total")
   if response.status_code != 200:
      return None

   return json.loads(response.text)

def generar_tabla():
    table = Table()
    table.add_column("Tiempo", width=50)
    table.add_row(str(time.time()))
    return table

data = get_data()

console = Console()

table = Table(title=f"Balances - Total: {data['total']}")
table.add_column("ID", style="dim", width=5)
table.add_column("Name", style="green")
table.add_column("Last Amount", style="yellow", justify="right")
table.add_column("Current Amount", style="cyan", justify="right")

with Progress() as progress:
    task1 = progress.add_task("[green]Getting data from server ...", total=100)

    while not progress.finished:
        progress.update(task1, advance=0.5)
        time.sleep(0.01)

console.print(Panel(json.dumps(data, indent=2), title="Raw response from API"))

if data is not None:
    for item in data['items']:
        id = str(item['id'])
        name = str(item['name'])
        last_amount = str(item['last_amount'])
        current_amount = str(item['current_amount'])

        table.add_row(id, name, last_amount, current_amount)

console.print(table)

with Live(generar_tabla(), refresh_per_second=2) as live:
    while True:
        time.sleep(1)
        live.update(generar_tabla())

console.log("Process finished successfully!")