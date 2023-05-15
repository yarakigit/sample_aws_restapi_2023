# DymamoDB
-  テーブル名
    - memo-user-save-test
- パーティションキー
    - memo-user-save-test-id
- その他キー
    - memotitle
    - memobody
    - timestamp
# IAM
- ロール名
    - memo-user-save-test

# Lambda
- memo-user-save-test-post
- memo-user-save-test-get
- memo-user-save-test-delete
- memo-user-save-test-put

# API Gateway
- API名
    - memo-user-save-test-api
- リソース名
    - test-resource
- ステージ名
    - test-stage


# Response JSON
- memoID
- memoTitle
- memoBody
- timestamp

# settings.json
~~~json
{
    "endpoint": "https://hogepiyo.com/test-stage/test-resource",
    "memotitle": "this is NEW memo title",
    "memobody": "this is NEW memo body",
    "memoid":"hogepiyo"
}  
~~~