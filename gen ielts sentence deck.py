import genanki
import json
from pathlib import Path

deck_name = 'ielts sentence'
my_model = genanki.Model(
    2033507265,  #随机唯一id: import random; print(random.randrange(1 << 30, 1 <<h1 31))
    deck_name + 'model',
    fields=[
        {
            'name': 'english'
        },
        {
            'name': 'chinese'
        },
        {
            'name': 'audio'
        },
    ],
    templates=[
        {
            'name': 'listen sentence',
            'qfmt': '<h1>{{audio}}</h1>',  # AND THIS
            'afmt':
            '{{FrontSide}}<br><h1>{{english}}</h1><br><h2>{{chinese}}<h2>',
        },
    ],
    css='h1, h2{text-align: center;}')

my_deck = genanki.Deck(2059423110, deck_name)
my_package = genanki.Package(my_deck)


def parse_word_format():
    #这是处理原版格式的, 不用这个了, 用sentences.json
    with open("./data/IELTS/words_chinese_google.json", 'r',
              encoding='utf-8') as file:
        data = json.load(file)
        for i in data:
            audio_path = './data/IELTS/crawler/' + data[i]['audios'][0]
            path = Path(audio_path)
            if not path.is_file():  #检测是否存在缺失的音频文件
                print(path)
                continue
            my_note = genanki.Note(
                model=my_model,
                fields=[
                    data[i]['sentences'][0], data[i]['chinese']['google'][0],
                    '[sound:{}]'.format(data[i]["audios"][0].split('/')[1])
                ])
            my_deck.add_note(my_note)
            my_package.media_files.append(audio_path)


def parse_sentence_format():
    with open("./data/IELTS/sentences.json", 'r', encoding='utf-8') as file:
        data = json.load(file)
        for key in data:
            audio_path = data[key]['audio_path']
            if not Path(audio_path).is_file():  #检测是否存在缺失的音频文件
                print(audio_path)
                continue
            my_note = genanki.Note(model=my_model,
                                   fields=[
                                       key, data[key]['chinese']['google'],
                                       f'[sound:{Path(audio_path).name}]'
                                   ])
            my_deck.add_note(my_note)
            my_package.media_files.append(audio_path)


parse_sentence_format()

my_package.write_to_file(f'./output/{deck_name}.apkg')
