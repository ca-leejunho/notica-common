from .singleton import Singleton
import notica_common.aws_connector

class Const(Singleton):
    class ConstError(TypeError):
        pass

    def __init__(self):
        aws_connector = notica_common.aws_connector.AwsConnector.get_instance()
        if not aws_connector.is_connected():
            pass

        SECRET_PARAMS = aws_connector.secret
        self.DYNAMODB_TABLE = SECRET_PARAMS.get('dynamodb_table', 'notica-stg')
        self.MIERUKA_HOST = SECRET_PARAMS.get('mieruka_host', '')
        self.MIERUKA_USER = SECRET_PARAMS.get('mieruka_user', '')
        self.MIERUKA_PASSWORD = SECRET_PARAMS.get('mieruka_password', '')
        self.MIERUKA_DB = SECRET_PARAMS.get('mieruka_db', '')
        self.WORKPLACEUSER_TABLE = SECRET_PARAMS.get('workplaceuser_table', '')
        self.WORKPLACE_ACCESS_TOKEN = SECRET_PARAMS.get('workplace_access_token', '')


    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise self.ConstError("Can't rebind const (%s)" % name)
        self.__dict__[name] = value