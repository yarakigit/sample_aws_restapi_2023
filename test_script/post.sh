#!/bin/zsh
settings=$(cat settings.json)

api_endpoint=$(echo $settings | jq -r '.endpoint')
api_key=$(echo $settings | jq -r '.apikey')
memo_title=$(echo $settings | jq -r '.memotitle')
memo_body=$(echo $settings | jq -r '.memobody')

# リクエストの作成
request_body=$(cat << EOF
{
    "memoTitle": "$memo_title",
    "memoBody": "$memo_body"
}
EOF
)

# API Gatewayへのリクエスト
response=$(curl -X POST \
    -H "Content-Type: application/json" \
    -H "x-api-key: $api_key" \
    -d "$request_body" \
    "$api_endpoint")

echo $response