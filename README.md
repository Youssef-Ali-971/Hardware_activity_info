# Hardware Activity Monitor

A lightweight, real-time terminal application for monitoring system hardware metrics including CPU usage, memory consumption, and network activity. Built with Python and Textual for cross-platform compatibility and minimal resource usage.

## ✨ Features

- **Real-time monitoring**: Live updates of CPU %, Memory %, and Network I/O every second
- **Terminal-based UI**: Clean, intuitive interface using Textual TUI framework
- **Data logging**: Automatic CSV logging for historical analysis and visualization
- **Cross-platform**: Runs on Linux, macOS, and Windows
- **Lightweight**: Minimal system resources and dependencies
- **Data visualization**: Built-in plotting capabilities for historical data analysis

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher

### Installation

#### Basic Installation (Monitoring Only)
```bash
# Windows/macOS/Linux
pip install psutil textual

# Arch Linux
sudo pacman -S python-psutil python-textual
```

#### Full Installation (Monitoring + Data Analysis)
```bash
# Windows/macOS/Linux
pip install psutil textual pandas matplotlib

# Arch Linux
sudo pacman -S python-psutil python-textual python-pandas python-matplotlib
```

### Usage

1. **Run the monitor**:
   ```bash
   python terminal_spy.py
   ```

2. **View real-time metrics** in the terminal interface

3. **Generate plots** from logged data:
   ```bash
   python plot_metrics.py
   ```

4. **Exit**: Press `q` to quit the application

## 📊 Data Output

- **Live display**: Real-time metrics in terminal
- **CSV logging**: Data saved to `system_log.csv` with timestamps
- **Visualization**: Graphs saved as `metrics_plot.png`

### CSV Format
```csv
timestamp,cpu_percent,memory_percent,net_sent,net_recv
2024-01-01T12:00:00,25.4,67.8,1048576,2097152
```

## 🛠️ Project Structure

```
hardware-activity/
├── terminal_spy.py      # Main monitoring application
├── plot_metrics.py      # Data visualization script
├── system_log.csv       # Generated data log
├── metrics_plot.png     # Generated plot
└── README.md           # This file
```

## 💡 Use Cases

- **System monitoring** on headless servers
- **Performance debugging** during development
- **Resource usage tracking** over time
- **Lightweight alternative** to GUI monitoring tools
- **Second monitor display** for compact setups

## 🔧 Customization

The application is built with modularity in mind:

- **Refresh interval**: Modify the `set_interval(1, ...)` value in `SystemStats.on_mount()`
- **Display format**: Customize the metrics display in `SystemStats.refresh_stats()`
- **Additional metrics**: Extend using `psutil` library capabilities
- **Styling**: Modify the Textual CSS or add custom themes

### Development Setup
```bash
git clone https://github.com/Youssef-Ali-971/hardware-activity
cd hardware-activity
pip install -r requirements.txt  # Create this file with dependencies
```

## 📋 Requirements

- **Python**: 3.7+
- **psutil**: System and process utilities
- **textual**: Modern TUI framework
- **pandas**: Data analysis (optional, for plotting)
- **matplotlib**: Visualization (optional, for plotting)

## 🐛 Troubleshooting

**Permission errors on Linux/macOS:**
```bash
# If you encounter permission issues
sudo python terminal_spy.py
```

**Module not found errors:**
```bash
# Ensure all dependencies are installed
pip install --upgrade psutil textual pandas matplotlib
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Youssef Ahmed Sayed Ali**
- Email: yaahmed2392010@gmail.com
- GitHub: [@Youssef-Ali-971](https://github.com/Youssef-Ali-971)

## 🏆 Acknowledgments

- Part of the **TerminalCraft YSWS** challenge
- Built with [Textual](https://github.com/Textualize/textual) TUI framework
- System metrics powered by [psutil](https://github.com/giampaolo/psutil)

---

⭐ **Star this repo** if you find it useful!
