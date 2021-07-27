class Auth(object):

    def __init__(self):
        self.tokenCast = 'a2ed059a48019f91b11b9867'
        self.logs = []

    def validarToken(self, token):
        if self.tokenCast != token:
            return False
        return True