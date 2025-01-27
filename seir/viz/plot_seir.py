import matplotlib.pyplot as plt


def plot_results(infected : list, day_fontsize : int = 16, infected_cases_fontsize : int = 16, 
    outbreak_test_fontsize : int = 20, axis_brightness : float = 0.2 , x_axis_label_name : str = 'Day' ,
    y_axis_label_name : str = "Number of Infected Cases",  plot_title : str = "Simulated Outbreak",
    plot_color : str = '#AA0000', plot_line_style : str = 'dashed', data_marker : str = 'o',
    plot_width : float = 10, plot_height : float = 6
    ):
    
    """Plots the time series of infected cases."""
    
    fig, ax = plt.subplots(figsize=(plot_width, plot_height))
    ax.plot(infected, color=plot_color, linestyle=plot_line_style, marker=data_marker)
    ax.set_xlabel(x_axis_label_name, fontsize=day_fontsize)
    ax.set_ylabel(y_axis_label_name, fontsize=infected_cases_fontsize)
    ax.set_title(plot_title, fontsize=outbreak_test_fontsize)
    ax.grid(alpha=axis_brightness)
    return fig
