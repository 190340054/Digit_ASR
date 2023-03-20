import os
from rich.progress import track
import librosa
import soundfile as sf
from rich.progress import track
import eng_to_ipa as p

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
    path = 'C:/Users/siris/OneDrive/Desktop/Documents/GitHub/Digit_ASR/Source/KLEF_Digit_Data/KLEF_Digit_Data/train/'
    a = 'C:/Users/siris/OneDrive/Desktop/Documents/GitHub/Digit_ASR/Source/KLEF_Digit_Data/KLEF_Digit_Data/train_16k'
    os.mkdir(f"C:/Users/siris/OneDrive/Desktop/Documents/GitHub/Digit_ASR/Source/KLEF_Digit_Data/KLEF_Digit_Data/train_16k")
    # flag = 0
    # count = 0
    for i in track(os.listdir(path)):
        # print("inside first loop")
        # if flag == 1:
            # break
        # flag+=1
        os.mkdir(f"C:/Users/siris/OneDrive/Desktop/Documents/GitHub/Digit_ASR/Source/KLEF_Digit_Data/KLEF_Digit_Data/train_16k/{i}")
        for j in os.listdir(f"{path}/{i}/"):
            # print("inside secound loop")
            # if count == 1:
                # break
            # count+=1
            file_name = os.path.basename(f"{path}/{i}/{j}")
            sample_name = format(file_name)
            destination_path = f"{a}/{i}/{sample_name}"
            samples, sample_rate = librosa.load(f"{path}/{i}/{j}", mono = True)
            samples = librosa.resample(samples, sample_rate, 16000)
            f = open(destination_path, "x")
            sf.write(destination_path, samples, 16000)

# resample()

def get_last_digit(s):
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
    for i in os.listdir(path):
        # print("inside first loop")
        # if flag == 1:
        #     break
        # flag+=1
        # count = 0
        os.mkdir(f"C:/Users/siris/OneDrive/Desktop/Documents/GitHub/Digit_ASR/Source/KLEF_Digit_Data/KLEF_Digit_Data/label/{i}")
        a = f"C:/Users/siris/OneDrive/Desktop/Documents/GitHub/Digit_ASR/Source/KLEF_Digit_Data/KLEF_Digit_Data/label"
        for j in os.listdir(f"{path}{i}/"):
            # print("inside secound loop")
            # if count == 1:
            #     break
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
    #     if flag == 1:
    #         break
    #     flag += 1
    # count = 0
        os.mkdir(f"C:/Users/siris/OneDrive/Desktop/Documents/GitHub/Digit_ASR/Source/KLEF_Digit_Data/KLEF_Digit_Data/phonemes/{i}")
        a = f"C:/Users/siris/OneDrive/Desktop/Documents/GitHub/Digit_ASR/Source/KLEF_Digit_Data/KLEF_Digit_Data/phonemes"
        for j in os.listdir(f"{path}{i}/"):
            # if count == 1:
            #     break
            # count += 1
            file_name = os.path.basename(f"{path}{i}/{j}")
            phone_name = get_file_name(file_name)
            phonemized = p.convert(open(f"{path}{i}/{j}", "r"))
            # print(phonemized)
            p_destination_path = f"{a}/{i}/{phone_name}"
            f = open(p_destination_path, 'x', encoding="utf-8")
            f.write(phonemized)

# phonemes()

def lexicon():
    y = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    lis = []
    for i in y:
        lis.append(p.convert((i, "r")))
    print(lis)

# lexicon()
