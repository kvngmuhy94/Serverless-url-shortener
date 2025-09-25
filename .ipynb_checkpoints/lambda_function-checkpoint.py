import boto3
import os
import json
import random
import string


dynamodb = boto3.resource('dynamodb')
table_name = os.environ.get('TABLE_NAME', 'urlShortenerTable')
Table = dynamodb.Table(table_name)

def generate_short_code(length=6):
    """Generate a random 6-character code for the shortened url."""
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
        original_url = body.get('url')

        if not original_url:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'URL is required'})
            }

        short_code = generate_short_code()

        Table.put_item(Item={
            'shortCode': short_code,
            'originalUrl': original_url
        })

        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Short URL created successfully',
                'shortUrl': f"https://{os.environ.get('DOMAIN_NAME')}/{short_code}"
            })
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})

        }
        
    

