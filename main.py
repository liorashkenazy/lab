import matplotlib.pyplot as plt
import mne
from utils import handling_recording, handling_recording_mne
from visualization import plot_raw_data, psd, spectrogram
import os

if __name__ == "__main__":
    # TODO: add the option to get folder from command line arg + channel str
    #folder_dir = sys.argv[1]
    folder_dir = r"C:\Users\lashkenazy\OneDrive - post.bgu.ac.il\lab\recordings"
    show_power_spectrum = True
    show_table = False
    show_spectrogram = False

    recording = handling_recording_mne(folder_dir + "\sz_pro_0421_102409_RestEyesOpen_AA_1_cln.mat")
    chan_names = recording.ch_names
    f_max = 40  # Max frequency for psd calculRRRRation

    if show_power_spectrum:
        # Plot psd of all channels in single plot
        psd(recording, f_max=f_max)
        # Plot psd of each channel separately
        # for channel in chan_names:
        #     psd(recording, f_max=f_max, channels=channel)
        psd(recording, f_max=f_max, channels=['Cz', 'Fp1'])
    if show_spectrogram:
        spectrogram(recording, channel=2, f_max=f_max)

    if show_table:
        table_values = []
        i = 1
        # iterate over files in folder_dir directory
        for filename in os.listdir(folder_dir):
            f = os.path.join(folder_dir, filename)
            # checking if it is a file
            if os.path.isfile(f):
                # files.append(f)
                # table_values.append(handling_recording(f, channel, i))
                i = i + 1
        # plot_table(table_values, channel)
    plt.show()
