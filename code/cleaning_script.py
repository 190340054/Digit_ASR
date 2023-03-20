import os
import librosa
from dotenv import load_dotenv
import soundfile as sf

load_dotenv()

#sample testing for correct path
# print(os.environ['train_path'])

def check_folder(path):
    """
    this is documenation space
    """
    #check does we have cleaning dir
    if os.path.isdir(path):
        #we will do something
        pass
    else:
        os.mkdir(path)
    return

def check_file_labelling(filename) -> str:
    """
    this is documenation space
    """
    filename = filename.split('.')[0]
    return f"{filename.upper()}.wav"

def resample_file(path,destination_path):
    """
    this is documenation space
    """
    try:
        print(destination_path)
        data, samplerate = librosa.load(path, mono = True)
        new_samplerate = os.environ['samplerate']
        print(path,destination_path)
        data = librosa.resample(data, samplerate, new_samplerate)
        print("writing into destination")
        sf.write(destination_path, data, new_samplerate)
        return True
    except:
        return False

def create_file(path):
    """
    this is documenation space
    """
    try :
        if os.path.isfile(path):
            print("file already exited !")
        else:
            print("creating a new file ")
            f=open(path,'x')
            f.close
        return True
    except:
        return False

def create_label(source_path,destination_path):
    hash = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    try:
        data, samplerate = sf.read(path, channels=1)
        length_data = len(date)
        f = open(destination_path,'w')
        insert_word = hash[int(basefile.split['.'][0][-1])]
        f.write(f'0\t15\tSIL\n15\t{data[15:-15]}{insert_word}\n{data[15:-15]}\t{len(data)-15}')
        f.close()
        return True
    except:
        return False

def read_files():
    """
    this is documenation space
    """
    #checking does we have clean folder or not
    # create subdir clean
    check_folder(f"{os.environ['clean_path']}")
    #create subdir label
    check_folder(f"{os.environ['label_path']}")
    destination_path = os.environ['clean_path']
    for i in os.listdir(os.environ['train_path']):
        check_folder(f"{os.environ['clean_path']}{i}")
        for j in os.listdir(f"{os.environ['train_path']}{i}"):
            # checking for filr name format
            file_name = check_file_labelling(j)
            #create destination_file in destination path
            destination_path +=f"/{file_name}"
            print(destination_path)
            create_file(destination_path)
            print("created a file")
            #resampleing
            print(f"{os.environ['train_path']}{i}/{j}")
            resample_file(f"{os.environ['train_path']}{i}/{j}",destination_path)
            print("done resampleing")
            #create sub folder in label dir
            check_folder(f"{os.environ['label_path']}/{i}")
            # create label
            label_destination_file = f"{os.environ['label_path']}/{i}/{file_name.split('.')[0]}.txt"
            create_file(label_destination_file)
            print("create a file",label_destination_file)
            #write content in the file
            create_label(f"{os.environ['train_path']}{i}/{j}",label_destination_file)
            print("done labelling")











read_files()
