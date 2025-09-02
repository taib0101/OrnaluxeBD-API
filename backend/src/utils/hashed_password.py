from bcrypt import hashpw, gensalt, checkpw

class Hash:

    @staticmethod
    def create_pass(password: str):
        return hashpw(password.encode(), gensalt()).decode()
    
    @staticmethod
    def check_pass(user_password: str, db_password: str):
        return checkpw(user_password.encode(), db_password.encode())