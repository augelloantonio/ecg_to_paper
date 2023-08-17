import numpy as np
import utils.plot as ecg_plot
import utils.load_ecg as ecg_loader
from config import SETTINGS

ecg = ecg_loader.load_ecg(SETTINGS.INPUT_FILE_PATH, SETTINGS.FILE_NAME, SETTINGS.FILE_EXTENSION, SETTINGS.SECONDS_START,SETTINGS.SECONDS_STOP, SETTINGS.SAMPLING_RATE, channel = SETTINGS.CHANNEL)
ecg_plot.plot_single_lead(ecg, save_fig_path=SETTINGS.OUTPUT_IMAGE_PATH, file_name=SETTINGS.FILE_NAME, sample_rate=SETTINGS.SAMPLING_RATE, normalize_ecg=SETTINGS.NORMALIZE_ECG)