import matplotlib.pyplot as plt


def plot_results(infected, day_fontsize = 16, infected_cases_fontsize = 16, 
    outbreak_test_fontsize = 20, axis_brightness = 0.2 ):
    
    """Plots the time series of infected cases."""
    
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))
    ax.plot(infected, color='#AA0000', linestyle='dashed', marker='o')
    ax.set_xlabel('Day', fontsize=day_fontsize)
    ax.set_ylabel('Number of Infected Cases', fontsize=infected_cases_fontsize)
    ax.set_title('Simulated Oubreak', fontsize=outbreak_test_fontsize)
    ax.grid(alpha=axis_brightness)
    return fig
