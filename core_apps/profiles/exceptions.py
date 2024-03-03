# File to write our own error handlers for situable situations
from rest_framework.exceptions import APIException


# our custom exception handlerr to make folowwing yourself avaliable
class CantFollowYourself(APIException):
    status_code = 403
    default_detail = "You can't follow yourself."
    default_code = "forbidden"
