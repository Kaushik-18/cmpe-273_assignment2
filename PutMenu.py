import boto3
import json


def lambda_handler(event, context):
    id = event['menu_id']
    data = event['selection']
    table = boto3.resource('dynamodb').Table('Menus')
    table.update_item(Key={'menu_id': id},
                      UpdateExpression='SET selection = :val1',
                      ExpressionAttributeValues={':val1': data})

    return "200 OK"
