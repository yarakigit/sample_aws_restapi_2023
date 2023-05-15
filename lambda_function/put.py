import json
import boto3
from datetime import datetime

def lambda_handler(event, context):
    # DynamoDBテーブルの設定
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('memo-user-save-test')

    # API Gatewayからのリクエストパラメーターの取得
    request_body = event['body']
    request_body = json.loads(request_body)

    # 固有のキーの取得
    memoID = request_body['memoID']
    
    memoTitle = request_body['memoTitle']
    memoBody = request_body['memoBody']
    
    # 日付の取得
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        table.update_item(
            Key={
                'memo-user-save-test-id': memoID
            },
            UpdateExpression="SET #memotitleAttr = :memotitleVal, #memobodyAttr = :memobodyVal, #timestampAttr = :timestampVal",
            ExpressionAttributeNames= {
            '#memotitleAttr' : 'memotitle',
            '#memobodyAttr' : 'memobody',
            '#timestampAttr' : 'timestamp'
            },
            ExpressionAttributeValues={
                ':memotitleVal': memoTitle,
                ':memobodyVal': memoBody,
                ':timestampVal': timestamp 
            }
        )
        response_body = {
            'statusCode': 200,
            'body': 'Memo Update successfully'
        }
    except Exception as e:
        response_body = {
            'statusCode': 404,
            'body': 'Memo not found'
        }    

    return response_body
