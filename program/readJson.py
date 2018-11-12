# -*- coding: utf-8 -*-

import json
import glob


def read_json(filepath):
    file_list = glob.glob(filepath)

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

    return data_list
