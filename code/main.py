import os
import librosa
import soundfile as sf
from rich.progress import track

path = 'C:/Users/siris/OneDrive/Desktop/Documents/GitHub/Digit_ASR/Source/KLEF_Digit_Data/KLEF_Digit_Data/train'

def get_total_speakers():
    total_speakers = len(os.listdir(path))
    print(total_speakers)

# get_total_speakers()

def get_total_samples():
    total_samples = 0
    for i in os.listdir(path):
        total_samples += len(os.listdir(f"{path}/{i}/"))
    print(total_samples)

 # get_total_samples()

def get_total_F_speakers():
    total_F_speakers = 0
    for i in os.listdir(path):
        if 'F' in i:
            total_F_speakers+=1
    print(total_F_speakers)

# get_total_F_speakers()

def get_total_M_speakers():
    total_M_speakers = 0
    for i in os.listdir(path):
        if 'M' in i:
            total_M_speakers+=1
    print(total_M_speakers)

# get_total_M_speakers()

def format(string):
    if string.isupper():
        ans = string
    else:
        ans = string.upper()
    return ans

def resample():

    path = 'C:/Users/siris/OneDrive/Desktop/Documents/GitHub/Digit_ASR/Source/KLEF_Digit_Data/KLEF_Digit_Data/train/'
    os.mkdir('C:/Users/siris/OneDrive/Desktop/Documents/GitHub/Digit_ASR/Source/KLEF_Digit_Data/KLEF_Digit_Data/train_16k')
    a = 'C:/Users/siris/OneDrive/Desktop/Documents/GitHub/Digit_ASR/Source/KLEF_Digit_Data/KLEF_Digit_Data/train_16k'

    flag = 0
    count = 0
    for i in track(os.listdir(path)):
        print("inside first loop")
        if flag == 1:
            break
        flag+=1
        for j in os.listdir(f"{path}/{i}/"):
            print("inside secound loop")
            if count == 1:
                break
            count+=1
            audio_file = f"{path}/{i}/{j}"
            print("extracted aduio file")
            samples, sample_rate = librosa.load(audio_file)
            print("loaded audio file")
            samples = librosa.resample(samples, sample_rate, 16000)
            print("resampleing done")
            file_name = format(f"{path}/{i}/{j}".split()[0])
            print(f"{path}/{i}/{j}"[0])
            print(f"{path}/{i}/{j}")
            print("extracted file_name ----->", file_name)
            ext = f"{path}/{i}/{j}"[1]
            print("extracted file name extention ---->", ext)
            file_name = file_name + ext
            print("concatinatced ---->", file_name)
            destination_path = f"{a}/{i}/{file_name}"
            f = open(destination_path, "x")
            sf.write(destination_path, samples, 16000)

resample()
