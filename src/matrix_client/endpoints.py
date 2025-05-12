import os
from dotenv import load_dotenv
load_dotenv()

class Endpoints:

    @staticmethod
    def get_matrix_by_id(matrix_id: str):
        return f'{os.getenv('HOSTADMIN')}/MatrixDetail/Get/all?Matrixes={matrix_id}&PageNumber=1&PageSize=10'
