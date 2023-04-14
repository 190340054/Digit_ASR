import os
from rich.progress import track
import librosa
import soundfile as sf
from rich.progress import track
import eng_to_ipa as p
from scipy.io import wavfile
import scipy
import wave

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
    var = string.split('.')[0]
    ext = string.split('.')[1]
    if var.isupper():
        ans = string
    else:
        ans = var.upper() + '.' + ext
    return ans


def resample():
    """
    loading audio wave files with original sampling rate
    and resampling it to 16000, saving all files into label folder
    """
    path = 'C:/Users/siris/OneDrive/Desktop/Documents/GitHub/Digit_ASR/Source/KLEF_Digit_Data/KLEF_Digit_Data/train/' #loading original .wav files path
    a = 'C:/Users/siris/OneDrive/Desktop/Documents/GitHub/Digit_ASR/Source/KLEF_Digit_Data/KLEF_Digit_Data/train_16k' # storing new folder directory into a variable for future use
    os.mkdir(f"C:/Users/siris/OneDrive/Desktop/Documents/GitHub/Digit_ASR/Source/KLEF_Digit_Data/KLEF_Digit_Data/train_16k") #creating new directory called train_16k
    # flag = 0
    # count = 0
    for i in track(os.listdir(path)): # iterate through all folders(each speaker)
        # print("inside first loop")
        # if flag == 1:
            # break
        # flag+=1
        os.mkdir(f"C:/Users/siris/OneDrive/Desktop/Documents/GitHub/Digit_ASR/Source/KLEF_Digit_Data/KLEF_Digit_Data/train_16k/{i}") #creating each speaker folder inside train_16k folder
        for j in os.listdir(f"{path}/{i}/"): #iterate through each audio file
            # print("inside secound loop")
            # if count == 1:
                # break
            # count+=1
            file_name = os.path.basename(f"{path}/{i}/{j}") # extracting file name of audio file suing basename function
            sample_name = format(file_name) # calling format function for formatting the audio file name (lowercase to uppercase)
            destination_path = f"{a}/{i}/{sample_name}" # setting destination_path
            samples, sample_rate = librosa.load(f"{path}/{i}/{j}", mono = True) #loading audio file using librosa. It returns samples and sampleing rate of audio file
            samples = librosa.resample(samples, sample_rate, 16000) #resampling samples into 16000 per sec
            f = open(destination_path, "x") # opening the destination directory for storing .wav file
            sf.write(destination_path, samples, 16000) #writing .wav file into destination path using soundfile pacakage

# resample()

def get_last_digit(s):
    """
    input type : string
    return type : string, string
    function for extractig digit from audio file_name and returning a string as file_name.txt
    """
    ext = s.split('.')[0]
    ext = ext + '.txt'
    d = s.split('.')[0][-1]
    if d == ' ':
        d = s.split('.')[0][-2]
    return d, ext


def labeling():
    hash = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    path = 'C:/Users/siris/OneDrive/Desktop/Documents/GitHub/Digit_ASR/Source/KLEF_Digit_Data/KLEF_Digit_Data/train/'
    os.mkdir(f"C:/Users/siris/OneDrive/Desktop/Documents/GitHub/Digit_ASR/Source/KLEF_Digit_Data/KLEF_Digit_Data/label")
    # flag = 0
    for i in track(os.listdir(path)):
        # print("inside first loop")
        # if flag == 1:
            # break
        # flag+=1
        # count = 0
        os.mkdir(f"C:/Users/siris/OneDrive/Desktop/Documents/GitHub/Digit_ASR/Source/KLEF_Digit_Data/KLEF_Digit_Data/label/{i}")
        a = f"C:/Users/siris/OneDrive/Desktop/Documents/GitHub/Digit_ASR/Source/KLEF_Digit_Data/KLEF_Digit_Data/label"
        for j in os.listdir(f"{path}{i}/"):
            # print("inside secound loop")
            # if count == 1:
                # break
            # count+=1
            file_name = os.path.basename(f"{path}{i}/{j}")
            digit, txt_name = get_last_digit(file_name)
            digit = int(digit)
            l_destination_path = f"{a}/{i}/{txt_name}"
            for val in range(len(hash)):
                if val == digit:
                    ans = hash[val]
                    break
            f = open(l_destination_path, 'x')
            f.write(file_name[:len(file_name)-4] + "    ")
            f.write(ans)

# labeling()

def get_file_name(string):
    return string.split('.')[0]


def phonemes():
    # sys.stdin.reconfigure(encoding='utf-8')
    path = ('C:/Users/siris/OneDrive/Desktop/Documents/GitHub/Digit_ASR/Source/KLEF_Digit_Data/KLEF_Digit_Data/label/')
    os.mkdir(f"C:/Users/siris/OneDrive/Desktop/Documents/GitHub/Digit_ASR/Source/KLEF_Digit_Data/KLEF_Digit_Data/phonemes")
    # flag = 0
    for i in os.listdir(path):
        # if flag == 1:
            # break
        # flag += 1
        # count = 0
        os.mkdir(f"C:/Users/siris/OneDrive/Desktop/Documents/GitHub/Digit_ASR/Source/KLEF_Digit_Data/KLEF_Digit_Data/phonemes/{i}")
        a = f"C:/Users/siris/OneDrive/Desktop/Documents/GitHub/Digit_ASR/Source/KLEF_Digit_Data/KLEF_Digit_Data/phonemes"
        for j in os.listdir(f"{path}{i}/"):
            # if count == 1:
                # break
            # count += 1
            file_name = os.path.basename(f"{path}{i}/{j}")
            phone_name = get_file_name(file_name)
            phonemized = p.convert(open(f"{path}{i}/{j}", "r"))
            # print(phonemized)
            p_destination_path = f"{a}/{i}/{phone_name}"
            f = open(p_destination_path, 'x', encoding="utf-8")
            f.write(file_name[:len(file_name)-4] + "    ")
            f.write(phonemized)

# phonemes()

def lexicon():
    y = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    lis = []
    for i in y:
        lis.append(p.convert((i, "r")))
    print(lis)

# lexicon()
# fs = wavfile.read("C:/Users/siris/OneDrive/Desktop/Documents/GitHub/Digit_ASR/Source/KLEF_Digit_Data/KLEF_Digit_Data/train_16k/V01_F02_U_D/V01_F02_U1_D0.wav")
# print(fs[0])
# print(type(fs[0]))
# print(type(str(fs[0])))
# print(data)


def transcrption_sample_data():
    hash = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    path = 'C:/Users/siris/OneDrive/Desktop/Documents/GitHub/Digit_ASR/Source/KLEF_Digit_Data/KLEF_Digit_Data/train_16k/'
    os.mkdir(f"C:/Users/siris/OneDrive/Desktop/Documents/GitHub/Digit_ASR/Source/KLEF_Digit_Data/KLEF_Digit_Data/transcrption_sample_data")
    # flag = 0
    for i in track(os.listdir(path)):
        # print("inside first loop")
        # if flag == 1:
            # break
        # flag+=1
        # count = 0
        os.mkdir(f"C:/Users/siris/OneDrive/Desktop/Documents/GitHub/Digit_ASR/Source/KLEF_Digit_Data/KLEF_Digit_Data/transcrption_sample_data/{i}")
        a = f"C:/Users/siris/OneDrive/Desktop/Documents/GitHub/Digit_ASR/Source/KLEF_Digit_Data/KLEF_Digit_Data/transcrption_sample_data"
        for j in os.listdir(f"{path}{i}/"):
            # print("inside secound loop")
            # if count == 1:
                # break
            # count+=1
            file_name = os.path.basename(f"{path}{i}/{j}")
            audio_file = f"{path}{i}/{j}"
            # print(file_name)
            digit, txt_name = get_last_digit(file_name)
            digit = int(digit)
            l_destination_path = f"{a}/{i}/{txt_name}"
            for val in range(len(hash)):
                if val == digit:
                    ans = hash[val]
                    break
            f = open(l_destination_path, 'x')
            frame_rate = scipy.io.wavfile.read(f"{path}{i}/{j}")
            f_r = str(frame_rate[0])
            with wave.open(audio_file) as mywav:
                duration_seconds = mywav.getnframes() / mywav.getframerate()
            # print(f_r, type(f_r))
            # print(duration_seconds, type(duration_seconds))
            f.write("sample_rate     time_period   start_time     end_time     sample_name")
            f.write("\n")
            f.write(f_r+"           "+ str(duration_seconds) +       "       0                15        SIL")
            f.write("\n")
            f.write(f_r +"           "+ str(duration_seconds) +          "       15             "+str(int((int(f_r))*duration_seconds)-15)+ "        "+str(ans))
            f.write("\n")
            f.write(f_r +"           "+ str(duration_seconds)  +"      "+str(int((int(f_r))*duration_seconds)-15) + "            " +str(int((int(f_r))*duration_seconds))+"         SIL")

# transcrption_sample_data()

def get_time_duration():
    path = 'C:/Users/siris/OneDrive/Desktop/Documents/GitHub/Digit_ASR/Source/KLEF_Digit_Data/KLEF_Digit_Data/train_16k/'
    lis = []
    for i in track(os.listdir(path)):
        for j in os.listdir(f"{path}{i}/"):
            frame_rate = scipy.io.wavfile.read(f"{path}{i}/{j}")
            time_duration = frame_rate[0]//16000
            lis.append(time_duration)
    print("max --->",max(lis))
    print("min --->",min(lis))

# get_time_duration()

# import wave
# with wave.open("C:/Users/siris/OneDrive/Desktop/Documents/GitHub/Digit_ASR/Source/KLEF_Digit_Data/KLEF_Digit_Data/train_16k/V01_F02_U_D/V01_F02_U1_D0.wav") as mywav:
#     duration_seconds = mywav.getnframes() / mywav.getframerate()
#     print(f"Length of the WAV file: {duration_seconds:.1f} s")
