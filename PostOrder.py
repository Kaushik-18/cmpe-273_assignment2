import boto3
import json


def lambda_handler(event, context):
    menu_table = boto3.resource('dynamodb').Table('Menus')
    order_table = boto3.resource('dynamodb').Table('Orders')

    menu_id = event['menu_id']
    customer_name = event['customer_name']
    customer_email = event['customer_email']
    order_id = event['order_id']
    selections = []
    m_response = menu_table.get_item(Key={"menu_id": menu_id})
    if 'Item' in m_response:
        menu_data = m_response['Item']
        selections = menu_data['selection']
        sel = ''
        for number, letter in enumerate(selections):
            sel += str(number + 1) + "." + letter + " "

        order_table.put_item(Item={'customer_name': customer_name,
                                   'customer_email': customer_email,
                                   'menu_id': menu_id,
                                   'order_id': order_id,
                                   'order_status': "1"})

        return {"Message": "Hi " + customer_name + ",please choose one of these selections : " + sel}
