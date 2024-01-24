import requests
import pandas as pd
import numpy as np
import json
import random
import time

# get the total number of available questions:
def request_total_question():
    url_total_questions = "https://opentdb.com/api_count_global.php"
    response_total_questions = requests.get(url_total_questions)
    result_total_questions = response_total_questions.json()
    for key_total, value_total in enumerate(result_total_questions['overall'].items()):
        if value_total[0] == 'total_num_of_verified_questions':
            total_number_of_questions = value_total[1]
    return total_number_of_questions

# request a token:
def request_token():
    response_token = requests.get("https://opentdb.com/api_token.php?command=request")
    result_token = response_token.json()
    token = result_token['token']
    return token, result_token

# fetch the first 50 questions:
def load_data(token):
    url_with_token = 'https://opentdb.com/api.php?amount=50&token='+ token
    response_url= requests.get(url_with_token)
    result = response_url.json()
    json_object = json.dumps(result, indent=4)
    json_object = json_object.replace("&#039;", "'")
    json_object = json_object.replace("&lt;", '<')
    json_object = json_object.replace("&gt;", ">")
    json_object = json_object.replace("&quot;", "'")
    json_object = json_object.replace("&amp;", "&")
    # json_object = unescape(json_object)
    result = eval(json_object)
    list_values = []
    list_columns = []
    # enumerate through data to fetch key and values:
    for key, value in enumerate(result['results']):
        list_columns.append(key)
        list_values.append(value)
        # create a dataframe with the values:
    df = pd.DataFrame(data = list_values)
    return df

#  fetch another new 50 questions and add them to the existing one dataframe:
def load_new_data(df, token):
    url_with_token = 'https://opentdb.com/api.php?amount=50&token='+ token
    response_url= requests.get(url_with_token)
    result = response_url.json()
    json_object = json.dumps(result, indent=4)
    json_object = json_object.replace("&#039;", "'")
    json_object = json_object.replace("&lt;", '<')
    json_object = json_object.replace("&gt;", ">")
    json_object = json_object.replace("&quot;", "'")
    json_object = json_object.replace("&amp;", "&")
    # json_object = unescape(json_object)
    result = eval(json_object)
    list_values = []
    list_columns = []
    # enumerate through data to fetch key and values:
    for key, value in enumerate(result['results']):
        list_columns.append(key)
        list_values.append(value)
        # create a dataframe with the values:
    df_new = pd.DataFrame(data = list_values)
    frames = [df, df_new]
    df = pd.concat(frames)
    df.to_csv('questions.csv', index=False)
    return df

# fetch one question, this function is only for the last remaining questions:
def load_data_single_amount(df, token):
    url_with_token = 'https://opentdb.com/api.php?amount=1&token='+ token
    response_url= requests.get(url_with_token)
    result = response_url.json()
    json_object = json.dumps(result, indent=4)
    json_object = json_object.replace("&#039;", "'")
    json_object = json_object.replace("&lt;", '<')
    json_object = json_object.replace("&gt;", ">")
    json_object = json_object.replace("&quot;", "'")
    json_object = json_object.replace("&amp;", "&")
    # json_object = unescape(json_object)
    result = eval(json_object)
    list_values = []
    list_columns = []
    # enumerate through data to fetch key and values:
    for key, value in enumerate(result['results']):
        list_columns.append(key)
        list_values.append(value)
        # create a dataframe with the values:
    df_per_single = pd.DataFrame(data = list_values)
    frames = [df, df_per_single]
    df = pd.concat(frames)
    return df

# make some data transformations and save the final dataframe to a csv file called questionsList.csv:
def transform_data(df):
    # create new column option1 from column correct answers:
    df['option1'] = df['correct_answer'].copy()
    # create three new option columns from incorrects answers:
    df[['option2', 'option3', 'option4']] = df["incorrect_answers"].apply(pd.Series)
    # make a new dataframe with these four option coloumns:
    df_opts = df[['option1', 'option2', 'option3', 'option4']].copy()
    # drop some columns:
    df = df.drop(['incorrect_answers', 'option1', 'option2', 'option3', 'option4'], axis=1)
    # shufftering the values for four option columns:
    df_opts = df_opts.apply(np.random.permutation, axis=1,result_type='expand').set_axis(df_opts.columns,axis=1)
    df = pd.concat([df, df_opts], axis=1)
    df.to_csv('questionsList.csv', index=False)
    
def main():
    total_number_of_questions = request_total_question()
    token, result_token = request_token()
    df = load_data(token)

    count_calls = divmod(total_number_of_questions, 50)
    for i in range(0, count_calls[0] - 1):
        print(len(df),"/",total_number_of_questions)
        time.sleep(5)
        df = load_new_data(df, token)

    for i in range(len(df), total_number_of_questions):
        print(len(df),"/",total_number_of_questions)
        time.sleep(5)
        df = load_data_single_amount(df, token)

    if len(df) == total_number_of_questions:
        transform_data(df)

if __name__ == '__main__':
    main()
