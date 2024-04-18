from rest_framework.exceptions import APIException


# simple own exception handler for already voted articles from user
class YouHaveAlreadyRated(APIException):
    status_code = 400
    default_detail = "You have already rated this article."
    default_code = "bad_request"
