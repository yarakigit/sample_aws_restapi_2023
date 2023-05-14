#!/bin/zsh
settings=$(cat settings.json)


image_file=$(echo $settings | jq -r '.image_path')
api_endpoint=$(echo $settings | jq -r '.endpoint')

image_data=$(base64 < "$image_file")

# リクエストの作成
request_body=$(cat << EOF
{
    "name": "Sample",
    "image": "$image_data"
}
EOF
)

# API Gatewayへのリクエスト
response=$(curl -X POST \
    -H "Content-Type: application/json" \
    -d "$request_body" \
    "$api_endpoint")

echo $response
