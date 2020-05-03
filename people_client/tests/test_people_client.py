""" Unit tests for the people client api module """
import pytest

from people_client import PeopleClient


@pytest.fixture
def mock_data():
    return {'login': 'login1',
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


def test_get_login_data(requests_mock, mock_data):
    """Test for get login data"""
    url = "http://test.com/"
    login = "test_login"
    pp = PeopleClient(url, "AZDFDARETTK")
    requests_mock.get(f"{url}prd/api/v2/people/{login}",
                      json=mock_data)
    assert pp.get_login_data("test_login") == mock_data


def test_get_login_data_with_not_url_slash(requests_mock, mock_data):
    """Test for get login data"""
    url = "http://test.com"
    login = "test_login"
    pp = PeopleClient(url, "AZDFDARETTK")
    requests_mock.get(f"{url}/prd/api/v2/people/{login}",
                      json=mock_data)
    assert pp.get_login_data("test_login") == mock_data


def test_get_login_error(requests_mock, mock_data):
    """Test for get login data error"""
    url = "http://test.com/"
    login = "test_login"
    pp = PeopleClient(url, "AZDFDARETTK")
    requests_mock.get(f"{url}prd/api/v2/people/{login}",
                      json=mock_data, status_code=404)
    assert not pp.get_login_data("test_login")
