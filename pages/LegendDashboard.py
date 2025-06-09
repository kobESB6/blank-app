import sys
import os

# Add the project root to sys.path so `legend` is recognized
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from legend.dashboard import show_legend_dashboard

show_legend_dashboard()
