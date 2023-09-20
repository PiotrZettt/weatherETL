
def create_chart():

    import matplotlib.pyplot as plt
    import matplotlib.dates as mdates
    import pandas as pd

    df = pd.read_csv('files/weather.csv')

    unique_names = df['name'].unique()

    plt.figure(figsize=(10, 6))

    for name in unique_names:
        subset = df[df['name'] == name]
        formatted_dates = pd.to_datetime(subset['extraction_timestamp'])
        date_format = mdates.DateFormatter("%d-%m-%Y--%H:%M")
        plt.plot(formatted_dates, subset['temp'], label=name, scalex=True)
        plt.gca().xaxis.set_major_formatter(date_format)

    plt.title('Temperature')
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.legend()

    plt.xticks(rotation=40)
    plt.tight_layout()
    plt.grid(True)
    plt.savefig('files/temperature_chart.pdf', format='pdf', dpi=300)
    plt.show()

