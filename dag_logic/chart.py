
def create_chart():

    import matplotlib.pyplot as plt
    import pandas as pd

    df = pd.read_csv('files/weather.csv')

    unique_names = df['name'].unique()

    plt.figure(figsize=(10, 6))

    for name in unique_names:
        subset = df[df['name'] == name]
        plt.plot(subset['extraction_timestamp'], subset['temp'], label=name)

    plt.title('Temperature')
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.legend()

    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.grid(True)
    plt.savefig('files/temperature_chart.pdf', format='pdf', dpi=300)
    plt.show()
