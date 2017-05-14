import boto3
import json


def lambda_handler(event, context):
    table = boto3.resource('dynamodb').Table('Menus')
    menu_id = event['menu_id']
    price = event['price']
    store_name = event['store_name']
    store_hours = event['store_hours']
    size = event['size']
    selection = event['selection']

    table.put_item(Item={
        'menu_id': menu_id,
        'price': price,
        'store_name': store_name,
        'selection': selection,
        'store_hours': store_hours,
        'size': size
    })
    return "200 OK"
