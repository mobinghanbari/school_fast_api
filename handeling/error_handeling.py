from fastapi import status




class JinjaExeption(Exception):
    def __init__(self, status_code: int, detail: dict):
        self.status_code = status_code
        self.detail = detail

    @staticmethod
    def success(detail: str = "Success"):
        raise JinjaExeption(status_code=status.HTTP_200_OK, detail={"error":detail})

    @staticmethod
    def bad_request(detail: str = "Bad Request"):
        raise JinjaExeption(status_code=status.HTTP_400_BAD_REQUEST, detail={"error":detail})

    @staticmethod
    def unauthorized(detail: str = "Unauthorized"):
        raise JinjaExeption(status_code=status.HTTP_401_UNAUTHORIZED, detail={"error":detail})

    @staticmethod
    def not_found(detail: str = "Not Found"):
        raise JinjaExeption(status_code=status.HTTP_404_NOT_FOUND, detail={'error': detail})

    @staticmethod
    def internal_server_error(detail: str = "a Problem has occurred"):
        raise JinjaExeption(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail={"error":detail})

