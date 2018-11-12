# -*- coding: utf-8 -*-
from watson_developer_cloud import AssistantV1
import json

ASSISTANT = AssistantV1(
    version='2018-11-06',
    iam_apikey='apikey',
    url='https://gateway.watsonplatform.net/assistant/api'
)


def assistant(text_data):
    result_list = []
    i = 0
    for line in text_data:
        if i == 10:
            break
        if len(line.rstrip()) < 8 or 'http' in line:
            result_list.append({'intents': [{'intent': 'random', 'confidence': 0}], 'input': {'text': line.rsplit()}})
            continue

        response = ASSISTANT.message(
            workspace_id='workspace_id',
            input={'text': line.rstrip()}
        ).get_result()
        result_list.append(response)
        i += 1
    return result_list


def result_analysis(result_data):
    classifier = [
        {'random_count': 0, 'texts': []},
        {'development_count': 0, 'texts': []},
        {'anime_count': 0, 'texts': []},
        {'adult_count': 0, 'texts': []},
        {'gourmet_count': 0, 'texts': []}
    ]

    for data in result_data:
        for intents in data['intents']:
            if intents['intent'] == 'Development':
                classifier[1]['development_count'] += 1
                classifier[1]['texts'].append(data['input']['text'])
            elif intents['intent'] == 'Anime':
                classifier[2]['anime_count'] += 1
                classifier[2]['texts'].append(data['input']['text'])
            elif intents['intent'] == 'Adult':
                classifier[3]['adult_count'] += 1
                classifier[3]['texts'].append(data['input']['text'])
            elif intents['intent'] == 'gourmet':
                classifier[4]['gourmet_count'] += 1
                classifier[4]['texts'].append(data['input']['text'])
            elif intents['intent'] == 'random':
                classifier[0]['random_count'] += 1
                classifier[0]['texts'].append(data['input']['text'])
            else:
                print(intents)

    return classifier
