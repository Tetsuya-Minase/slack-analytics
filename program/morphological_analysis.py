# -*- coding: utf-8 -*-
import json
import MeCab

def analysis():
    mecab = MeCab.Tagger("-Ochasen")
    try:
        # 結果ファイル用
        result_file = open('result_gourmet.txt', 'w')
        result_data = [];
        # ローカルJSONファイルの読み込み
        # with open('development_of_loose.json', 'r') as f:
        # with open('anime.json', 'r') as f:
        # with open('general.json', 'r') as f:
        # with open('adult.json', 'r') as f:
        with open('gourmet.json', 'r') as f:
            data = json.load(f)
            for data_line in data:
                for text_data in data_line['data']:
                    # urlと100文字以上はいらなそう
                    if 'http' in text_data or len(text_data) > 100:
                        # print(text_data)
                        continue

                    parse_data = mecab.parse(text_data)

                    # 動詞と名詞が無ければ一旦捨てる
                    if '動詞' not in parse_data or '名詞' not in parse_data:
                        continue

                    result_data.append(text_data)

        file_data = '\n'.join(map(str, result_data))
        result_file.write(file_data)
    except json.JSONDecodeError as e:
        print('JSONDecodeError: ', e)
    finally:
        f.close()
        result_file.close()

def textAnalysis():
    mecab = MeCab.Tagger("-Ochasen")
    try:
        # 結果ファイル用
        result_file = open('result_mytext.txt', 'w')
        result_data = [];
        # ローカルJSONファイルの読み込み
        with open('myText.txt', 'r') as f:
            for line in f:
                # urlと100文字以上はいらなそう
                if 'http' in line or len(line) > 100 or len(line) < 10:
                    print(line)
                    continue

                parse_data = mecab.parse(line)

                # 動詞と名詞が無ければ一旦捨てる
                if '動詞' not in parse_data or '名詞' not in parse_data:
                    print(line)
                    continue

                result_data.append(line)
        # file_data = '\n'.join(map(str, result_data))
        file_data = ''.join(result_data)
        result_file.write(file_data)
    except json.JSONDecodeError as e:
        print('JSONDecodeError: ', e)
    finally:
        f.close()
        result_file.close()

analysis()
# textAnalysis()