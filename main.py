import matplotlib.pyplot as plt
import mne
from utils import handling_recording, handling_recording_mne
from visualization import plot_raw_data, plot_psd, spectrogram

if __name__ == "__main__":
    # TODO: add the option to get folder from command line arg + channel str
    #folder_dir = sys.argv[1]
    folder_dir = r"C:\Users\lashkenazy\OneDrive - post.bgu.ac.il\lab\recordings"
    recording = handling_recording_mne(folder_dir + "\sz_pro_0421_102409_RestEyesOpen_AA_1_cln.mat")
    ch_names = recording.ch_names
    fmax = 50  # Max frequency for psd calculation
    spectrogram(recording)
    # # Plot psd of all channels in single plot
    # plot_psd(recording, fmax=fmax)
    # # Plot psd of each channel separately
    # for channel in ch_names:
    #     plot_psd(recording, fmax=fmax, channels=channel)
    # plt.show()
    #
#     table_values = []
#     i = 1
#     # iterate over files in folder_dir directory
#     for filename in os.listdir(folder_dir):
#         f = os.path.join(folder_dir, filename)
#         # checking if it is a file
#         if os.path.isfile(f):
#             files.append(f)
#             # table_values.append(handling_recording(f, channel, i))
#             i = i + 1
#     # plot_table(table_values, channel)