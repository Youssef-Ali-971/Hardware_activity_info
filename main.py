import psutil
import datetime
import csv
from pathlib import Path
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static
from textual.containers import Container
from textual.reactive import reactive

LOG_FILE = Path("system_log.csv")

class SystemStats(Static):
    cpu = reactive(0.0)
    mem = reactive(0.0)
    net_sent = reactive(0)
    net_recv = reactive(0)

    def on_mount(self):
        self.set_interval(1, self.refresh_stats)

    def refresh_stats(self):
        self.cpu = psutil.cpu_percent()
        self.mem = psutil.virtual_memory().percent
        net_io = psutil.net_io_counters()
        self.net_sent = net_io.bytes_sent
        self.net_recv = net_io.bytes_recv

        self.log_stats()

        self.update(
            f"[b yellow]CPU:[/b yellow] {self.cpu:.1f}%\n"
            f"[b yellow]Memory:[/b yellow] {self.mem:.1f}%\n"
            f"[b yellow]Net Sent:[/b yellow] {self.net_sent / 1_000_000:.2f} MB\n"
            f"[b yellow]Net Received:[/b yellow] {self.net_recv / 1_000_000:.2f} MB\n"
        )

    def log_stats(self):
        now = datetime.datetime.now().isoformat()
        with LOG_FILE.open("a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([now, self.cpu, self.mem, self.net_sent, self.net_recv])

        if LOG_FILE.stat().st_size == 0:
            writer.writerow(["timestamp", "cpu_percent", "memory_percent", "net_sent", "net_recv"])


class TerminalSpyApp(App):
    TITLE = "Hardware activity"
    CSS_PATH = None
    BINDINGS = [("q", "quit", "Quit")]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Container(SystemStats(id="stats"))
        yield Footer()


if __name__ == "__main__":
    if not LOG_FILE.exists():
        LOG_FILE.write_text("timestamp,cpu_percent,memory_percent,net_sent,net_recv\n")
    TerminalSpyApp().run()
