# Python Data Visualization Assignment
# Starter code for creating charts and graphs with matplotlib and plotly

import matplotlib.pyplot as plt
import numpy as np
# import plotly.graph_objects as go  # Uncomment when using plotly
# import plotly.express as px  # Uncomment when using plotly

# Sample data
x = np.linspace(0, 10, 100)
y = np.sin(x)
categories = ['A', 'B', 'C', 'D']
values = [23, 45, 56, 78]

# TODO: Task 1 - Basic Plots with Matplotlib
def basic_matplotlib_plots():
    # Line plot
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label='sin(x)', color='blue', linewidth=2)
    plt.title('Basic Line Plot')
    plt.xlabel('X values')
    plt.ylabel('Y values')
    plt.legend()
    plt.grid(True)
    plt.savefig('line_plot.png')
    plt.show()

    # Bar chart
    plt.figure(figsize=(8, 5))
    plt.bar(categories, values, color=['red', 'green', 'blue', 'orange'])
    plt.title('Basic Bar Chart')
    plt.xlabel('Categories')
    plt.ylabel('Values')
    plt.savefig('bar_chart.png')
    plt.show()

    # Scatter plot
    plt.figure(figsize=(8, 6))
    plt.scatter(x[:50], y[:50], c=y[:50], cmap='viridis', s=50)
    plt.title('Scatter Plot with Color Mapping')
    plt.xlabel('X values')
    plt.ylabel('Y values')
    plt.colorbar(label='Y value')
    plt.savefig('scatter_plot.png')
    plt.show()

# TODO: Task 2 - Advanced Charts and Customization
def advanced_matplotlib():
    # Histogram
    data = np.random.normal(0, 1, 1000)
    plt.figure(figsize=(8, 6))
    plt.hist(data, bins=30, alpha=0.7, color='skyblue', edgecolor='black')
    plt.title('Histogram of Normal Distribution')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.savefig('histogram.png')
    plt.show()

    # Pie chart
    plt.figure(figsize=(8, 8))
    plt.pie(values, labels=categories, autopct='%1.1f%%', startangle=90)
    plt.title('Pie Chart Example')
    plt.axis('equal')
    plt.savefig('pie_chart.png')
    plt.show()

    # Subplots
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 10))

    ax1.plot(x, y)
    ax1.set_title('Line Plot')

    ax2.bar(categories, values)
    ax2.set_title('Bar Chart')

    ax3.hist(data, bins=20)
    ax3.set_title('Histogram')

    ax4.scatter(x[:30], y[:30])
    ax4.set_title('Scatter Plot')

    plt.tight_layout()
    plt.savefig('subplots.png')
    plt.show()

# TODO: Task 3 - Interactive Visualizations with Plotly
def plotly_visualizations():
    # Note: Uncomment the plotly imports at the top first
    # This function requires plotly to be installed

    try:
        import plotly.graph_objects as go
        import plotly.express as px

        # Interactive scatter plot
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=x, y=y, mode='lines+markers', name='sin(x)'))
        fig.update_layout(
            title='Interactive Line Plot',
            xaxis_title='X values',
            yaxis_title='Y values'
        )
        fig.write_html('interactive_plot.html')
        fig.show()

        # Interactive bar chart with plotly express
        df_data = {'Category': categories, 'Value': values}
        fig = px.bar(df_data, x='Category', y='Value', title='Interactive Bar Chart')
        fig.write_html('interactive_bar.html')
        fig.show()

    except ImportError:
        print("Plotly not installed. Install with: pip install plotly")
        print("For now, focus on matplotlib visualizations above.")

if __name__ == "__main__":
    print("=== Basic Matplotlib Plots ===")
    basic_matplotlib_plots()

    print("\n=== Advanced Matplotlib Charts ===")
    advanced_matplotlib()

    print("\n=== Plotly Interactive Visualizations ===")
    plotly_visualizations()