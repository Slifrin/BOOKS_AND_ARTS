#!/usr/bin/env python3
"""
Process Monitor CLI Tool
Monitors top 20 processes by memory usage with live updates.
Shows process name, PID, CPU usage, and memory usage.
Uses only Python standard library modules.
"""

import subprocess
import time
import os
import sys
import signal
from collections import namedtuple
import argparse

# Process information structure
ProcessInfo = namedtuple('ProcessInfo', ['pid', 'name', 'cpu_percent', 'memory_mb'])

class ProcessMonitor:
    def __init__(self, refresh_interval=2.0):
        self.refresh_interval = refresh_interval
        self.running = True
        
    def get_processes(self):
        """Get process information using ps command."""
        try:
            # Use ps command to get process information
            # Format: PID, COMMAND, %CPU, RSS (memory in KB)
            cmd = ['ps', 'axo', 'pid=,comm=,%cpu=,rss=']
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            
            processes = []
            for line in result.stdout.strip().split('\n'):
                if line.strip():
                    parts = line.strip().split(None, 3)
                    if len(parts) >= 4:
                        try:
                            pid = int(parts[0])
                            name = parts[1]
                            cpu_percent = float(parts[2])
                            memory_kb = int(parts[3])
                            memory_mb = memory_kb / 1024.0  # Convert KB to MB
                            
                            processes.append(ProcessInfo(
                                pid=pid,
                                name=name,
                                cpu_percent=cpu_percent,
                                memory_mb=memory_mb
                            ))
                        except (ValueError, IndexError):
                            continue
            
            # Sort by memory usage (descending) and return top 20
            processes.sort(key=lambda p: p.memory_mb, reverse=True)
            return processes[:20]
            
        except subprocess.CalledProcessError as e:
            print(f"Error running ps command: {e}")
            return []
        except Exception as e:
            print(f"Error getting process information: {e}")
            return []
    
    def clear_screen(self):
        """Clear the terminal screen using ANSI escape sequences."""
        # \033[2J clears the entire screen
        # \033[H moves cursor to home position (0,0)
        print('\033[2J\033[H', end='')
        sys.stdout.flush()
    
    def format_memory(self, memory_mb):
        """Format memory size for display."""
        if memory_mb >= 1024:
            return f"{memory_mb/1024:.1f}GB"
        else:
            return f"{memory_mb:.1f}MB"
    
    def display_processes(self, processes):
        """Display the process information in a formatted table."""
        self.clear_screen()
        
        print("=" * 80)
        print("TOP 20 PROCESSES BY MEMORY USAGE")
        print("=" * 80)
        print(f"Updated: {time.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Refresh interval: {self.refresh_interval} seconds")
        print("Press Ctrl+C to exit")
        print("=" * 80)
        
        # Header
        header = f"{'PID':<8} {'PROCESS NAME':<25} {'CPU%':<8} {'MEMORY':<10}"
        print(header)
        print("-" * 80)
        
        # Process rows
        for i, process in enumerate(processes, 1):
            # Truncate long process names
            name = process.name[:24] if len(process.name) > 24 else process.name
            memory_str = self.format_memory(process.memory_mb)
            
            row = f"{process.pid:<8} {name:<25} {process.cpu_percent:<8.1f} {memory_str:<10}"
            print(row)
        
        print("=" * 80)
    
    def signal_handler(self, signum, frame):
        """Handle interrupt signal (Ctrl+C)."""
        self.running = False
        print("\nExiting process monitor...")
        sys.exit(0)
    
    def run(self):
        """Main monitoring loop."""
        # Set up signal handler for graceful exit
        signal.signal(signal.SIGINT, self.signal_handler)
        
        print("Starting process monitor...")
        print("Loading...")
        
        while self.running:
            try:
                processes = self.get_processes()
                if processes:
                    self.display_processes(processes)
                else:
                    print("No process information available.")
                
                time.sleep(self.refresh_interval)
                
            except KeyboardInterrupt:
                self.signal_handler(None, None)
            except Exception as e:
                print(f"Error in monitoring loop: {e}")
                time.sleep(self.refresh_interval)

def main():
    """Main function with command line argument parsing."""
    parser = argparse.ArgumentParser(
        description="Monitor top 20 processes by memory usage with live updates"
    )
    parser.add_argument(
        '-i', '--interval',
        type=float,
        default=2.0,
        help='Refresh interval in seconds (default: 2.0)'
    )
    parser.add_argument(
        '--version',
        action='version',
        version='Process Monitor 1.0'
    )
    
    args = parser.parse_args()
    
    # Validate refresh interval
    if args.interval < 0.5:
        print("Warning: Minimum refresh interval is 0.5 seconds")
        args.interval = 0.5
    elif args.interval > 60:
        print("Warning: Maximum refresh interval is 60 seconds")
        args.interval = 60
    
    # Create and run monitor
    monitor = ProcessMonitor(refresh_interval=args.interval)
    
    try:
        monitor.run()
    except Exception as e:
        print(f"Fatal error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()