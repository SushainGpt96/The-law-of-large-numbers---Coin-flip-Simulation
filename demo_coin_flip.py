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
    print("This demo will flip 50 coins and show you the new graph!")
    print("The graph now shows the difference between heads and tails")
    print("moving between positive and negative y-axis values.")
    print()
    
    # Create coin flip instance
    cf = SimpleCoinFlip()
    
    # Auto-flip 50 times with a short delay
    print("🔄 Flipping 50 coins...")
    cf.auto_flip(50, 0.1)
    
    # Show final statistics
    cf.show_stats()
    
    print("\n📈 Now showing the new graph...")
    print("The blue line shows Heads - Tails difference")
    print("Above 0 = heads leading, Below 0 = tails leading")
    print("The black dashed line represents equal 50/50 distribution")
    
    # Show the graph
    cf.plot_graph()
    
    print("\n✅ Demo complete! The graph shows how the coin flip results")
    print("deviate from the theoretical 50/50 distribution over time.")

if __name__ == "__main__":
    main()
