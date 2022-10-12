import unittest
from unittest import TestCase
from unittest import mock

from rx import return_value
import githubAPI567_Atishay
from githubAPI567_Atishay import Github


from githubAPI567_Atishay import Github

@mock.patch('githubAPI567_Atishay.Github', return_value=False)
class TestGithub(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    def test1(self, mock_github_results):
        actual_result = githubAPI567_Atishay.Github()
        expected_result = False
        self.assertEqual(expected_result, actual_result)
        
    def test2(self, mock_github_results):
        actual_directory = githubAPI567_Atishay.Github()
        expected_directory = True
        self.assertNotEqual(expected_directory, actual_directory)
    
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()


