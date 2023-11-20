import json

# Your JSON data as a string
json_data = '''
{
    "results": [
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.8115627
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.25084448
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.85333383
        },
        {
            "double_negation_result": false,
            "highest_category": "Profanity",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.06065326
        },
        {
            "double_negation_result": false,
            "highest_category": "Threat",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.5885171
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.568186
        },
        {
            "double_negation_result": true,
            "highest_category": "Threat",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.23090743
        },
        {
            "double_negation_result": true,
            "highest_category": "Insult",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.07054565
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.32971194
        },
        {
            "double_negation_result": false,
            "highest_category": "Profanity",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.78207105
        },
        {
            "error": "cannot access local variable 'severe_toxic_score' where it is not associated with a value"
        },
        {
            "double_negation_result": true,
            "highest_category": "Insult",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.47173777
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.47119883
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.6027529
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.42129645
        },
        {
            "error": "cannot access local variable 'severe_toxic_score' where it is not associated with a value"
        },
        {
            "double_negation_result": false,
            "highest_category": "Profanity",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.83334327
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.25462922
        },
        {
            "double_negation_result": true,
            "highest_category": "Insult",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.5140397
        },
        {
            "double_negation_result": true,
            "highest_category": "Insult",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.30464804
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.6027529
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.24603334
        },
        {
            "double_negation_result": false,
            "highest_category": "Profanity",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.90451443
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.85333383
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.25462922
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.5885171
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.743089
        },
        {
            "double_negation_result": true,
            "highest_category": "Insult",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.47886392
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.72028047
        },
        {
            "double_negation_result": false,
            "highest_category": "Profanity",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.9749944
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.3722269
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.64447093
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.3666224
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.3811502
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.35186127
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.16043124
        },
        {
            "double_negation_result": false,
            "highest_category": "Profanity",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.85333383
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.8629672
        },
        {
            "double_negation_result": true,
            "highest_category": "Profanity",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.8540474
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.22712809
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.112850055
        },
        {
            "double_negation_result": true,
            "highest_category": "Threat",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.46982017
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.18744208
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.76197964
        },
        {
            "double_negation_result": true,
            "highest_category": "Insult",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.20973456
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.36095104
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.42568782
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.62136006
        },
        {
            "double_negation_result": true,
            "highest_category": "Insult",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.45921504
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.34328604
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.32971194
        },
        {
            "double_negation_result": false,
            "highest_category": "Profanity",
            "medical_term": true,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.04686289
        },
        {
            "double_negation_result": true,
            "highest_category": "Insult",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.13041082
        },
        {
            "double_negation_result": false,
            "highest_category": "Threat",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.5024724
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.15545623
        },
        {
            "double_negation_result": true,
            "highest_category": "Insult",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.8540474
        },
        {
            "double_negation_result": false,
            "highest_category": "Profanity",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.6308517
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.09828771
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.05824285
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.20839658
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.4402136
        },
        {
            "double_negation_result": false,
            "highest_category": "Profanity",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.9061063
        },
        {
            "double_negation_result": false,
            "highest_category": "Threat",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.24282593
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.8460273
        },
        {
            "double_negation_result": false,
            "highest_category": "Threat",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.44039994
        },
        {
            "double_negation_result": false,
            "highest_category": "Threat",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.24763705
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.47323486
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.7570315
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.26293078
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.059232414
        },
        {
            "double_negation_result": false,
            "highest_category": "Profanity",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.032391842
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.36095104
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.46716887
        },
        {
            "double_negation_result": false,
            "highest_category": "Threat",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.31547862
        },
        {
            "double_negation_result": false,
            "highest_category": "Profanity",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.046368107
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.3281604
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.27236435
        },
        {
            "double_negation_result": false,
            "highest_category": "Threat",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.56269526
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.2820025
        },
        {
            "double_negation_result": false,
            "highest_category": "Threat",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.6426206
        },
        {
            "double_negation_result": true,
            "highest_category": "Insult",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.28087774
        },
        {
            "double_negation_result": false,
            "highest_category": "Profanity",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.8629672
        },
        {
            "double_negation_result": false,
            "highest_category": "Profanity",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.025556687
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.37576625
        },
        {
            "double_negation_result": true,
            "highest_category": "Threat",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.6989911
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.7856813
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.28425202
        },
        {
            "double_negation_result": false,
            "highest_category": "Threat",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.17631748
        },
        {
            "error": "cannot access local variable 'severe_toxic_score' where it is not associated with a value"
        },
        {
            "double_negation_result": false,
            "highest_category": "Threat",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.6852916
        },
        {
            "double_negation_result": false,
            "highest_category": "Threat",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.37751234
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.57271194
        },
        {
            "double_negation_result": false,
            "highest_category": "Profanity",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.7856813
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.52007306
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.34328604
        },
        {
            "double_negation_result": false,
            "highest_category": "Threat",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.41168427
        },
        {
            "double_negation_result": false,
            "highest_category": "Threat",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.3286776
        },
        {
            "double_negation_result": false,
            "highest_category": "Profanity",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.2763787
        },
        {
            "double_negation_result": false,
            "highest_category": "Profanity",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.687436
        },
        {
            "double_negation_result": false,
            "highest_category": "Profanity",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.89241093
        },
        {
            "double_negation_result": false,
            "highest_category": "Threat",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.7701451
        },
        {
            "double_negation_result": false,
            "highest_category": "Profanity",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.89241093
        }
    ]
}
'''

# Load the JSON data
data = json.loads(json_data)

# Filter results where highest_category is "Insult"
insult_results = [result for result in data['results'] if result.get('highest_category') == 'Insult']

# Extract underline_decision values where highest_category is "Insult"
insult_underline_decisions = [result.get('underline_decision', 0) for result in insult_results]

# Calculate mean, min, and max for "Insult"
mean_insult = sum(insult_underline_decisions) / len(insult_underline_decisions) if len(insult_underline_decisions) > 0 else 0
min_insult = min(insult_underline_decisions) if len(insult_underline_decisions) > 0 else 0
max_insult = max(insult_underline_decisions) if len(insult_underline_decisions) > 0 else 0

# Count occurrences of "double_negation_result" being true for "Insult"
count_true = sum(1 for result in insult_results if result.get('highest_category'))

print(f"Insult:")
print(f"Mean: {mean_insult}")
print(f"Min: {min_insult}")
print(f"Max: {max_insult}")
print(f'Count of "double_negation_result" being true: {count_true}')
