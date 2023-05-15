#!/bin/zsh
settings=$(cat settings.json)

api_endpoint=$(echo $settings | jq -r '.endpoint')
memo_id=$(echo $settings | jq -r '.memoid')

# リクエストの作成
request_body=$(cat << EOF
{
    "memoID": "$memo_id"
}
EOF
)


# API Gatewayへのリクエスト
response=$(curl -X DELETE \
    -H "Content-Type: application/json" \
    -d "$request_body" \
    "$api_endpoint")

echo $response
