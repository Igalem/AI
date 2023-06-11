import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.ticker as ticker
import pandas as pd

def create_plot(data):
    # Convert data into DataFrame
    columns = list(data[0])
    df = pd.DataFrame(data[1:], columns=data[0])

    bar_colors = ['#575f6f']
    # Create bar plot
    # plt.plot(df['Month'], df['Total Spend'], color=bar_colors)
    # plt.plot(df['Month'], df['Total Spend'])
    # plt.xlabel('Month')
    # plt.ylabel('Total Spend')
    x = columns[0]
    y = columns[1]
    plt.style.use('https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-light.mplstyle')
    mpl.rcParams['font.size'] = 10

    # plt.plot(df[x], df[y], linewidth=2.0, color='#571270', marker='o')
    plt.bar(df[x], df[y], linewidth=2.0, color='#ad6eff')
    plt.ticklabel_format(style='plain', axis='y')
    plt.xlabel(x)
    plt.ylabel(y)
    # plt.tight_layout()
    plt.legend()
    plt.title(x)
    graph_path = 'static/graph1.png'
    plt.savefig(graph_path)
    plt.close() 
    return graph_path    