from src.bearer.signIn import sigh_in
class Headers(object):

    @classmethod
    def get_matrix_by_id_headers(cls):
        return {
            'accept' : 'text/plain',
            'Authorization' : f'Bearer {sigh_in()}'
        }

