import unittest
import blog

class TestBlog(unittest.TestCase):

    def test_001_init(self):

        with self.assertRaises(blog.EmailNotValidException):
            self.assertTrue(blog.add_user('mladen'))

        self.assertTrue(blog.add_user('mladen@digitalcube.rs'))

        with self.assertRaises(blog.UserAlreadyExistsException):
            self.assertTrue(blog.add_user('mladen@digitalcube.rs'))