import os
import errno
from config import APP_ROOT

class LastErrorHolder:
    """
    Support holding of last error
    """
    def __init__(self):
        self.errorText  = ""
        self.__hasError = False

    def clearError(self):
        """
        Clears last error
        :return: None
        """
        self.errorText  = ""
        self.__hasError = False

    def setError(self, errorText):
        """
        Sets new error
        :param errorText: new error text
        :return: False
        """
        self.errorText   = errorText
        self.__hasError  = True

        return False

    @property
    def hasError(self):
        """
        Holds error flag.
        :return: True when have error, otherwise False
        """
        return self.__hasError
