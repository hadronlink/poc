def lambda_handler(event, context):
    my_list = [1, 2, 3, 4, 5, 6, 7]
    print(my_list)
    return {
        'statusCode': 200
    }