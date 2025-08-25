import random
import matplotlib.pyplot as plt
import time

class SimpleCoinFlip:
    def __init__(self):
        self.heads_count = 0
        self.tails_count = 0
        self.flip_count = 0
        self.cumulative_heads = []
        self.cumulative_tails = []
        
    def flip_coin(self):
        """Flip a coin and return the result"""
        result = random.choice(['H', 'T'])
        
        if result == 'H':
            self.heads_count += 1
            print("🪙 HEADS!")
        else:
            self.tails_count += 1
            print("🪙 TAILS!")
            
        self.flip_count += 1
        self.cumulative_heads.append(self.heads_count)
        self.cumulative_tails.append(self.tails_count)
        
        return result
    
    def show_stats(self):
        """Display current statistics"""
        print(f"\n📊 Statistics:")
        print(f"   Heads: {self.heads_count}")
        print(f"   Tails: {self.tails_count}")
        print(f"   Total Flips: {self.flip_count}")
        if self.flip_count > 0:
            heads_percent = (self.heads_count / self.flip_count) * 100
            tails_percent = (self.tails_count / self.flip_count) * 100
            print(f"   Heads: {heads_percent:.1f}% | Tails: {tails_percent:.1f}%")
    
    def plot_graph(self):
        """Create and display the cumulative results graph"""
        if len(self.cumulative_heads) == 0:
            print("No data to plot yet. Flip some coins first!")
            return
            
        plt.figure(figsize=(10, 6))
        
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
        
        x = list(range(1, len(percentages) + 1))
        
        # Plot the percentage difference line
        plt.plot(x, percentages, 'b-', linewidth=2, marker='o', markersize=4, label='Excess Heads Over Tails (%)')
        
        # Add horizontal line at y=0
        plt.axhline(y=0, color='black', linestyle='--', alpha=0.5, label='Equal (50/50)')
        
        plt.xlabel('Trials')
        plt.ylabel('Excess Heads Over Tails (Percentage)')
        plt.title('The Law of Large Numbers')
        plt.grid(True, alpha=0.3)
        plt.legend()
        
        # Set y-axis limits to show from -50% to +50% like the reference
        plt.ylim(-50, 50)
        
        # Add some styling
        plt.style.use('default')
        plt.tight_layout()
        
        # Show the plot
        plt.show()
    
    def auto_flip(self, num_flips, delay=0.5):
        """Automatically flip the coin multiple times"""
        print(f"\n🔄 Auto-flipping {num_flips} times with {delay}s delay...")
        for i in range(num_flips):
            print(f"\nFlip {i+1}:", end=" ")
            self.flip_coin()
            time.sleep(delay)
        print("\n✅ Auto-flip complete!")
    
    def reset(self):
        """Reset all statistics"""
        self.heads_count = 0
        self.tails_count = 0
        self.flip_count = 0
        self.cumulative_heads.clear()
        self.cumulative_tails.clear()
        print("🔄 Statistics reset!")

def main():
    print("🪙 Welcome to the Simple Coin Flip Simulator!")
    print("=" * 50)
    
    coin_flip = SimpleCoinFlip()
    
    while True:
        print("\nOptions:")
        print("1. Flip coin once")
        print("2. Auto-flip multiple times")
        print("3. Show statistics")
        print("4. Show graph")
        print("5. Reset statistics")
        print("6. Exit")
        
        choice = input("\nEnter your choice (1-6): ").strip()
        
        if choice == '1':
            coin_flip.flip_coin()
            coin_flip.show_stats()
            
        elif choice == '2':
            try:
                num = int(input("How many flips? "))
                delay = float(input("Delay between flips (seconds)? "))
                coin_flip.auto_flip(num, delay)
                coin_flip.show_stats()
            except ValueError:
                print("❌ Please enter valid numbers!")
                
        elif choice == '3':
            coin_flip.show_stats()
            
        elif choice == '4':
            coin_flip.plot_graph()
            
        elif choice == '5':
            coin_flip.reset()
            
        elif choice == '6':
            print("👋 Thanks for using the Coin Flip Simulator!")
            break
            
        else:
            print("❌ Invalid choice! Please enter 1-6.")

if __name__ == "__main__":
    main()
