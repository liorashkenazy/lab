import mat73
import mne.io
import numpy as np
import pandas as pd

from band_power import *

MONT = mne.channels.make_standard_montage("standard_1020")


def handling_recording(file_name: str):
    """Segment the data of an entire recording to trial conditions

    Args:
        file_name: name of the file to be loaded

    Returns:
        A dictionary representing the recording
        The dictionary contains the following keys:
        "category": [int] represent the type of the recording. 0 - proband, 1 - relative, 2 - healthy
        "channels": [list[str]] all channels names
        "fs": [float] sampling rate in Hz
        "data": [DataFrame] the data from the recording where each row is the data from different electrode.

    """
    # Loading file
    data_set = mat73.loadmat(file_name)['cln']
    
    # Set recording parameters in a dictionary
    recording_dict = {"category": 0 if "_pro_" in file_name else 1 if "_rel_" in file_name else 2,
                      "channels": [x["labels"] for x in data_set['chanlocs']],
                      "fs": data_set['srate']}
    recording_dict["data"] = pd.DataFrame(np.transpose(data_set['data']), columns=recording_dict["channels"])

    return recording_dict


def handling_recording_mne(file_name: str):
    """Segment the data of an entire recording to trial conditions

    Args:
        file_name: name of the file to be loaded

    Returns:
        A dictionary representing the recording
        The dictionary contains the following keys:
        "category": [int] represent the type of the recording. 0 - proband, 1 - relative, 2 - healthy
        "channels": [list[str]] all channels names
        "fs": [float] sampling rate in Hz
        "data": [DataFrame] the data from the recording where each row is the data from different electrode.

    """
    # Loading file
    data_set = mat73.loadmat(file_name)['cln']
    channels = [x["labels"] for x in data_set['chanlocs']]
    fs = data_set['srate']
    info = mne.create_info(ch_names=channels, sfreq=fs, ch_types='eeg')
    raw_data = mne.io.RawArray(data_set['data'], info)
    raw_data.set_montage(MONT)
    return raw_data
