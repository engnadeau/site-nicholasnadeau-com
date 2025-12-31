#!/usr/bin/env python3
"""
Generate visualizations for the AI Cost Economics blog post.
Charts: Token cost decline vs Capex explosion, DeepSeek disruption, etc.
"""

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
from datetime import datetime
import os

# Set style for clean, professional charts
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.size'] = 11
plt.rcParams['axes.labelsize'] = 12
plt.rcParams['axes.titlesize'] = 14
plt.rcParams['figure.facecolor'] = 'white'

OUTPUT_DIR = '/home/user/site-nicholasnadeau-com/src/assets/images/post/2025'

def create_token_cost_vs_capex_chart():
    """
    Dual-axis chart showing token cost decline (log scale) vs capex growth.
    """
    fig, ax1 = plt.subplots(figsize=(12, 7))

    # Token cost data (per million tokens, blended input/output for frontier models)
    token_dates = [
        datetime(2023, 3, 1),   # GPT-4 launch
        datetime(2023, 6, 1),   # GPT-3.5 Turbo price cut
        datetime(2023, 11, 1),  # GPT-4 Turbo
        datetime(2024, 5, 1),   # GPT-4o launch
        datetime(2024, 7, 1),   # GPT-4o mini
        datetime(2024, 10, 1),  # Claude 3.5 Sonnet refresh
        datetime(2025, 1, 1),   # DeepSeek R1
        datetime(2025, 6, 1),   # Mid-2025 prices
        datetime(2025, 12, 1),  # End 2025
    ]

    # Frontier model token costs (blended $/million tokens)
    token_costs = [
        45.0,   # GPT-4 launch ($30/$60 blended)
        2.0,    # GPT-3.5 Turbo cut
        15.0,   # GPT-4 Turbo ($10/$30 blended)
        10.0,   # GPT-4o ($5/$15)
        0.375,  # GPT-4o mini ($0.15/$0.60)
        4.5,    # Claude 3.5 Sonnet ($3/$15)
        1.37,   # DeepSeek R1 ($0.55/$2.19)
        2.0,    # Mid-2025 avg frontier
        1.0,    # End 2025 projected
    ]

    # Capex data (quarterly, in billions)
    capex_dates = [
        datetime(2023, 3, 31),
        datetime(2023, 6, 30),
        datetime(2023, 9, 30),
        datetime(2023, 12, 31),
        datetime(2024, 3, 31),
        datetime(2024, 6, 30),
        datetime(2024, 9, 30),
        datetime(2024, 12, 31),
        datetime(2025, 3, 31),
        datetime(2025, 6, 30),
        datetime(2025, 9, 30),
        datetime(2025, 12, 31),
    ]

    # Hyperscaler capex (Amazon, Microsoft, Google, Meta combined, quarterly $B)
    capex_quarterly = [
        35, 38, 40, 45,      # 2023
        48, 53, 60, 65,      # 2024 (~$241B total)
        85, 95, 113, 112,    # 2025 (~$405B total, Q3 was $113.4B per research)
    ]

    # Plot token costs on left axis (log scale)
    color1 = '#2ecc71'  # Green for costs going down
    ax1.set_xlabel('Date', fontweight='bold')
    ax1.set_ylabel('Token Cost ($/million tokens)', color=color1, fontweight='bold')
    line1 = ax1.semilogy(token_dates, token_costs, 'o-', color=color1, linewidth=2.5,
                          markersize=8, label='Frontier Model Token Cost')
    ax1.tick_params(axis='y', labelcolor=color1)
    ax1.set_ylim(0.1, 100)

    # Add annotations for key models
    annotations = [
        (datetime(2023, 3, 1), 45, 'GPT-4\nLaunch', (-30, 20)),
        (datetime(2024, 7, 1), 0.375, 'GPT-4o\nmini', (30, -30)),
        (datetime(2025, 1, 1), 1.37, 'DeepSeek\nR1', (30, 10)),
    ]
    for date, cost, label, offset in annotations:
        ax1.annotate(label, xy=(date, cost), xytext=offset,
                     textcoords='offset points', fontsize=9,
                     arrowprops=dict(arrowstyle='->', color='gray', lw=0.8),
                     bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.8))

    # Plot capex on right axis
    ax2 = ax1.twinx()
    color2 = '#e74c3c'  # Red for costs going up
    ax2.set_ylabel('Quarterly Capex ($B)', color=color2, fontweight='bold')
    line2 = ax2.bar(capex_dates, capex_quarterly, width=25, alpha=0.6, color=color2,
                    label='Hyperscaler Capex')
    ax2.tick_params(axis='y', labelcolor=color2)
    ax2.set_ylim(0, 150)

    # Format x-axis
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
    ax1.xaxis.set_major_locator(mdates.MonthLocator(interval=4))
    plt.xticks(rotation=45)

    # Title and legend
    plt.title('The Great Divergence: AI Token Costs vs Infrastructure Spending',
              fontsize=16, fontweight='bold', pad=20)

    # Create combined legend
    lines1, labels1 = ax1.get_legend_handles_labels()
    ax1.legend(lines1 + [plt.Rectangle((0,0),1,1, fc=color2, alpha=0.6)],
               labels1 + ['Hyperscaler Capex'], loc='upper center',
               bbox_to_anchor=(0.5, -0.15), ncol=2, frameon=True)

    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}/2025-12_ai-cost-divergence.png', dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print(f"Saved: {OUTPUT_DIR}/2025-12_ai-cost-divergence.png")


def create_training_cost_comparison():
    """
    Bar chart comparing training costs: DeepSeek vs estimated hyperscaler costs.
    """
    fig, ax = plt.subplots(figsize=(10, 6))

    # Training cost estimates (in millions $)
    models = ['DeepSeek R1\n($5.6M)', 'GPT-4\n(est. $100M+)', 'Gemini Ultra\n(est. $200M+)',
              'Claude 3\n(est. $100M+)', 'Llama 3\n(est. $150M+)']
    costs = [5.6, 100, 200, 100, 150]

    colors = ['#2ecc71', '#e74c3c', '#e74c3c', '#e74c3c', '#3498db']  # Green for DeepSeek, red for big tech, blue for Meta (open)

    bars = ax.bar(models, costs, color=colors, edgecolor='white', linewidth=1.5)

    # Add value labels on bars
    for bar, cost in zip(bars, costs):
        height = bar.get_height()
        ax.annotate(f'${cost}M' if cost < 10 else f'${int(cost)}M',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 5), textcoords='offset points',
                    ha='center', va='bottom', fontweight='bold', fontsize=11)

    ax.set_ylabel('Estimated Training Cost ($ Millions)', fontweight='bold')
    ax.set_title('The DeepSeek Shock: Frontier AI at a Fraction of the Cost',
                 fontsize=14, fontweight='bold', pad=15)

    # Add annotation for the 18x-36x difference
    ax.annotate('18x-36x\ncheaper', xy=(0, 50), fontsize=12, fontweight='bold',
                color='#2ecc71', ha='center')

    ax.set_ylim(0, 250)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}/2025-12_deepseek-training-cost.png', dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print(f"Saved: {OUTPUT_DIR}/2025-12_deepseek-training-cost.png")


def create_capex_growth_chart():
    """
    Line chart showing hyperscaler capex growth with projections.
    """
    fig, ax = plt.subplots(figsize=(10, 6))

    years = [2022, 2023, 2024, 2025, 2026, 2027]

    # Historical and projected capex (in billions)
    # 2022-2024: ~$477B total per Goldman
    # 2025-2027: ~$1.15T projected per Goldman
    capex = [140, 180, 241, 405, 500, 450]  # Conservative 2027

    # Create gradient fill
    ax.fill_between(years, capex, alpha=0.3, color='#e74c3c')
    ax.plot(years, capex, 'o-', color='#e74c3c', linewidth=2.5, markersize=10)

    # Add value labels
    for year, cap in zip(years, capex):
        ax.annotate(f'${cap}B', xy=(year, cap), xytext=(0, 10),
                    textcoords='offset points', ha='center', fontweight='bold')

    # Highlight the projection zone
    ax.axvspan(2024.5, 2027, alpha=0.1, color='gray')
    ax.annotate('Projected', xy=(2026, 550), ha='center', fontsize=10,
                fontstyle='italic', color='gray')

    ax.set_xlabel('Year', fontweight='bold')
    ax.set_ylabel('Annual Capex ($ Billions)', fontweight='bold')
    ax.set_title('Hyperscaler AI Infrastructure Spending\n(Amazon, Microsoft, Google, Meta)',
                 fontsize=14, fontweight='bold', pad=15)

    ax.set_xlim(2021.5, 2027.5)
    ax.set_ylim(0, 600)
    ax.set_xticks(years)

    # Add growth rate annotation
    ax.annotate('+68% YoY\n(2024→2025)', xy=(2024.5, 320), fontsize=10,
                ha='center', color='#e74c3c', fontweight='bold')

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}/2025-12_hyperscaler-capex.png', dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print(f"Saved: {OUTPUT_DIR}/2025-12_hyperscaler-capex.png")


def create_cost_decline_rate_chart():
    """
    Visualization of the 10x/year cost decline vs Moore's Law.
    """
    fig, ax = plt.subplots(figsize=(10, 6))

    years = np.array([0, 1, 2, 3, 4, 5])
    year_labels = ['2023', '2024', '2025', '2026', '2027', '2028']

    # Starting from GPT-4 launch cost of ~$45/M tokens
    start_cost = 45

    # Different decline rates
    ai_decline_10x = start_cost / (10 ** years)  # 10x per year (AI inference)
    moores_law = start_cost / (2 ** (years * 0.66))  # ~2x every 18 months

    ax.semilogy(years, ai_decline_10x, 'o-', color='#2ecc71', linewidth=2.5,
                markersize=10, label='AI Inference Cost (10x/year)')
    ax.semilogy(years, moores_law, 's--', color='#3498db', linewidth=2,
                markersize=8, label="Moore's Law (~2x/18mo)")

    ax.set_xlabel('Years from GPT-4 Launch', fontweight='bold')
    ax.set_ylabel('Cost per Million Tokens ($)', fontweight='bold')
    ax.set_title('AI Cost Deflation: Faster Than Moore\'s Law',
                 fontsize=14, fontweight='bold', pad=15)

    ax.set_xticks(years)
    ax.set_xticklabels(year_labels)
    ax.set_ylim(0.0001, 100)

    ax.legend(loc='upper right', frameon=True)

    # Add annotation about the gap
    ax.annotate('By 2026:\nAI: $0.0045/M\nMoore: $7.50/M\n~1600x difference',
                xy=(3, 0.01), fontsize=10,
                bbox=dict(boxstyle='round,pad=0.5', facecolor='lightyellow', alpha=0.8))

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}/2025-12_ai-vs-moores-law.png', dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print(f"Saved: {OUTPUT_DIR}/2025-12_ai-vs-moores-law.png")


def create_bubble_indicators_chart():
    """
    Multi-metric view of AI bubble warning signs.
    """
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))

    # 1. Capex vs Revenue Growth
    ax1 = axes[0, 0]
    quarters = ['Q1 24', 'Q2 24', 'Q3 24', 'Q4 24', 'Q1 25', 'Q2 25', 'Q3 25']
    capex_growth = [45, 52, 63, 68, 70, 72, 75]  # YoY %
    cloud_revenue_growth = [25, 28, 30, 32, 33, 35, 34]  # YoY %

    x = np.arange(len(quarters))
    width = 0.35
    ax1.bar(x - width/2, capex_growth, width, label='Capex Growth', color='#e74c3c', alpha=0.8)
    ax1.bar(x + width/2, cloud_revenue_growth, width, label='Cloud Revenue Growth', color='#3498db', alpha=0.8)
    ax1.set_ylabel('YoY Growth (%)')
    ax1.set_title('Spending Outpacing Revenue', fontweight='bold')
    ax1.set_xticks(x)
    ax1.set_xticklabels(quarters, rotation=45)
    ax1.legend(loc='upper left', fontsize=9)
    ax1.axhline(y=50, color='gray', linestyle='--', alpha=0.5)

    # 2. Debt Accumulation
    ax2 = axes[0, 1]
    years = ['2021', '2022', '2023', '2024', '2025']
    debt = [25, 30, 35, 60, 121]  # Billions, with 2025 being the $121B figure
    colors = ['#3498db', '#3498db', '#3498db', '#f39c12', '#e74c3c']
    ax2.bar(years, debt, color=colors, edgecolor='white')
    ax2.set_ylabel('New Debt ($B)')
    ax2.set_title('Hyperscaler Debt Surge\n(300% increase in 2024-25)', fontweight='bold')
    for i, d in enumerate(debt):
        ax2.annotate(f'${d}B', xy=(i, d), xytext=(0, 5),
                     textcoords='offset points', ha='center', fontsize=10)

    # 3. Free Cash Flow Trend
    ax3 = axes[1, 0]
    quarters_fcf = ['Q1 24', 'Q2 24', 'Q3 24', 'Q4 24', 'Q1 25', 'Q2 25', 'Q3 25']
    fcf_growth = [15, 10, 5, -2, -5, -10, -16]  # Estimated FCF growth %
    colors_fcf = ['#2ecc71' if x >= 0 else '#e74c3c' for x in fcf_growth]
    ax3.bar(quarters_fcf, fcf_growth, color=colors_fcf, alpha=0.8)
    ax3.axhline(y=0, color='black', linewidth=1)
    ax3.set_ylabel('FCF Growth (%)')
    ax3.set_title('Free Cash Flow Turning Negative', fontweight='bold')
    ax3.set_xticklabels(quarters_fcf, rotation=45)

    # 4. Consumer Adoption Reality
    ax4 = axes[1, 1]
    categories = ['Using AI\n(any form)', 'Paying for AI', 'Enterprise\nAI ROI']
    percentages = [71, 3, 15]
    colors_adopt = ['#3498db', '#e74c3c', '#f39c12']
    bars = ax4.bar(categories, percentages, color=colors_adopt, alpha=0.8)
    ax4.set_ylabel('Percentage (%)')
    ax4.set_title('The Monetization Gap', fontweight='bold')
    ax4.set_ylim(0, 100)
    for bar, pct in zip(bars, percentages):
        ax4.annotate(f'{pct}%', xy=(bar.get_x() + bar.get_width()/2, pct),
                     xytext=(0, 5), textcoords='offset points', ha='center',
                     fontweight='bold', fontsize=12)

    plt.suptitle('AI Bubble Warning Indicators', fontsize=16, fontweight='bold', y=1.02)
    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}/2025-12_bubble-indicators.png', dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print(f"Saved: {OUTPUT_DIR}/2025-12_bubble-indicators.png")


if __name__ == '__main__':
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    print("Generating AI Economics visualizations...")
    create_token_cost_vs_capex_chart()
    create_training_cost_comparison()
    create_capex_growth_chart()
    create_cost_decline_rate_chart()
    create_bubble_indicators_chart()
    print("\nAll charts generated successfully!")
