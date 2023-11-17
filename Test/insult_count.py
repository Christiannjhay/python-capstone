import json

# Your JSON data as a string
json_data = '''
{
    "results": [
        {
            "double_negation_result": false,
            "highest_category": "Threat",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.54823303
        },
        {
            "double_negation_result": true,
            "highest_category": "Profanity",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.03592727
        },
        {
            "double_negation_result": false,
            "highest_category": "Threat",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.47119883
        },
        {
            "double_negation_result": false,
            "highest_category": "Threat",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.5721988
        },
        {
            "double_negation_result": false,
            "highest_category": "Profanity",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.47886392
        },
        {
            "double_negation_result": true,
            "highest_category": "Threat",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.112540044
        },
        {
            "double_negation_result": false,
            "highest_category": "Threat",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.19124292
        },
        {
            "double_negation_result": false,
            "highest_category": "Threat",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.056016337
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.19314334
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.06579731
        },
        {
            "double_negation_result": true,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.17718399
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.6588125
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.4398409
        },
        {
            "double_negation_result": false,
            "highest_category": "Profanity",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.059479803
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.39842087
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.33255672
        },
        {
            "double_negation_result": false,
            "highest_category": "Profanity",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.025556687
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.08479069
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.46186632
        },
        {
            "double_negation_result": true,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.2648175
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.39441586
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.51980776
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.19893374
        },
        {
            "double_negation_result": true,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.075294
        },
        {
            "double_negation_result": true,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.46716887
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.46186632
        },
        {
            "double_negation_result": false,
            "highest_category": "Profanity",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.025556687
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.08479069
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.46186632
        },
        {
            "double_negation_result": true,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.2648175
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.39441586
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.51980776
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.19893374
        },
        {
            "double_negation_result": true,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.075294
        },
        {
            "double_negation_result": true,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.46716887
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.46186632
        },
        {
            "double_negation_result": false,
            "highest_category": "Profanity",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.025556687
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.08479069
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.46186632
        },
        {
            "double_negation_result": true,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.2648175
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.39441586
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.51980776
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.19893374
        },
        {
            "double_negation_result": true,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.075294
        },
        {
            "double_negation_result": true,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.46716887
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.46186632
        },
        {
            "double_negation_result": false,
            "highest_category": "Profanity",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.025556687
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.08479069
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.46186632
        },
        {
            "double_negation_result": true,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.2648175
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.39441586
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.51980776
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.19893374
        },
        {
            "double_negation_result": true,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.075294
        },
        {
            "double_negation_result": true,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.46716887
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.46186632
        },
        {
            "double_negation_result": false,
            "highest_category": "Profanity",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.025556687
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.08479069
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.46186632
        },
        {
            "double_negation_result": true,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.2648175
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.39441586
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.51980776
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.19893374
        },
        {
            "double_negation_result": true,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.075294
        },
        {
            "double_negation_result": true,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.46716887
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.46186632
        },
        {
            "double_negation_result": false,
            "highest_category": "Profanity",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.025556687
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.08479069
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.46186632
        },
        {
            "double_negation_result": true,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.2648175
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.39441586
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.51980776
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.19893374
        },
        {
            "double_negation_result": true,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.075294
        },
        {
            "double_negation_result": true,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.46716887
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.46186632
        },
        {
            "double_negation_result": false,
            "highest_category": "Profanity",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.025556687
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.08479069
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.46186632
        },
        {
            "double_negation_result": true,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.2648175
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.39441586
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.51980776
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.19893374
        },
        {
            "double_negation_result": true,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.075294
        },
        {
            "double_negation_result": true,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.46716887
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.46186632
        },
        {
            "double_negation_result": false,
            "highest_category": "Profanity",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.025556687
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.08479069
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.46186632
        },
        {
            "double_negation_result": true,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.2648175
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.39441586
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.51980776
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.19893374
        },
        {
            "double_negation_result": true,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.075294
        },
        {
            "double_negation_result": true,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.46716887
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.46186632
        },
        {
            "double_negation_result": false,
            "highest_category": "Profanity",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.025556687
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.08479069
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.46186632
        },
        {
            "double_negation_result": true,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.2648175
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.39441586
        },
        {
            "error": "cannot access local variable 'severe_toxic_score' where it is not associated with a value"
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.19893374
        },
        {
            "error": "cannot access local variable 'severe_toxic_score' where it is not associated with a value"
        },
        {
            "double_negation_result": true,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.46716887
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.46186632
        },
        {
            "double_negation_result": false,
            "highest_category": "Profanity",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.025556687
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.08479069
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.46186632
        },
        {
            "double_negation_result": true,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.2648175
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.39441586
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.51980776
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.19893374
        },
        {
            "double_negation_result": true,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.075294
        },
        {
            "double_negation_result": true,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.46716887
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
