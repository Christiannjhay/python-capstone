import json
import statistics

# Your JSON data as a string
json_data = '''
{
    "results": [
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": true,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.012503231
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": true,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.2191003
        },
        {
            "double_negation_result": false,
            "highest_category": "Profanity",
            "medical_term": true,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.008544922
        },
        {
            "double_negation_result": false,
            "highest_category": "Profanity",
            "medical_term": true,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.011246625
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": true,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.2922276
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": true,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.044883765
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": true,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.024378212
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": true,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.11129999
        },
        {
            "double_negation_result": true,
            "highest_category": "Sexually Explicit",
            "medical_term": true,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.081625134
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": true,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.33836752
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": true,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.20056234
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.085582085
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": true,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.1140901
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": true,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.08241652
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": true,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.015142105
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": true,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.11357342
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": true,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.083999306
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": true,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.10653123
        },
        {
            "double_negation_result": false,
            "highest_category": "Profanity",
            "medical_term": true,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.011246625
        },
        {
            "double_negation_result": true,
            "highest_category": "Sexually Explicit",
            "medical_term": true,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.102192536
        },
        {
            "double_negation_result": true,
            "highest_category": "Sexually Explicit",
            "medical_term": true,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.2922276
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": true,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.39915034
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": true,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.32236105
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": true,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.020960633
        },
        {
            "double_negation_result": true,
            "highest_category": "Sexually Explicit",
            "medical_term": true,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.009236055
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": true,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.09741997
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": true,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.03015274
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": true,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.17718399
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": true,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.15213956
        },
        {
            "double_negation_result": true,
            "highest_category": "Sexually Explicit",
            "medical_term": true,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.051563308
        },
        {
            "double_negation_result": true,
            "highest_category": "Sexually Explicit",
            "medical_term": true,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.42349213
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": true,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.25462922
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": true,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.25462922
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": true,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.056016337
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.09481675
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": true,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.032391842
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": true,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.015393426
        },
        {
            "double_negation_result": false,
            "highest_category": "Profanity",
            "medical_term": true,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.25462922
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": true,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.10175867
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": true,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.0926474
        },
        {
            "double_negation_result": true,
            "highest_category": "Sexually Explicit",
            "medical_term": true,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.11357342
        },
        {
            "double_negation_result": true,
            "highest_category": "Sexually Explicit",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.39231625
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": true,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.036870047
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": true,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.44002727
        },
        {
            "double_negation_result": true,
            "highest_category": "Sexually Explicit",
            "medical_term": true,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.3722269
        },
        {
            "double_negation_result": true,
            "highest_category": "Sexually Explicit",
            "medical_term": true,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.3048984
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": true,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.3625127
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": true,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.22579013
        },
        {
            "double_negation_result": true,
            "highest_category": "Sexually Explicit",
            "medical_term": true,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.32182294
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": true,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.033334624
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": true,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.2854937
        },
        {
            "double_negation_result": true,
            "highest_category": "Sexually Explicit",
            "medical_term": true,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.11202335
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": true,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.3389984
        },
        {
            "double_negation_result": true,
            "highest_category": "Sexually Explicit",
            "medical_term": true,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.15932569
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": true,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.14256015
        },
        {
            "double_negation_result": false,
            "highest_category": "Profanity",
            "medical_term": true,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.0201057
        },
        {
            "double_negation_result": true,
            "highest_category": "Sexually Explicit",
            "medical_term": true,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.033806015
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": true,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.022964042
        },
        {
            "double_negation_result": true,
            "highest_category": "Sexually Explicit",
            "medical_term": true,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.22579013
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": true,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.02826718
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": true,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.3389984
        },
        {
            "double_negation_result": true,
            "highest_category": "Sexually Explicit",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.07054565
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": true,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.055274166
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": true,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.27525392
        },
        {
            "double_negation_result": false,
            "highest_category": "Profanity",
            "medical_term": true,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.012880214
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": true,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.37576625
        },
        {
            "double_negation_result": false,
            "highest_category": "Profanity",
            "medical_term": true,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.01438814
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": true,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.028974265
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": true,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.034748793
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": true,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.123468354
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": true,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.20705862
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": true,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.3260917
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": true,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.15600902
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": true,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.03875561
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": true,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.37458646
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": true,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.15213956
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": true,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.041915078
        },
        {
            "double_negation_result": false,
            "highest_category": "Profanity",
            "medical_term": true,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.0103670005
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": true,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.019477395
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": true,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.20265625
        },
        {
            "double_negation_result": true,
            "highest_category": "Sexually Explicit",
            "medical_term": true,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.25462922
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": true,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.09958932
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": true,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.1996317
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": true,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.15987846
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": true,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.19029272
        },
        {
            "double_negation_result": true,
            "highest_category": "Sexually Explicit",
            "medical_term": true,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.2922276
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": true,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.24282593
        }
    ]
}
'''

# Load the JSON data
data = json.loads(json_data)

# Count occurrences of medical_term being true
count_true = sum(1 for result in data['results'] if result.get('medical_term') is True)

# Extract the underline_decision values
underline_decisions = [result.get('underline_decision', 0) for result in data['results']]

# Calculate the mean, maximum, and midpoint (median)
mean_value = statistics.mean(underline_decisions)
max_value = max(underline_decisions)
midpoint_value = statistics.median(underline_decisions)

print(f'The count of "medical_term" being true is: {count_true}')
print(f'The mean of "underline_decision" values is: {mean_value}')
print(f'The maximum "underline_decision" value is: {max_value}')
print(f'The midpoint (median) "underline_decision" value is: {midpoint_value}')
