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

def resample():
    path = 'C:/Users/siris/OneDrive/Desktop/Documents/GitHub/Digit_ASR/Source/KLEF_Digit_Data/KLEF_Digit_Data/train/'
    os.mkdir('C:/Users/siris/OneDrive/Desktop/Documents/GitHub/Digit_ASR/Source/KLEF_Digit_Data/KLEF_Digit_Data/train_16k')
    a = 'C:/Users/siris/OneDrive/Desktop/Documents/GitHub/Digit_ASR/Source/KLEF_Digit_Data/KLEF_Digit_Data/train_16k'
    flag = 0
    for i in track(os.listdir(path)):
        print("entering into 1st loop")
        if flag==1:
            break
        flag+=1
        os.mkdir(f"{a}/{i}")
        count = 0
        for j in os.listdir(f"{path}/{i}/"):
            if count==1:
                break
            audio_file = f"{path}/{i}/{j}"
            samples, sample_rate = librosa.load(audio_file)
            samples = librosa.resample(samples, sample_rate, 16000)
            destination_path = f"{a}/{i}/{j}"
            file_name = os.path.basename(destination_path)
            ans = os.path.splitext(file_name)[0]
            for i in ans:
                if 97<=ord(i)<=122:
                    ans = ans.replace(i, chr(ord(i)-32))
                    new_file_name = f"{a}/{i}/{ans}"
                    f = open(new_file_name, 'x')
                    sf.write(new_file_name, samples, 16000)
                    # basename = os.path.basename(destination_path)
                    count+=1

                f = open(destination_path, 'x')
                sf.write(destination_path, samples, 16000)
                # basename = os.path.basename(destination_path)
                count+=1
resample()
