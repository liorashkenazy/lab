import matplotlib as mpl
import matplotlib.pyplot as plt
import mne
import mne.viz
import numpy as np
# For eliminating warnings
from warnings import simplefilter


# ignore all future warnings from MNE
mne.set_log_level(verbose="ERROR")


def plot_raw_data(recording):
    recording.plot()
    plt.show()


def plot_psd(recording: mne.io.Raw, fmin=0, fmax=np.inf, channels='all', disp=False):
    """Plot the psd of raw data

        Args:
            recording: raw data
            fmin: the lower band on frequencies of interest [float]
            fmax: the upper band on frequencies of interest [float]
            channels: channels to include. can be string or list of strings
            disp: if True, plot the psd

        """
    fig = recording.compute_psd(fmin=fmin, fmax=fmax, picks=channels).plot()
    if type(channels) == list:
        channels = " ,".join(channels)
    fig.axes[0].set_title("Power Spectrum of " + channels + " Channel/s")
    # TODO: add legend
    if disp:
        plt.show()


def spectrogram(record):
    sfreq = record.info['sfreq']
    data, times = record['Cz']
    f, t, Sxx = mne.time_frequency.psd_multitaper()
    plt.pcolormesh(t, f, Sxx)
    plt.ylabel('Frequency (Hz)')
    plt.xlabel('Time (s)')
    plt.show()
