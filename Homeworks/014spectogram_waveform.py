from scipy.io import wavfile
import matplotlib.pyplot as pyplot
sampling_frequency, signal_data = wavfile.read('sample_for_task_013.wav')
# duration = len(signal_data)/ sampling_frequency

pyplot.subplot(311) # three rows, one col,1st plot
pyplot.specgram(signal_data, Fs = sampling_frequency)
pyplot.title('Some spectogram')
pyplot.xlabel('duration (s)')
pyplot.ylabel('Frequency (Hz)')

pyplot.subplot(313) # three rows, one col,3rd plot
pyplot.plot(signal_data)
pyplot.title('Some waveform')
pyplot.xlabel('duration')
pyplot.ylabel('intensity')
pyplot.show()
