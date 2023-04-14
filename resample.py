import os
import librosa

def resample():
    r_dir="C:/Users/siris/OneDrive/Desktop/Documents/GitHub/Digit_ASR/Source/KLEF_Digit_Data/KLEF_Digit_Data/train/V01_F02_U_D/V01_F02_U1_D0.wav"
    des_dir = "C:/Users/siris/OneDrive/Desktop/Documents/GitHub/Digit_ASR/Source/KLEF_Digit_Data/KLEF_Digit_Data/"
    resample_fs = 16000


    audiofile, fs = librosa.load(os.path.join(r_dir))             # Join path with wavfile
    data = librosa.resample(audiofile, fs, resample_fs)                     # Resampling to 16000 Hz
    librosa.output.write_wav(r_dir, data, resample_fs)  # Wave write after resampling


    # for dirname, _,filenames in os.walk(r_dir):
    #     filenames = sorted(filenames)
    #     for filename in filenames:
    #         sr, audio   =  wavfile.read(os.path.join(dirname,filename))  # Join path with wavfile
    #         # print(dirname,filename,sr,len(audio),audio)                  # Printing file path

resample()
