#from _future_ import print_function

import boto3
#import time
import json

print('Loading function')
ssmClient = boto3.client('ssm')

def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))
    message = event['Records'][0]['Sns']['Message']
    print("From SNS: " + message)
    #return message
    if message == "start":
        print("SNS message is: " + message)
        ssmCommand = ssmClient.send_command(
            Targets =[
                {
                    "Key": "tag:Name",
                    "Values":[
                        "SanjanaSSMNginxInstance",
                        ]
                },
            ],
        DocumentName = 'AWS-RunShellScript',
        #TimeoutSeconds = 240,
        Comment = 'nginx service start',
        Parameters = {
            "commands":  ["sudo iptables -I INPUT -p tcp --dport 80 -j ACCEPT"] 
        }
    )
    #print(ssmCommand)
    if message == "stop":
        print("SNS message is: " + message)
        ssmCommand = ssmClient.send_command(
            Targets =[
                {
                    "Key": "tag:Name",
                    "Values":[
                        "SanjanaSSMNginxInstance",
                        ]
                },
            ],

        DocumentName = 'AWS-RunShellScript',
       # TimeoutSeconds = 240,
        Comment = 'nginx service stop',
        Parameters = {
            "commands": ["sudo iptables -I INPUT -p tcp --dport 80 -j DROP"] 
        }
    )
    #print(ssmCommand)
