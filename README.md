# ECG TO PAPER
Simple python script to convert a single ecg lead trace on millimetered paper.

![ECG on paper](https://github.com/augelloantonio/ecg_to_paper/blob/main/builded_images/16265.png)

## How to run

1. Clone repo or download zip from Github. 
2. Install dependencies with comand:

```
pip install -r requirements.txt
```

3. Execute main script:

```
python3 main.py
```

## Configuration
Everything you need to do is just edit config.py file settings to change the name of file you need to convert to paper, the file extension, the start and stop time wanted.

Settings are:
- INPUT_FILE_PATH = the path where the input ecg files are located, default is "ecg_files";
- FILE_NAME = the file name, default is "16265.dat" from [MIT-BIH Normal Sinus Rhythm Database v1.0.0](https://www.physionet.org/content/nsrdb/1.0.0/);
- FILE_EXTENSION = the file extension, defualt is "dat";
- OUTPUT_IMAGE_PATH = the path where the output ecg images are saved, defualt is "builded_images"
- SAMPLING_RATE = the ecg sampling rate;
- NORMALIZE_ECG = enable or not the ecg normalization, a moving mean filter will be applied to the trace;
- SECONDS_START = at which second of the trace start;
- SECONDS_STOP = at which second of the trace stop;
- CHANNEL = the channel to extract, if used;

### Useful info
The best performance are with sample of 10 seconds.
The file extension supported to now are:
- txt;
- ecg;
- dat;
- csv;

The .dat files need to have also .atr and .hea.
