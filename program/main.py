# -*- coding: utf-8 -*-
import readJson
import morphological_analysis
import watson


def main():
    # JSONデータ取得。事前にやるので今回は不要。
    json_data = readJson.read_json('#ファイルパス')
    print(json_data)

    # Assistantに投げるデータを取得
    text_data = morphological_analysis.text_analysis()
    print(text_data)

    # Assistantに投げる
    result = watson.assistant(text_data)
    print(result)

    # Assistant結果分析
    analyze_result = watson.result_analysis(result)
    total_count = analyze_result[0]['random_count'] + analyze_result[1]['development_count'] + analyze_result[2]['anime_count'] + analyze_result[3]['adult_count'] + analyze_result[4]['gourmet_count']
    print(total_count)
    print(analyze_result[1]['development_count'])
    print(analyze_result[1]['development_count'] / total_count * 100)
    print(analyze_result[2]['anime_count'] / total_count * 100)
    print(analyze_result[2]['anime_count'])
    print(analyze_result[3]['adult_count'] / total_count * 100)
    print(analyze_result[3]['adult_count'])
    print(analyze_result[4]['gourmet_count'] / total_count * 100)
    print(analyze_result[4]['gourmet_count'])
    print(analyze_result[0]['random_count'] / total_count * 100)
    print(analyze_result[0]['random_count'])


if __name__ == '__main__':
    main()
