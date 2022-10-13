#Author : Atishay Jain
#Subject : 567A 
#HW 05A: Isolate External Dependencies

#Mock the Github API



import unittest
from unittest import TestCase
from unittest import mock
from unittest.mock import patch, MagicMock, Mock
from rx import return_value
import githubAPI567_Atishay
from githubAPI567_Atishay import Github


class TestGithub(unittest.TestCase):
    @mock.patch('githubAPI567_Atishay.Github', return_value = True)
    def test1(self, mock_github_results): 
        original_value = githubAPI567_Atishay.Github()
        expected_value = True
        self.assertEqual(expected_value, original_value)

    @mock.patch('githubAPI567_Atishay.Github', return_value = True)    
    def test2(self, mock_github_results):
        original_file = githubAPI567_Atishay.Github()
        expected_file = True
        self.assertEqual(expected_file, original_file) 
    

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

