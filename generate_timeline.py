import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import numpy as np

# AI History data
events = [
    ("Turing Test Proposed", "Alan Turing, 1950", "Alan Turing proposes a method to evaluate machine intelligence.", 1950),
    ("Logic Theorist Program", "Newell & Simon, 1955", "The first AI program capable of proving mathematical theorems.", 1955),
    ("Perceptron Invented", "Frank Rosenblatt, 1958", "Introduction of the first neural network capable of learning patterns.", 1958),
    ("LISP Created", "John McCarthy, 1958", "Development of LISP, a key programming language for AI research.", 1958),
    ("General Problem Solver", "Newell & Simon, 1959", "A system designed to solve a broad range of problems.", 1959),
    ("ELIZA Chatbot", "Weizenbaum, 1966", "The first chatbot simulating human-like conversation.", 1966),
    ("Shakey the Robot", "1969", "First mobile robot capable of reasoning about its environment.", 1969),
    ("AI Winter Begins", "1974–1980", "Funding cuts and slow progress lead to the first AI Winter.", 1974),
    ("Expert Systems Boom", "1980s", "Rule-based systems like MYCIN and XCON dominate applied AI.", 1980),
    ("Backpropagation Popularized", "1986", "Rumelhart, Hinton, and Williams popularize backpropagation for training neural networks.", 1986),
    ("AI Winter II", "Late 1980s–1990s", "Another period of reduced funding due to unmet expectations.", 1989),
    ("Deep Blue Defeats Kasparov", "IBM, 1997", "Chess computer Deep Blue beats world champion Garry Kasparov.", 1997),
    ("Deep Learning Renaissance", "2006", "Hinton and others revive neural networks with deep architectures.", 2006),
    ("ImageNet Breakthrough", "AlexNet, 2012", "AlexNet wins ImageNet, showing deep CNNs outperform traditional methods.", 2012),
    ("AlphaGo Defeats Lee Sedol", "DeepMind, 2016", "Reinforcement learning mastery over Go by AI.", 2016),
    ("BERT and Transformer Models", "Google, 2018", "Introduction of BERT revolutionizes NLP with transformer architecture.", 2018),
    ("GPT-3 Released", "OpenAI, 2020", "Massive language model with broad capabilities in NLP tasks.", 2020),
    ("ChatGPT Launch", "OpenAI, 2022", "Conversational AI goes mainstream with wide public adoption.", 2022),
    ("GPT-4 Released", "OpenAI, 2023", "Multimodal and more advanced reasoning capabilities.", 2023),
    ("AI in Science & Medicine", "2020s", "AI assists in protein folding (AlphaFold), drug discovery, and scientific research.", 2023),
]

# Create the timeline with reduced height (no title space)
fig, ax = plt.subplots(figsize=(20, 10))

# Set up the timeline with original spacing (no top space for title)
ax.set_xlim(1945, 2025)
ax.set_ylim(-1, len(events) * 1.2)  # Remove top space since no title

# Remove axes and ticks
ax.set_yticks([])
ax.set_xticks([])  # Remove x-axis ticks to avoid duplicate years
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)

# Plot events with original vertical layout
for i, (title, subtitle, description, year) in enumerate(events):
    # Position with original spacing
    y_pos = (len(events) - i - 1) * 1.2  # Original spacing between events
    
    # Color coding by era
    if year < 1970:
        color = '#2E86AB'  # Early AI - Blue
    elif year < 1980:
        color = '#A23B72'  # AI Winter - Purple
    elif year < 2000:
        color = '#F18F01'  # Expert Systems - Orange
    elif year < 2015:
        color = '#C73E1D'  # Deep Learning - Red
    else:
        color = '#6B2D91'  # Modern AI - Purple
    
    # Draw event marker
    ax.plot(year, y_pos, 'o', markersize=12, color=color, markeredgecolor='black', markeredgewidth=1)
    
    # Draw connecting line
    ax.axhline(y=y_pos, xmin=0.02, xmax=(year-1945)/80, color='lightgray', linewidth=1, alpha=0.5)
    
    # Add text with original fonts
    ax.text(year + 0.5, y_pos, f"{title}\n{subtitle}", 
            fontsize=10, va='center', ha='left', fontweight='bold')
    ax.text(year + 0.5, y_pos - 0.6, description, 
            fontsize=8, va='center', ha='left', style='italic', alpha=0.8)

# Add title with original positioning
# ax.text(1950, len(events) * 1.2 + 0.5, "Artificial Intelligence Timeline", 
#         fontsize=20, fontweight='bold', ha='left')

# Add decade tick marks with labels
years = range(1950, 2025, 10)
for year in years:
    ax.axvline(x=year, color='lightgray', linewidth=0.5, alpha=0.3)
    ax.text(year, -0.5, str(year), fontsize=8, ha='center', va='top')

# Save as PNG
plt.tight_layout()
plt.savefig('ai_timeline.png', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()  # Close the figure instead of showing it

print("Timeline saved as 'ai_timeline.png'")
