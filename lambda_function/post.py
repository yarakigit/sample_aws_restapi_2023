import json
import boto3
import base64
from datetime import datetime

def lambda_handler(event, context):
    # DynamoDBテーブルの設定
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('image-user-save-test')

    # API Gatewayからのリクエストパラメーターの取得
    request_body = event['body']
    request_body = json.loads(request_body)

    # 名前と画像の取得
    name = request_body['name']
    image_data = request_body['image']

    # 画像のデコード
    image_binary = base64.b64decode(image_data)

    # 日付の取得
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # 画像の保存
    image_id = str(datetime.now().timestamp())  # 一意の画像IDを生成
    table.put_item(
        Item={
            'user-custom-img-id': image_id,
            'name': name,
            'image': image_binary,
            'timestamp' : timestamp
        }
    )

    # レスポンスの作成
    response = {
        'statusCode': 200,
        'body': 'Image saved successfully',
        'imageId': image_id
    }

    return response
