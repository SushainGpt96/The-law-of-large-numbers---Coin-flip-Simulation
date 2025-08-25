import tkinter as tk
from tkinter import ttk, messagebox
import random
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.animation as animation
from collections import deque
import threading
import time

class CoinFlipApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Coin Flip Simulator")
        self.root.geometry("800x600")
        
        # Initialize data
        self.heads_count = 0
        self.tails_count = 0
        self.flip_history = deque(maxlen=100)  # Keep last 100 flips
        self.cumulative_heads = deque(maxlen=100)
        self.cumulative_tails = deque(maxlen=100)
        self.flip_count = 0
        
        # Create GUI
        self.create_widgets()
        self.create_graph()
        
        # Animation
        self.animation_running = False
        self.ani = None
        
    def create_widgets(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        
        # Title
        title_label = ttk.Label(main_frame, text="Coin Flip Simulator", 
                               font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))
        
        # Coin display
        self.coin_label = ttk.Label(main_frame, text="🪙", font=("Arial", 48))
        self.coin_label.grid(row=1, column=0, columnspan=3, pady=(0, 20))
        
        # Flip button
        self.flip_button = ttk.Button(main_frame, text="Flip Coin", 
                                     command=self.flip_coin, style="Accent.TButton")
        self.flip_button.grid(row=2, column=0, columnspan=3, pady=(0, 20))
        
        # Statistics frame
        stats_frame = ttk.LabelFrame(main_frame, text="Statistics", padding="10")
        stats_frame.grid(row=3, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 20))
        
        # Heads count
        ttk.Label(stats_frame, text="Heads:").grid(row=0, column=0, sticky=tk.W, padx=(0, 10))
        self.heads_label = ttk.Label(stats_frame, text="0", font=("Arial", 12, "bold"))
        self.heads_label.grid(row=0, column=1, sticky=tk.W, padx=(0, 20))
        
        # Tails count
        ttk.Label(stats_frame, text="Tails:").grid(row=0, column=2, sticky=tk.W, padx=(0, 10))
        self.tails_label = ttk.Label(stats_frame, text="0", font=("Arial", 12, "bold"))
        self.tails_label.grid(row=0, column=3, sticky=tk.W, padx=(0, 20))
        
        # Total flips
        ttk.Label(stats_frame, text="Total Flips:").grid(row=0, column=4, sticky=tk.W, padx=(0, 10))
        self.total_label = ttk.Label(stats_frame, text="0", font=("Arial", 12, "bold"))
        self.total_label.grid(row=0, column=5, sticky=tk.W)
        
        # Control buttons frame
        control_frame = ttk.Frame(main_frame)
        control_frame.grid(row=4, column=0, columnspan=3, pady=(0, 20))
        
        # Auto-flip controls
        self.auto_flip_var = tk.BooleanVar()
        self.auto_flip_check = ttk.Checkbutton(control_frame, text="Auto-flip", 
                                              variable=self.auto_flip_var, 
                                              command=self.toggle_auto_flip)
        self.auto_flip_check.grid(row=0, column=0, padx=(0, 10))
        
        # Speed control
        ttk.Label(control_frame, text="Speed (ms):").grid(row=0, column=1, padx=(0, 5))
        self.speed_var = tk.StringVar(value="500")
        speed_spinbox = ttk.Spinbox(control_frame, from_=100, to=2000, increment=100,
                                   textvariable=self.speed_var, width=8)
        speed_spinbox.grid(row=0, column=2, padx=(0, 10))
        
        # Reset button
        reset_button = ttk.Button(control_frame, text="Reset", command=self.reset_stats)
        reset_button.grid(row=0, column=3)
        
        # Graph frame
        graph_frame = ttk.LabelFrame(main_frame, text="Cumulative Results", padding="10")
        graph_frame.grid(row=5, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S))
        graph_frame.columnconfigure(0, weight=1)
        graph_frame.rowconfigure(0, weight=1)
        main_frame.rowconfigure(5, weight=1)
        
        # Create matplotlib figure
        self.fig, self.ax = plt.subplots(figsize=(8, 4))
        self.canvas = FigureCanvasTkAgg(self.fig, graph_frame)
        self.canvas.get_tk_widget().grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
    def create_graph(self):
        self.ax.set_xlabel('Trials')
        self.ax.set_ylabel('Excess Heads Over Tails (Percentage)')
        self.ax.set_title('The Law of Large Numbers')
        self.ax.grid(True, alpha=0.3)
        self.ax.legend()
        
    def flip_coin(self):
        # Simulate coin flip
        result = random.choice(['H', 'T'])
        
        # Update counts
        if result == 'H':
            self.heads_count += 1
            self.coin_label.config(text="🪙\nHEADS!")
        else:
            self.tails_count += 1
            self.coin_label.config(text="🪙\nTAILS!")
        
        self.flip_count += 1
        
        # Update labels
        self.heads_label.config(text=str(self.heads_count))
        self.tails_label.config(text=str(self.tails_count))
        self.total_label.config(text=str(self.flip_count))
        
        # Store history
        self.flip_history.append(result)
        self.cumulative_heads.append(self.heads_count)
        self.cumulative_tails.append(self.tails_count)
        
        # Update graph
        self.update_graph()
        
        # Reset coin display after 1 second
        self.root.after(1000, lambda: self.coin_label.config(text="🪙"))
        
    def update_graph(self):
        self.ax.clear()
        
        if len(self.cumulative_heads) > 0:
            x = list(range(1, len(self.cumulative_heads) + 1))
            
            # Calculate the percentage difference (excess heads over tails as percentage)
            percentages = []
            for heads, tails in zip(self.cumulative_heads, self.cumulative_tails):
                total = heads + tails
                if total > 0:
                    # Calculate percentage: (heads - tails) / total * 100
                    percentage = ((heads - tails) / total) * 100
                    percentages.append(percentage)
                else:
                    percentages.append(0)
            
            # Plot the percentage difference line
            self.ax.plot(x, percentages, 'b-', linewidth=2, marker='o', markersize=4, label='Excess Heads Over Tails (%)')
            
            # Add horizontal line at y=0
            self.ax.axhline(y=0, color='black', linestyle='--', alpha=0.5, label='Equal (50/50)')
            
            self.ax.set_xlabel('Trials')
            self.ax.set_ylabel('Excess Heads Over Tails (Percentage)')
            self.ax.set_title('The Law of Large Numbers')
            self.ax.grid(True, alpha=0.3)
            self.ax.legend()
            
            # Set y-axis limits to show from -50% to +50% like the reference
            self.ax.set_ylim(-50, 50)
        
        self.canvas.draw()
        
    def toggle_auto_flip(self):
        if self.auto_flip_var.get():
            self.start_auto_flip()
        else:
            self.stop_auto_flip()
            
    def start_auto_flip(self):
        self.animation_running = True
        self.auto_flip_thread()
        
    def stop_auto_flip(self):
        self.animation_running = False
        
    def auto_flip_thread(self):
        def auto_flip():
            while self.animation_running:
                self.root.after(0, self.flip_coin)
                time.sleep(int(self.speed_var.get()) / 1000)
                
        thread = threading.Thread(target=auto_flip, daemon=True)
        thread.start()
        
    def reset_stats(self):
        self.heads_count = 0
        self.tails_count = 0
        self.flip_count = 0
        self.flip_history.clear()
        self.cumulative_heads.clear()
        self.cumulative_tails.clear()
        
        self.heads_label.config(text="0")
        self.tails_label.config(text="0")
        self.total_label.config(text="0")
        self.coin_label.config(text="🪙")
        
        self.update_graph()

def main():
    root = tk.Tk()
    app = CoinFlipApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
