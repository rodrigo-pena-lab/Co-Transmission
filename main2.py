import brian2 as b2
import numpy as np
import seaborn as sns
import pandas as pd
from simulation.index import simulate_cotrans_net
import matplotlib.pyplot as plt
import logging
from helpers.save_plot_with_timestamp import save_plot_with_timestamp
import traceback
import datetime
from helpers.save_run_info_with_timestamp import save_run_info_with_timestamp
# Set up logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def main():
    logger.info("Starting main simulation")
    fig = simulate_cotrans_net()
    save_plot_with_timestamp(fig, 'heatmaps_cotrans.pdf')
    save_plot_with_timestamp(fig, 'heatmaps_cotrans.png')
    plt.show()
    logger.info("All simulations completed. Showing plots.")

if __name__ == '__main__':
        main()


