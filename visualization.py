import matplotlib as mpl
import matplotlib.pyplot as plt
import mne
import mne.viz
import numpy as np
# For eliminating warnings
from warnings import simplefilter

import scipy.signal
from mne.time_frequency import psd_multitaper, multitaper, tfr_multitaper

# ignore all future warnings from MNE
mne.set_log_level(verbose="ERROR")


def plot_raw_data(raw):
    raw.plot()
    plt.show()


def psd(raw: mne.io.Raw, f_min=0, f_max=np.inf, channels='all', disp=False):
    """Plot the psd of raw data

        Args:
            raw: raw data
            f_min: the lower band on frequencies of interest [float]
            f_max: the upper band on frequencies of interest [float]
            channels: channels to include. can be string or list of strings
            disp: if True, plot the psd

        """
    fig = raw.compute_psd(fmin=f_min, fmax=f_max, picks=channels).plot()
    if type(channels) == list:
        fig.axes[0].legend(channels, loc='center right')
        channels = " ,".join(channels)
    fig.axes[0].set_title("Power Spectrum of " + channels + " Channel/s")
    # TODO: add legend
    if disp:
        plt.show()


def spectrogram(raw: mne.io.Raw, channel: str, f_min=0, f_max=np.inf, t_min=None, t_max=None, disp=False):
    """Plot the spectrogram of raw data

        Args:
            raw: raw data
            f_min: the lower band on frequencies of interest [float]
            f_max: the upper band on frequencies of interest [float]
            t_min: first time in seconds to include [float]
            t_max: last time in seconds to include [float]
            channel: channels to include
            disp: if True, plot the spectrogram

        """

    # Convert Raw object to numpy array and convert from Volt to micro-Volt
    data = raw.get_data(picks=channel, tmin=t_min, tmax=t_max).flatten()
    fs = raw.info['sfreq']
    f, t, Sxx = scipy.signal.spectrogram(data, fs=fs)
    freq_range = np.ravel((f >= f_min) & (f <= f_max))
    # time_range = np.ravel((t >= t_min) & (t <= t_max))
    # Convert to dB
    Sxx = 10 * np.log10(Sxx[freq_range, :])
    plt.pcolormesh(t, f[freq_range], Sxx, cmap='jet')
    cbar = plt.colorbar()  # with a color bar
    cbar.ax.set_ylabel("Power Spectra [dB]")
    plt.ylabel('Frequency (Hz)')
    plt.xlabel('Time (s)')
    if disp:
        plt.show()

