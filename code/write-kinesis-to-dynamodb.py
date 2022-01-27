from decimal import Decimal
import base64
import json
import boto3


def put_transaction(cc_num,
                    trans_date_trans_time,
                    trans_num,
                    first,
                    last,
                    gender,
                    street,
                    city,
                    state,
                    zip,
                    lat,
                    long,
                    job,
                    dob,
                    merchant,
                    category,
                    merch_lat,
                    merch_long,
                    amt,
                    is_fraud
                    ):
    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('CreditCardTransactions')

    response = table.put_item(
        Item={
            'cc_num': str(cc_num),
            'trans_date_trans_time': trans_date_trans_time,
            'trans_num': trans_num,
            'customer': {
                'first': first,
                'last': last,
                'gender': gender,
                'street': street,
                'city': city,
                'state': state,
                'zip': zip,
                'lat': lat,
                'long': long,
                'job': job,
                'dob': dob
            },
            'merchant_info': {
                'merchant': merchant,
                'category': category,
                'merch_lat': merch_lat,
                'merch_long': merch_long
            },
            'amt': amt,
            'is_fraud': is_fraud
        }
    )
    return response
            

def lambda_handler(event, context):
    
    for record in event['Records']:
        # decode kinesis data
        decoded_record = base64.b64decode(record["kinesis"]["data"])
        # decode bytes into a str
        str_record = str(decoded_record, 'utf-8')
        # transform string into a dictionary
        deserialized_record = json.loads(str_record, parse_float=Decimal)

        trans_response = put_transaction(
            deserialized_record['cc_num'],
            deserialized_record['trans_date_trans_time'],
            deserialized_record['trans_num'],
            deserialized_record['first'],
            deserialized_record['last'],
            deserialized_record['gender'],
            deserialized_record['street'],
            deserialized_record['city'],
            deserialized_record['state'],
            deserialized_record['zip'],
            deserialized_record['lat'],
            deserialized_record['long'],
            deserialized_record['job'],
            deserialized_record['dob'],
            deserialized_record['merchant'],
            deserialized_record['category'],
            deserialized_record['merch_lat'],
            deserialized_record['merch_long'],
            deserialized_record['amt'],
            deserialized_record['is_fraud']
        )
        print(trans_response)
