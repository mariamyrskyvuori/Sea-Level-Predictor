import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Tuodaan data CSV-tiedostosta
    df = pd.read_csv('epa-sea-level.csv')


    # Luodaan scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])


    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    print(f'Slope: {slope}')
    print(f'Intercept: {intercept}')

    # Luodaan vuosilukujen väli 1880-2050
    years_extended = pd.Series(range(1880, 2051))

    # Lasketaan sovitusviivan y-arvot
    sea_levels_extended = slope * years_extended + intercept


    # Piirretään sovitusviiva
    plt.plot(years_extended, sea_levels_extended, color='red', label='Best fit line 1880-2050')

    # Create second line of best fit (using data from year 2000)
    df_recent = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    print(f'Recent Slope: {slope_recent}')
    print(f'Recent Intercept: {intercept_recent}')

    # Luodaan vuosilukujen väli 2000-2050
    years_recent = pd.Series(range(2000, 2051))

    # Lasketaan sovitusviivan y-arvot (2000-2050)
    sea_levels_recent = slope_recent * years_recent + intercept_recent

    # Piirretään toinen sovitusviiva (2000-2050)
    plt.plot(years_recent, sea_levels_recent, color='green', label='Best fit line 2000-2050')

    # Asetetaan otsikko ja akselien nimet
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.legend()

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()