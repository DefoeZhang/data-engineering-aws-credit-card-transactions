from __future__ import print_function

import base64
import json
import boto3
from datetime import datetime

s3_client = boto3.client('s3')

# Converting datetime object to string
dateTimeObj = datetime.now()

#format the string
timestampStr = dateTimeObj.strftime("%Y-%m-%d %H:%M:%S")

# this is the list for the records
kinesisRecords = []

def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))
    for record in event['Records']:
        # Kinesis data is base64 encoded so decode here
        payload = base64.b64decode(record['kinesis']['data'])
        payload_str = payload.decode("utf-8")
        # append each record to a list
        kinesisRecords.append(payload_str)
        # this is just for logging
        print("Decoded payload: " + payload_str)

    # make a string out of the list. Backslash n for new line in the s3 file
    ex_string = '\n'.join(kinesisRecords)

    # generate the name for the file with the timestamp
    mykey = 'output-' + timestampStr + '.txt'

    #put the file into the s3 bucket
    response = s3_client.put_object(Body=ex_string, Bucket='my-aws-bulkimport', Key= mykey)

    return 'Successfully processed {} records.'.format(len(event['Records']))
