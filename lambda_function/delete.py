import json
import boto3

def lambda_handler(event, context):
    # DynamoDBテーブルの設定
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('memo-user-save-test')

    # API Gatewayからのリクエストパラメーターの取得
    request_body = event['body']
    request_body = json.loads(request_body)

    # 固有のキーの取得
    memoID = request_body['memoID']

    # テーブルから情報を取得
    try:
        response = table.delete_item(
            Key={
                'memo-user-save-test-id': memoID
            }
        )
        # レスポンスの作成
        response_body = {
            'statusCode': 200,
            'body': 'Memo deleted successfully'
        }
    except Exception as e:
        response_body = {
            'statusCode': 404,
            'body': 'Memo not found'
        }
    return response_body
