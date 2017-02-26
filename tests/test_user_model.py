import unittest
from models import User

class UserModelTestCase(unittest.TestCase):
    def test_password_setter(self):
        u = User(password = 'cat')
        self.assertTrue(u.password_hash is not None)

if __name__ == '__main__':
    userTest = UserModelTestCase()
    userTest.test_password_setter()
