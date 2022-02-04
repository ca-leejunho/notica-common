import os
import json
from datetime import datetime, timezone

import boto3
from botocore.exceptions import ClientError
import notica_common.const
from .singleton import Singleton

class AwsConnector(Singleton):
    def __init__(self):
        self.session = boto3.session.Session()
        self.__secret = self.__get_secret()

    def is_connected(self):
        return True if self.session and self.__secret else False

    @property
    def secret(self):
        return self.__secret

    def __get_secret(self):
        client = self.session.client(
            service_name='secretsmanager',
            region_name='ap-northeast-1'
        )

        secret_id = os.getenv('SECRET_NAME', 'notica-stg')

        try:
            get_secret_value_response = client.get_secret_value(SecretId=secret_id)
        except ClientError as e:
            return json.loads('{}')
        except Exception as e:
            return json.loads('{}')
        else:
            secret = get_secret_value_response['SecretString']
            return json.loads(secret)

    def is_cancelled(self, req_id):
        const = notica_common.const.Const.get_instance()
        dynamodb = self.session.resource('dynamodb').Table(const.DYNAMODB_TABLE)
        item = dynamodb.get_item(Key={'Id': req_id})['Item']
        return item['Status'] == 'CANCELLED'

    def dynamodb_update_item(self, key, update_expression, expression_attribute_names, expression_attribute_values):
        const = notica_common.const.Const.get_instance()
        self.session.resource('dynamodb').Table(const.DYNAMODB_TABLE).update_item(
            Key={'Id': key},
            UpdateExpression='SET #updatedAt = :now',
            ExpressionAttributeNames={'#updatedAt': 'UpdatedAt'},
            ExpressionAttributeValues={':now': int(datetime.now(timezone.utc).timestamp())}
        )
        self.session.resource('dynamodb').Table(const.DYNAMODB_TABLE).update_item(
            Key={'Id': key},
            UpdateExpression=update_expression,
            ExpressionAttributeNames=expression_attribute_names,
            ExpressionAttributeValues=expression_attribute_values
        )