from monkeylearn import MonkeyLearn

ml = MonkeyLearn('[YOUR_API_KEY]')
model_id = '[MODEL_ID]'
data = ['first text', {'text': 'the meeting is at 10 AM', 'external_id': 'ANY_ID'}, '']
response = ml.extractors.extract(model_id, data=data)
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