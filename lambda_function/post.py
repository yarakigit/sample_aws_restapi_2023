import json
import boto3
from datetime import datetime
import random
import string

def lambda_handler(event, context):
    # DynamoDBテーブルの設定
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('memo-user-save-test')

    # API Gatewayからのリクエストパラメーターの取得
    request_body = event['body']
    request_body = json.loads(request_body)

    memoTitle = request_body['memoTitle']
    memoBody = request_body['memoBody']

    # 日付の取得
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # 乱数
    random.seed(timestamp)
    random_str=''.join(random.choice(string.ascii_letters + string.digits) for _ in range(64))
    
    # DBへ保存
    memoID = str(datetime.now().timestamp()) + random_str  # IDを生成
    table.put_item(
        Item={
            'memo-user-save-test-id': memoID,
            'memotitle': memoTitle,
            'memobody': memoBody,
            'timestamp' : timestamp
        }
    )

    # レスポンスの作成
    response = {
        'statusCode': 200,
        'body': 'Memo saved successfully',
        'memoID': memoID
    }

    return response