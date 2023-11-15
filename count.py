import json

# Your JSON data
json_data = '''
{
    "results": [
        {
            "double_negation_result": true,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.11419344
        },
        {
            "double_negation_result": true,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.081625134
        },
        {
            "double_negation_result": true,
            "highest_category": "Profanity",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.019603057
        },
        {
            "double_negation_result": true,
            "highest_category": "Profanity",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.014513801
        },
        {
            "double_negation_result": true,
            "highest_category": "Profanity",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.021314176
        },
        {
            "double_negation_result": true,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.037577134
        },
        {
            "double_negation_result": true,
            "highest_category": "Profanity",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.01426248
        },
        {
            "double_negation_result": true,
            "highest_category": "Profanity",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.016021729
        },
        {
            "double_negation_result": true,
            "highest_category": "Profanity",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.017843807
        },
        {
            "double_negation_result": true,
            "highest_category": "Profanity",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.022374803
        },
        {
            "double_negation_result": true,
            "highest_category": "Profanity",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.014953613
        },
        {
            "double_negation_result": false,
            "highest_category": "Profanity",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.007885204
        },
        {
            "double_negation_result": false,
            "highest_category": "Profanity",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.021549871
        },
        {
            "double_negation_result": true,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.018974753
        },
        {
            "double_negation_result": true,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.019728716
        },
        {
            "double_negation_result": false,
            "highest_category": "Profanity",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.011246625
        },
        {
            "double_negation_result": true,
            "highest_category": "Profanity",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.026970858
        },
        {
            "double_negation_result": true,
            "highest_category": "Profanity",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.012943043
        },
        {
            "double_negation_result": true,
            "highest_category": "Profanity",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.022139108
        },
        {
            "double_negation_result": true,
            "highest_category": "Profanity",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.008921904
        },
        {
            "double_negation_result": true,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.030506283
        },
        {
            "double_negation_result": true,
            "highest_category": "Profanity",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.030034892
        },
        {
            "double_negation_result": true,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.023671126
        },
        {
            "double_negation_result": true,
            "highest_category": "Profanity",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.010743983
        },
        {
            "double_negation_result": true,
            "highest_category": "Profanity",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.01608456
        },
        {
            "double_negation_result": true,
            "highest_category": "Profanity",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.027677942
        },
        {
            "double_negation_result": true,
            "highest_category": "Profanity",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.017466826
        },
        {
            "double_negation_result": true,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.04834723
        },
        {
            "double_negation_result": true,
            "highest_category": "Profanity",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.020607091
        },
        {
            "double_negation_result": true,
            "highest_category": "Profanity",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.040925518
        },
        {
            "double_negation_result": false,
            "highest_category": "Profanity",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.015833238
        },
        {
            "double_negation_result": true,
            "highest_category": "Profanity",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.013382856
        },
        {
            "double_negation_result": false,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.049336795
        },
        {
            "double_negation_result": true,
            "highest_category": "Profanity",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.009173225
        },
        {
            "double_negation_result": true,
            "highest_category": "Profanity",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.01633588
        },
        {
            "double_negation_result": false,
            "highest_category": "Profanity",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.013885498
        },
        {
            "double_negation_result": true,
            "highest_category": "Profanity",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.01608456
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.028031485
        },
        {
            "double_negation_result": true,
            "highest_category": "Sexually Explicit",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.021549871
        },
        {
            "double_negation_result": true,
            "highest_category": "Profanity",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.022964042
        },
        {
            "double_negation_result": true,
            "highest_category": "Profanity",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.017592486
        },
        {
            "double_negation_result": true,
            "highest_category": "Profanity",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.012503231
        },
        {
            "double_negation_result": true,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.046368107
        },
        {
            "double_negation_result": true,
            "highest_category": "Profanity",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.29039988
        },
        {
            "double_negation_result": true,
            "highest_category": "Profanity",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.01419965
        },
        {
            "double_negation_result": true,
            "highest_category": "Profanity",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.014827953
        },
        {
            "double_negation_result": true,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.040430736
        },
        {
            "double_negation_result": true,
            "highest_category": "Profanity",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.028149333
        },
        {
            "double_negation_result": true,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.02543884
        },
        {
            "double_negation_result": true,
            "highest_category": "Profanity",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.0126288915
        },
        {
            "double_negation_result": true,
            "highest_category": "Profanity",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.019854378
        },
        {
            "double_negation_result": true,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.024378212
        },
        {
            "double_negation_result": true,
            "highest_category": "Profanity",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.015581916
        },
        {
            "double_negation_result": true,
            "highest_category": "Profanity",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.018723432
        },
        {
            "double_negation_result": true,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.054037213
        },
        {
            "double_negation_result": true,
            "highest_category": "Profanity",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.0143253105
        },
        {
            "double_negation_result": true,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.050821137
        },
        {
            "double_negation_result": true,
            "highest_category": "Profanity",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.04166769
        },
        {
            "double_negation_result": true,
            "highest_category": "Profanity",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.024613906
        },
        {
            "double_negation_result": true,
            "highest_category": "Profanity",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.017089844
        },
        {
            "double_negation_result": true,
            "highest_category": "Profanity",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.019603057
        },
        {
            "double_negation_result": true,
            "highest_category": "Profanity",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.010806813
        },
        {
            "double_negation_result": true,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.03781283
        },
        {
            "double_negation_result": true,
            "highest_category": "Profanity",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.022256956
        },
        {
            "double_negation_result": true,
            "highest_category": "Profanity",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.017969469
        },
        {
            "double_negation_result": true,
            "highest_category": "Profanity",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.022374803
        },
        {
            "double_negation_result": true,
            "highest_category": "Profanity",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.01633588
        },
        {
            "error": "cannot access local variable 'severe_toxic_score' where it is not associated with a value"
        },
        {
            "double_negation_result": true,
            "highest_category": "Profanity",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.019603057
        },
        {
            "double_negation_result": true,
            "highest_category": "Profanity",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.02449606
        },
        {
            "double_negation_result": true,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.091913216
        },
        {
            "double_negation_result": true,
            "highest_category": "Profanity",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.016838523
        },
        {
            "double_negation_result": true,
            "highest_category": "Profanity",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.03015274
        },
        {
            "double_negation_result": true,
            "highest_category": "Profanity",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.017592486
        },
        {
            "double_negation_result": true,
            "highest_category": "Profanity",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.017341165
        },
        {
            "double_negation_result": true,
            "highest_category": "Profanity",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.017969469
        },
        {
            "error": "cannot access local variable 'severe_toxic_score' where it is not associated with a value"
        },
        {
            "double_negation_result": true,
            "highest_category": "Profanity",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.015896067
        },
        {
            "error": "cannot access local variable 'severe_toxic_score' where it is not associated with a value"
        },
        {
            "double_negation_result": true,
            "highest_category": "Profanity",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.043399423
        },
        {
            "double_negation_result": true,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.11088664
        },
        {
            "double_negation_result": true,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.03781283
        },
        {
            "double_negation_result": true,
            "highest_category": "Profanity",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.019226074
        },
        {
            "double_negation_result": true,
            "highest_category": "Profanity",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.045378547
        },
        {
            "double_negation_result": true,
            "highest_category": "Profanity",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.01005285
        },
        {
            "error": "cannot access local variable 'severe_toxic_score' where it is not associated with a value"
        },
        {
            "double_negation_result": true,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.02543884
        },
        {
            "double_negation_result": true,
            "highest_category": "Profanity",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.029563503
        },
        {
            "error": "cannot access local variable 'severe_toxic_score' where it is not associated with a value"
        },
        {
            "double_negation_result": true,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.05799546
        },
        {
            "double_negation_result": true,
            "highest_category": "Profanity",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.016838523
        },
        {
            "double_negation_result": true,
            "highest_category": "Profanity",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.034984488
        },
        {
            "double_negation_result": true,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.048842013
        },
        {
            "double_negation_result": true,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.04315203
        },
        {
            "double_negation_result": true,
            "highest_category": "Profanity",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.020607091
        },
        {
            "double_negation_result": true,
            "highest_category": "Profanity",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.023671126
        },
        {
            "double_negation_result": true,
            "highest_category": "Profanity",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.014073989
        },
        {
            "double_negation_result": true,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.15324512
        },
        {
            "double_negation_result": true,
            "highest_category": "Insult",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.031684756
        },
        {
            "double_negation_result": true,
            "highest_category": "Profanity",
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.019226074
        }
    ]
}
'''

# Load the JSON data
data = json.loads(json_data)

# Count the number of entries with "double_negation_result" set to True
true_count = sum(1 for entry in data["results"] if entry.get("double_negation_result", False))

print("Number of true:", true_count)