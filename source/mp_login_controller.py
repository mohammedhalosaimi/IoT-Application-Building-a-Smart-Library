# from flask import request

# USERNAME = "jaqen"
# PASSWORD = "hgar"

class login_controller:

    @staticmethod
    def validate_login(request):
        """
            This method validates login information
            Parameters: The request object
            Returns: True: Details were correct, False: Details were incorrect.
        """
        # sent_username = request.form.get('username')
        # sent_password = request.form.get('password')
        # if(sent_username == USERNAME and sent_password == PASSWORD):
        #     return True
        # else:
        #     return False