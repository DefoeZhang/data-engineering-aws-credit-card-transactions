import json
import boto3
from datetime import datetime
from boto3.dynamodb.conditions import Key


def lambda_handler(event, context):

    print("MyEvent:")
    print(event)

#    mycontext = event.get("context")
#    method = mycontext.get("http-method")
    method = event['context']['http-method']

    if method == "GET":
        # TODO: write code...
        #client = boto3.resource('dynamodb')
        #table = client.Table('CreditCardTransactions')
        dynamo_client = boto3.client('dynamodb')
        
        #response = table.get_item(
        #    Key = {
        #        'cc_num': '3573030000000000.0',
        #        'trans_date_trans_time': '6/21/20 12:16'
        #    })                                                              
        #print(response['Item'])
        
        cc_num = event['params']['querystring']['cc_num']
        trans_date_trans_time = event['params']['querystring']['trans_date_trans_time']
        print(cc_num)
        print(trans_date_trans_time)
        response = dynamo_client.get_item(TableName = 'CreditCardTransactions', Key = {'cc_num':{'S': cc_num}, 'trans_date_trans_time':{'S': trans_date_trans_time}})
        #response = dynamo_client.get_item(TableName = 'CreditCardTransactions', Key = {'cc_num': cc_num, 'trans_date_trans_time': trans_date_trans_time})
        print(response['Item'])

        #myreturn = "This is the return of the get"

        return {
            'statusCode': 200,
            'body': json.dumps(response['Item'])
           }

    elif method == "POST":

#       mystring = event['params']['querystring']['param1']
        p_record = event['body-json']
        p_record['trans_date_trans_time'] = datetime.strptime(p_record['trans_date_trans_time'], '%m/%d/%y %H:%M').strftime('%Y-%m-%d %H:%M:%S')
        recordstring = json.dumps(p_record)
        print("POST")
        print('recordstring:', recordstring)
        
        client = boto3.client('kinesis')
        response = client.put_record(
            StreamName='APIData',
            Data= recordstring,
            PartitionKey='string'
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps(p_record)
        }
    else:
        return {
            'statusCode': 501,
            'body': json.dumps("Server Error")
        }
