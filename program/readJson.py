# -*- coding: utf-8 -*-

import json
import glob


def read_json():
    # file_list = glob.glob('../slack_data/development_of_loose/*')
    # file_list = glob.glob('../slack_data/anime/*')
    # file_list = glob.glob('../slack_data/general/*')
    # file_list = glob.glob('../slack_data/adult/*')
    file_list = glob.glob('../slack_data/gourmet/*')

    data_list = []
    for file in file_list:
        try:
            # ローカルJSONファイルの読み込み
            with open(file, 'r') as f:
                data = json.load(f)
                list_obj = {'date': '', 'data': []}
                list_obj['date'] = file[-15:].replace('.json', '')
                for data_detail in data:
                    if len(data_detail['text']) > 10:
                        list_obj['data'].append(data_detail['text'])
        except json.JSONDecodeError as e:
            print('JSONDecodeError: ', e)
        finally:
            data_list.append(list_obj)
            f.close()

    fw = open('gourmet.json', 'w')
    # fw = open('adult.json', 'w')
    # fw = open('general.json', 'w')
    # fw = open('anime.json', 'w')
    # fw = open('development_of_loose.json', 'w')
    # json.dump関数でファイルに書き込む
    json.dump(data_list, fw, ensure_ascii=False, indent=4)
    return data_list
