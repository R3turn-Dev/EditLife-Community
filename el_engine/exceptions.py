from time import time


# Database Management
class DBEngineNotFound(Exception):
    def __init__(self, message, errors):
        super().__init__(message)

        self.errors = errors
        self.raise_time = time()
