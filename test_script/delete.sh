#!/bin/zsh
settings=$(cat settings.json)

api_endpoint=$(echo $settings | jq -r '.endpoint')
api_key=$(echo $settings | jq -r '.apikey')
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
    -H "x-api-key: $api_key" \
    "$api_endpoint?memoID=$memo_id")

echo $response
