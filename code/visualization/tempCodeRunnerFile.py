
    ax.set_ylim(-2, 52)
    ax.set_xticks(range(0, 55, 10))
    ax.set_yticks(range(0, 55, 10))
    ax.xaxis.set_minor_locator(plt.MultipleLocator(1))
    ax.yaxis.set_minor_locator(plt.MultipleLocator(1))
    ax.grid(True, which='both', axis='both', linestyle='-', color='gray', linewidth=0.5)
    ax.tick_params(