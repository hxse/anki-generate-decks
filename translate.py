import json
from pathlib import Path


def gen_sentences():
    # 读出所有sentence
    with open("./data/IELTS/words.json", "r", encoding='utf-8') as read_file:
        data = json.load(read_file)
        sentences = [s for i in [*data] for s in data[i]['sentences']]
    # 把sentence写入txt文件里
    with open('./data/IELTS/words_sentences.txt', 'w',
              encoding='utf-8') as write_file:
        write_file.write('\n'.join(sentences))


def mer_translate():
    #把翻译合并到数据并生成新的json
    ## 读取翻译数据
    with open('./data/IELTS/words.json', 'r', encoding='utf-8') as json_file:
        json_data = json.load(json_file)
        ## 合并数据
        with open("./data/IELTS/words_chinese_google.json",
                  "w",
                  encoding='utf-8') as write_file:
            with open('./data/IELTS/translate_chinese_goole.txt',
                      'r',
                      encoding='utf-8') as translate_file:
                for key in json_data:
                    json_data[key]['chinese'] = {}
                    json_data[key]['chinese']['google'] = []
                    for i in json_data[key]['sentences']:
                        json_data[key]['chinese']['google'] = [
                            *json_data[key]['chinese']['google'],
                            translate_file.readline().strip()
                        ]
                json.dump(json_data, write_file, ensure_ascii=False, indent=4)


def create_chinese_google():
    #creat_chinese_google for dir
    with open('./data/IELTS/words_chinese_google.json', 'r',
              encoding='utf-8') as json_file:
        json_data = json.load(json_file)
        json_data = {
            v['sentences'][i]: v['chinese']['google'][i]
            for k, v in json_data.items() for i in range(len(v['sentences']))
        }
        print(len(json_data))

    data_all = {}
    for i in range(198):
        text_path = f'./data/IELTS/crawler/{i}/{i}'
        out_path = f'./data/IELTS/crawler/{i}/{i}_chinese_google.txt'
        with open(text_path, 'r', encoding='utf8') as read_file:
            data = []
            for i2, line in enumerate(read_file.readlines()):
                i2 += 1
                line = line.strip()
                mp3_path = f'data/IELTS/crawler/{i}/{i}_{str(i2).zfill(3)}.mp3'
                data.append(json_data[line])
                data_all[line] = {
                    'chinese': {
                        'google': json_data[line]
                    },
                    'audio_path': mp3_path
                }
                with open(out_path, 'w', encoding='utf8') as write_file:
                    write_file.write('\n'.join(data))
    out_all_path = f'./data/IELTS/sentences.json'
    with open(out_all_path, 'w', encoding='utf-8') as file:
        json.dump(data_all, file, ensure_ascii=False, indent=4)
    print(len(data_all))
