from flask import request


class login_controller:

    @staticmethod
    def validate_login(request):
        username = request.form.get('username')
        password = request.form.get('password')
        if(username == "admin" and password == "123"):
            return True
        else:
            return False