from monkeylearn import MonkeyLearn
ModelID= 'ex_zU4txsUn'
MonkeyLearnAPIKey= '09c96df13fe78cfbf8ae9b56a824cf8106640d14'

ml = MonkeyLearn('[MonkeyLearnAPIKey]')
model_id = '[ModelID]'
data = ['first text', {'text': 'the meeting is at 10 AM', 'external_id': 'ANY_ID'}, '']
response = ml.extractors.extract(ModelID, data=data)
print(response.body)


'''response example (format to be noticed)

[
    {
        "text": "first text",
        "external_id": null,
        "error": false,
        "extractions": []
    }, {
        "text": "the meeting is at 10 AM",
        "external_id": "ANY_ID",
        "error": false,
        "extractions": [{
            "extracted_text": "10 AM",
            "tag_name": "TIME",
            "parsed_value": "10:00:00",
            "offset_span": [18, 22]
        }]
    }, {
        "text": "",
        "external_id": null,
        "error": true,
        "error_detail": "Invalid text, empty strings are not allowed",
        "extractions": null
    }
]

'''