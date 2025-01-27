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
    default_code = "username_already_exists"
    default_detail = {
        "code": default_code,
        "message": "این نام کاربری تکراریست.",
    }

class TransactionDone(APIException):
    status_code = 400
    default_code = "tranction_done_before"
    default_detail = {
        "code": default_code,
        "message": "تراکنش انجام شده است.",
    }

class SuspendedUser(APIException):
    status_code = 400
    default_code = "user_is_suspended"
    default_detail = {
        "code": default_code,
        "message": "کاربر بن شده است.",
    }

class UserDoesNotExist(APIException):
    status_code = 400
    default_code = "user_does_not_exist"
    default_detail = {
        "code": default_code,
        "message": "کاربر وجود ندارد.",
    }

class UnsufficientBalance(APIException):
    status_code = 400
    default_code = "gold_balance_is_not_sufficient"
    default_detail = {
        "code": default_code,
        "message": "مقدار طلای درخواستی بیشتر از موجودی کاربر است.",
    }