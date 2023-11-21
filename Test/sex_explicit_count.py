import json
import statistics

# Your JSON data as a string
json_data = '''
{
    "results": [
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.7510937
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.6289369
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.83334327
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
            "underline_decision": 0.6027529
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.45761138
        },
        {
            "double_negation_result": false,
            "highest_category": "Profanity",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.7998551
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.8299589
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.7510937
        },
        {
            "double_negation_result": false,
            "highest_category": "Profanity",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.9288007
        },
        {
            "double_negation_result": false,
            "highest_category": "Profanity",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.85850734
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
            "highest_category": "Sexually Explicit",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.7998551
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.85333383
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.7570315
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.8299589
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.85173553
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
            "highest_category": "Profanity",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.8540474
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.78855824
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.7998551
        },
        {
            "double_negation_result": true,
            "highest_category": "Profanity",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.85333383
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.8629672
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.6852916
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.85333383
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.6852916
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.6027529
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.7510937
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.8629672
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.8696708
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.61223894
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.6863638
        },
        {
            "double_negation_result": false,
            "highest_category": "Profanity",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.8115627
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.85333383
        },
        {
            "double_negation_result": false,
            "highest_category": "Profanity",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.88599813
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.8364697
        },
        {
            "double_negation_result": false,
            "highest_category": "Profanity",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.8778702
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.8988238
        },
        {
            "double_negation_result": false,
            "highest_category": "Profanity",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.8696708
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
            "highest_category": "Sexually Explicit",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.8988238
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.76523775
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.7761081
        },
        {
            "double_negation_result": false,
            "highest_category": "Profanity",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.8403191
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.6588125
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.85850734
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.82048255
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.8364697
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.78207105
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.6989911
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.8629672
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.88599813
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.8299589
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.7510937
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.68408644
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.7510937
        },
        {
            "double_negation_result": false,
            "highest_category": "Profanity",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.7998551
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
            "highest_category": "Sexually Explicit",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.82048255
        },
        {
            "double_negation_result": false,
            "highest_category": "Profanity",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.9248995
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.8460273
        },
        {
            "error": "cannot access local variable 'severe_toxic_score' where it is not associated with a value"
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.78855824
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.78207105
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.85333383
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.7998551
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.52811706
        },
        {
            "double_negation_result": false,
            "highest_category": "Profanity",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.65996873
        },
        {
            "error": "cannot access local variable 'severe_toxic_score' where it is not associated with a value"
        },
        {
            "double_negation_result": false,
            "highest_category": "Profanity",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.8696708
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.88599813
        },
        {
            "double_negation_result": false,
            "highest_category": "Profanity",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.7761081
        },
        {
            "error": "cannot access local variable 'severe_toxic_score' where it is not associated with a value"
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.82048255
        },
        {
            "error": "cannot access local variable 'severe_toxic_score' where it is not associated with a value"
        },
        {
            "double_negation_result": false,
            "highest_category": "Profanity",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.8403191
        },
        {
            "double_negation_result": true,
            "highest_category": "Sexually Explicit",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.8540474
        },
        {
            "error": "cannot access local variable 'severe_toxic_score' where it is not associated with a value"
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.83334327
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.8988238
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.8403191
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.7308154
        },
        {
            "error": "cannot access local variable 'severe_toxic_score' where it is not associated with a value"
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.7308154
        },
        {
            "double_negation_result": false,
            "highest_category": "Profanity",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.85173553
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
            "highest_category": "Sexually Explicit",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.85333383
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.85333383
        },
        {
            "error": "cannot access local variable 'severe_toxic_score' where it is not associated with a value"
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.8252207
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.743089
        },
        {
            "error": "cannot access local variable 'severe_toxic_score' where it is not associated with a value"
        },
        {
            "error": "cannot access local variable 'severe_toxic_score' where it is not associated with a value"
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.78711975
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": true,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.8115627
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.7510937
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.76197964
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.90451443
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.85333383
        },
        {
            "double_negation_result": false,
            "highest_category": "Sexually Explicit",
            "medical_term": false,
            "message": "Sentiment analysis stored successfully",
            "underline_decision": 0.8403191
        }
    ]
}
'''

# Load the JSON data
data = json.loads(json_data)

# Count occurrences of highest_category being "Sexually Explicit"
count_sexually_explicit = sum(1 for result in data['results'] if result.get('highest_category') == 'Sexually Explicit')

# Extract the underline_decision values
underline_decisions = [result.get('underline_decision', 0) for result in data['results']]

# Calculate the mean, maximum, and midpoint (median) of underline_decision values
mean_value = statistics.mean(underline_decisions)
max_value = max(underline_decisions)
midpoint_value = statistics.median(underline_decisions)

print(f'The count of "highest_category" being "Sexually Explicit" is: {count_sexually_explicit}')
print(f'The mean of "underline_decision" values is: {mean_value}')
print(f'The maximum "underline_decision" value is: {max_value}')
print(f'The midpoint (median) "underline_decision" value is: {midpoint_value}')
