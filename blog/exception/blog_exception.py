class UnSupportMethodException(BaseException):

    def __init__(self, arg):
        self.args = arg
        super(UnSupportMethodException, self).__init__(arg)
