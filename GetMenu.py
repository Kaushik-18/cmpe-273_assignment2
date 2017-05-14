import boto3
import json


def lambda_handler(event, context):
    menu_id = event['menu-id']
    table = boto3.resource('dynamodb').Table('Menus')
    response = table.get_item(Key={"menu_id": menu_id})

    if 'Item' in response:
        return response['Item']
    else:
        return 'Menu not found !'
