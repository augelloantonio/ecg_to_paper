import numpy as np

def movingAverageMean(data, size):
    """
    Moving average mean filter.

    * ARGS:
    - data: raw ecg as list
    - size: the size of the window to run

    * Returns:
    - moving_averages: the moving average signal as list
    """

    newData = []
    for i in data:
        newData.append(i)

    i = 0
    moving_averages = []

    while i < len(newData)-size+1:
        this_window = data[i: i+size]
        window_average = np.sum(this_window) / size

        val = newData[i]-window_average
        moving_averages.append(val)

        i += 1

    # moving_averages = np.nan_to_num(moving_averages, nan=0.0)

    return moving_averages