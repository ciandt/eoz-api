"""
Responsible to get creating people details.
"""
import requests


class PeopleClient:

    def __init__(self, base_url: str, token: str):
        """ Class Constructor """
        self.base_url = base_url if base_url.endswith("/") else f"{base_url}/"
        self.token = token
        self.header = {"x-api-key": self.token}

    def get_login_data(self, login: str) -> dict:
        """Get data related to a user
        Returns
        -------
        dict
            {'login': 'login1',
             'name': 'NAME LOGIN 1',
             'email': 'email@email.com',
             'admission': 123,
             'admissionReal': 123,
             'role': {'code': 28, 'name': 'Developer'},
             'area': {'code': 101, 'name': 'Tower', 'begin': None},
             'project': {'code': 8872, 'name': 'Project'},
             'cityBase': {'code': 6, 'name': 'City name',
                         'acronym': 'BH'},
             'company': {'code': 1, 'name': 'Company name'},
             'coach': 'Coach name',
             'pdm': 'Pdm Name',
             'bp': 'Bp name'}

        """
        url = f"{self.base_url}prd/api/v2/people/{login}"
        response = requests.get(url, headers=self.header)

        if response.status_code == 200:
            return response.json()
