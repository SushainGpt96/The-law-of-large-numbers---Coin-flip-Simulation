#!/usr/bin/env python3
"""
Demo script for the Coin Flip Simulator
This script demonstrates the new graph functionality that shows
the difference between heads and tails on a line graph.
"""

from simple_coin_flip import SimpleCoinFlip
import time

def main():
    print("🪙 Coin Flip Simulator Demo")
    print("=" * 40)
    print("This demo will flip 1000 coins and show you the percentage graph!")
    print("The graph shows the excess of heads over tails (percentage)")
    print("moving between positive and negative y-axis values.")
    print()
    
    # Create coin flip instance
    cf = SimpleCoinFlip()
    
    # Auto-flip 1000 times with a short delay
    total_flips = 1000
    delay_seconds = 0.01
    print(f"🔄 Flipping {total_flips} coins with {delay_seconds}s delay...")
    cf.auto_flip(total_flips, delay_seconds)
    
    # Show final statistics
    cf.show_stats()
    
    print("\n📈 Now showing the graph (Law of Large Numbers)...")
    print("The blue line shows percentage difference: Heads - Tails")
    print("Above 0% = heads leading, Below 0% = tails leading")
    print("The black dashed line represents equal 50/50 distribution")
    
    # Show the graph
    cf.plot_graph()
    
    print("\n✅ Demo complete! The graph shows how the coin flip results")
    print("deviate from and converge toward the theoretical 50/50 over time.")

if __name__ == "__main__":
    main()
