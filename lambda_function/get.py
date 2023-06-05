import json
import boto3

def lambda_handler(event, context):
    # DynamoDBテーブルの設定
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('memo-user-save-test')

    # API Gatewayからのリクエストパラメーターの取得
    # 固有のキーの取得
    memoID = event['memoID']
    
    # テーブルから情報を取得
    response = table.get_item(
        Key={
            'memo-user-save-test-id': memoID
        }
    )

    # レスポンスの作成
    if 'Item' in response:
        # debug
        #key_list = response['Item'].keys()
        #print("キーの一覧:", key_list)
        #
        item=response['Item']
        memoTitle = item['memotitle']
        memoBody = item['memobody']
        timestamp = item['timestamp']
        response_body = {
            'statusCode': 200,
            'body': {
                'memoTitle': memoTitle,
                'memoBody': memoBody,
                'timestamp': timestamp
            }
        }
    else:
        response_body = {
            'statusCode': 404,
            'body': 'Memo not found'
        }

    return response_body
