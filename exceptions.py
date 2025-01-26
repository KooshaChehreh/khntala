from rest_framework.exceptions import APIException



class AccountSuspended(APIException):
    status_code = 400
    default_code = "account_suspended"
    default_detail = {
        "code": default_code,
        "message": "حساب کاربری تعلیق شده است و امکان ورود وجود ندارد.",
    }

class InvalidUsernameOrPassword(APIException):
    status_code = 400
    default_code = "invalid_username_or_password"
    default_detail = {
        "code": default_code,
        "message": "کلمه عبور یا کاربری وارد شده اشتباه است.",
    }

class UsernameAlreadyExists(APIException):
    status_code = 400
    default_code = "invalid_username_or_password"
    default_detail = {
        "code": default_code,
        "message": "کلمه عبور یا کاربری وارد شده اشتباه است.",
    }