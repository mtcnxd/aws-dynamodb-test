from datetime import datetime
import boto3

class ClientService:
    def __init__(self):
        dynamodb = boto3.resource(
            'dynamodb',
            aws_access_key_id="",
            aws_secret_access_key="",
            region_name='us-east-1'
        )

        self.table = dynamodb.Table('mecanica_rubio')
    
    def create_row(self, pk, sk, entity, client_data):
        return self.table.put_item(
            Item={
                'pk': pk,
                'sk': sk,
                'entity': entity,
                'data': client_data,
                'created_at': datetime.now().isoformat()
            }
        )
    
    def get_row(self, pk, sk):
        return self.table.get_item(
            Key={
                'pk': pk,
                'sk': sk
            }
        )