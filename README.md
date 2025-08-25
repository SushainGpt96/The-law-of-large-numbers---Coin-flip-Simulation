# Coin Flip Simulator

A simple Python application that simulates coin flips and displays cumulative results in a graph.

## Features

- **Interactive Coin Flipping**: Flip coins one at a time or automatically
- **Real-time Statistics**: Track heads, tails, and percentages
- **Live Graphing**: Visual representation of cumulative results
- **Two Versions**: GUI (tkinter) and Command-line interfaces

## Files

1. **`coin_flip_app.py`** - Full GUI application with tkinter
2. **`simple_coin_flip.py`** - Command-line version
3. **`requirements.txt`** - Python dependencies

## Installation

1. Make sure you have Python 3.8+ installed
2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### GUI Version (Recommended)

Run the full-featured GUI application:
```bash
python coin_flip_app.py
```

**Features:**
- Click "Flip Coin" to flip manually
- Enable "Auto-flip" for continuous flipping
- Adjust speed with the speed control
- Real-time graph updates
- Reset button to clear statistics

### Command-Line Version

Run the simple command-line version:
```bash
python simple_coin_flip.py
```

**Options:**
1. **Flip coin once** - Single coin flip
2. **Auto-flip multiple times** - Batch flipping with configurable delay
3. **Show statistics** - Display current counts and percentages
4. **Show graph** - Plot cumulative results
5. **Reset statistics** - Clear all data
6. **Exit** - Quit the application

## Example Output

```
🪙 Welcome to the Simple Coin Flip Simulator!
==================================================

Options:
1. Flip coin once
2. Auto-flip multiple times
3. Show statistics
4. Show graph
5. Reset statistics
6. Exit

Enter your choice (1-6): 1
🪙 HEADS!

📊 Statistics:
   Heads: 1
   Tails: 0
   Total Flips: 1
   Heads: 100.0% | Tails: 0.0%
```

## Graph Features

The application creates a focused, real-time graph showing:
- **Blue line with circles**: Excess Heads Over Tails as a percentage
- **Black dashed line**: Reference line at y=0 representing equal 50/50 distribution
- **X-axis**: Number of trials
- **Y-axis**: Percentage difference from -50% to +50%
- **Fixed y-axis range**: Always shows from -50% to +50% for consistent visualization

The single percentage graph creates a "random walk" visualization that demonstrates **The Law of Large Numbers**. It shows how the percentage difference between heads and tails converges toward 0% as the number of trials increases. When the line is above 0%, heads are leading; when below 0%, tails are leading. This format makes it easy to see how probability theory works in practice - early fluctuations give way to convergence as trials increase.

## Dependencies

- `matplotlib` - For creating graphs
- `tkinter` - Built-in Python GUI library (for GUI version)
- `random` - Built-in Python random module
- `time` - Built-in Python time module

## Tips

1. **For quick testing**: Use the command-line version
2. **For demonstration**: Use the GUI version with auto-flip
3. **For analysis**: Use the graphing feature to see trends
4. **Reset often**: Use the reset function to start fresh experiments

## Mathematical Background

The coin flip simulator demonstrates:
- **Probability**: Theoretical 50/50 chance for fair coin
- **Law of Large Numbers**: As flips increase, results approach theoretical probability
- **Random Walk**: The difference between heads and tails over time
- **Cumulative Statistics**: How individual results build up over multiple trials

## Troubleshooting

- **Graph not showing**: Make sure matplotlib is properly installed
- **GUI not working**: Ensure tkinter is available (usually built-in with Python)
- **Slow performance**: Reduce auto-flip speed or number of flips

## Future Enhancements

Potential improvements could include:
- Save/load statistics
- Export data to CSV
- Multiple coin types
- Advanced statistical analysis
- Animation effects
- Sound effects

Enjoy flipping coins and exploring probability! 🪙
