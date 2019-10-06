import unittest
from credentials import Credentials

class TestCredentials(unittest.TestCase):
    def setUp(self):
        """
        sets up a fake user before each test
        """    
        self.test_credential = Credentials('boxxy', 'lovvy', '9090')
        Credentials.credentials_list.append(self.test_credential)
    
    def tearDown(self):
        """
        cleans up after each test, removes all fake credentials.
        :return:
        """
        User.users_list.clear()
        Credentials.credentials_list.clear()

    def test_add_credentials(self):
        new_credential = Credentials('skype', 'smile', '9999')
        self.assertEqual(new_credential.account, 'skype')
        self.assertEqual(new_credential.username, 'smile')
        self.assertEqual(new_credential.password, '9999')

    def test_save_credentials(self):
        Credentials.save_credential(self.test_credential)
        has_credential = self.test_credential in Credentials.credentials_list
        self.assertTrue(has_credential)        
     def test_find_credential(self):
        credential = Credentials.find_credential(self.test_credential.account)
        self.assertEqual(credential, self.test_credential)        

    def test_get_all_credentials(self):
        credentials = Credentials.get_all_credentials()
        self.assertEqual(Credentials.credentials_list, credentials)
