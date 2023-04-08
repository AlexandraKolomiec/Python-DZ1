
class BaseException(Exception):
    pass

class LevelException(BaseException):
    print('Level')

class AccesException(BaseException):
    print('Access')