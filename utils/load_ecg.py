import numpy as np
import pandas as pd 
import wfdb

def load_ecg(path, file_name, format, seconds_start, seconds_stop, sampling_rate, channel=0):

    file_path = path + file_name
    ecg = []
    if seconds_start == 0:
        seconds_start = 1

    sec_start = seconds_start*sampling_rate
    sec_stop = seconds_stop*sampling_rate

    if format == "txt":
        ecg = np.genfromtxt(file_path, delimiter=',')
        ecg = ecg[sec_start:sec_stop]
    elif format == "csv":
        df = pd.read_csv(file_path, sep=';')
        ecg = df['data']
        ecg = ecg[sec_start:sec_stop]
    elif format == "dat":
        hospital_record_file_no_extension = file_path[:len(file_path)-4]
        record = wfdb.rdrecord(hospital_record_file_no_extension, sampfrom=sec_start, sampto=sec_stop, channels=[channel])
        ECG = np.array(record.p_signal)
        ecg = [i for i in np.ravel(ECG)]
    elif format == "ecg":
        ecg = np.genfromtxt(file_path, delimiter=',')
        ecg = ecg[sec_start:sec_stop]

    return ecg