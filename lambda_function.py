import json
import pandas as pd

def lambda_handler(event, context):
    my_list = [1, 2, 3, 4, 5, 6]
    print(my_list)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }