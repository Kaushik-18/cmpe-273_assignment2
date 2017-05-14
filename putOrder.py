import boto3
import json
import datetime


def lambda_handler(event, context):
    menu_table = boto3.resource('dynamodb').Table('Menus')
    order_table = boto3.resource('dynamodb').Table('Orders')

    order_id = event['order_id']

    order_response = order_table.get_item(Key={"order_id": order_id})

    if 'Item' in order_response:
        item = order_response['Item']
        menu_response = menu_table.get_item(Key={"menu_id": item['menu_id']})
        menu_items = menu_response['Item']
        status = item['order_status']
        message = ''
        data = {}
        if 'orders' in item:
            data = item['orders']

        if 'input' in event:
            sel = event['input']
            if status == "1":
                sellist = menu_items['selection']
                data["size"] = sellist[int(sel) - 1]

                size_data = ''
                sizelist = menu_items['size']
                for number, letter in enumerate(sizelist):
                    size_data += str(number + 1) + "." + letter + " "
                message += "which size do you want ? " + size_data

            else:
                data['size'] = menu_items['size'][int(sel) - 1]
                if 'size' in data:
                    priceindex = menu_items['size'].index(data['size'])
                    data['price'] = menu_items['price'][priceindex]
                    data['order_time'] = '{:%m-%d-%Y %H:%M:%S}'.format(datetime.datetime.now())
                    message = "Your order costs " + data[
                        'price'] + " We will email you when your order is ready.Thank you !"
                else:
                    message = 'Size not selected !'

        order_table.update_item(Key={'order_id': order_id}, UpdateExpression='SET order_status =  :val1',
                                ExpressionAttributeValues={':val1': "2"})

        order_table.update_item(Key={'order_id': order_id},
                                UpdateExpression='SET orders = :val1',
                                ExpressionAttributeValues={':val1': data})

        return {"Message": message}
