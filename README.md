# AWS REST API Sample
---
## 手順
### `DynamoDB`でテーブルの作成
- マネージド NoSQL データベース
1. `DynamoDB` :arrow_right: `テーブル` :arrow_right: `テーブルの作成`
    - テーブル名, キーを入力
- 無料枠 : 25GB
## IAM
- AWS リソースへのアクセス管理
- `ロール` :arrow_right: `ロールを作成` (短期的な権限を付与)
    - `ユースケース`を`Lambda`にする
        - `AWSLambdaBasicExecutionRole` : Provides write permissions to CloudWatch Logs.
        - `AmazonDynamoDBFullAccess`
    - `次へ` :arrow_right: `ロールを作成`

## AWS Lambda
- `関数の作成`
    - `関数名` を入力
    - `ランタイム` : Python3.9
    - `アーキテクチャ` : x86_64
    - `アクセス権限` : `既存のロールを使用する` : 上記で作成したものを使用する
    - `関数の作成`をクリック
    - `Deploy`

## API Gateway
- `REST API`
    - `REST`, `新しいAPI`, `エンドポイント`は`リージョン`
- リソース
    - `アクション` :arrow_right: `リソースの作成` :arrow_right: リソース名を入力
- メソッド
    - `アクション` :arrow_right: `メソッドの作成` :arrow_right: `POST` を選択
    - Lambda関数名を入力
    - `LAMBDA`の`統合リクエスト` :arrow_right: `マッチングテンプレートの追加` :arrow_right: `application/json`
    - `アクション` :arrow_right: `APIのデプロイ`
        - ステージを作成もしくは選択


## APIキーの設定
- `API Gateway` :arrow_right: `リソース` :arrow_right: メソッドを選択 :arrow_right: `メソッドリクエスト`を選択 :arrow_right: `APIキーの必要性`を`true`に設定
    - [AWS API Gateway コンソールを使用して API キーをセットアップする](https://docs.aws.amazon.com/ja_jp/apigateway/latest/developerguide/api-gateway-setup-api-key-with-console.html) 

- APIキーの作成
    - `API Gateway` :arrow_right: `アクション` :arrow_right: `APIキーの作成`

## 使用量プランの作成
- `API Gateway` :arrow_right: `使用量プラン` :arrow_right: `作成`
- `API`と`ステージ`を選択
- 既存のキーを使用する場合, `API キーを使用量プランに追加`
    - [AWS API Gateway REST API を使用して API キーをセットアップする](https://docs.aws.amazon.com/ja_jp/apigateway/latest/developerguide/api-gateway-setup-api-key-with-restapi.html)