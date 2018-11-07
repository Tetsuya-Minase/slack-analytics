# -*- coding: utf-8 -*-
from watson_developer_cloud import AssistantV1
import json

ASSISTANT = AssistantV1(
    version='2018-11-06',
    iam_apikey='your api key',
    url='https://gateway.watsonplatform.net/assistant/api'
)

def assistant():
    data_list = []

    try:
        with open('myText.txt', 'r') as f:
            for line in f:
                if len(line.rstrip()) < 10 or 'http' in line:
                    data_list.append({'intents': [{'intent': 'random', 'confidence': 0}], 'input': {'text': line.rsplit()}})
                    continue

                response = ASSISTANT.message(
                    workspace_id='your workspace_id',
                    input={
                        'text': line.rstrip()
                    }
                ).get_result()
                data_list.append(response)

    except Exception as e:
        print(e)
    finally:
        f.close()

    fw = open('result_assistant.json', 'w')
    json.dump(data_list, fw, ensure_ascii=False, indent=4)
    fw.close()


assistant()