import base64
import json


def generate_audio():
    audio_file_first_pg = "MindsetFirstPageRead.mp3"
    audio_file_second_pg = "MindsetSecondPageRead.mp3"
    print("Hello World")
    audio_files = [audio_file_first_pg, audio_file_second_pg]

    audio_data = {}

    for file_path in audio_files:
        audio_data[file_path] = encode_audio(file_path)

    with open('audio_data.json', "w") as json_file:
        json.dump(audio_data, json_file, indent=4)
    # print(audio_data)
    return audio_data


def encode_audio(file_path):
    with open(file_path, 'rb') as file:
        encoded_content = base64.b64encode(file.read()).decode('utf-8')
    return encoded_content
