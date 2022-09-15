import unittest
from unittest import mock
from .data_utils.DataLoader import DataLoader


def mock_requests_get(*args, **kwargs):
  class MockResponse():
    def __init__(self, content, status_code):
      self.content = content
      self.status_code = status_code
  return MockResponse(b'id\tname\tdesignation\n1\traj\tsoftware\tengineer\n2\tsowmya\tml\tengineer', 200) 
  


class TestDataLoader(unittest.TestCase):

  @mock.patch('requests.get', mock_requests_get)
  def test_dataLoad(self, mock_get):
    dl = DataLoader('dummyurl.com')
    self.assertEqual(dl.df.shape, (2,3))

  
if __name__ == '__main__':
  unittest.main()
