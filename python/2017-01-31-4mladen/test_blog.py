import unittest
import blog


class TestBlog(unittest.TestCase):

    def test_001_init(self):

        with self.assertRaises(blog.EmailNotValidSize):
            self.assertTrue(blog.add_user('mla'))

        with self.assertRaises(blog.EmailNotValidException):
           self.assertTrue(blog.add_user('mladen'))

        with self.assertRaises(blog.EmailNotValidException):
           self.assertTrue(blog.add_user('ml@den@digitalcube.rs'))

        with self.assertRaises(blog.EmailNotValidException):
            self.assertTrue(blog.add_user('mla^den@digitalcube.rs'))

        with self.assertRaises(blog.EmailNotValidException):
            self.assertTrue(blog.add_user('msdasdn@digitalcube.rs.'))

        self.assertTrue(blog.add_user('mladen@digitalcube.rs'))

        with self.assertRaises(blog.UserAlreadyExistsException):
            self.assertTrue(blog.add_user('mladen@digitalcube.rs'))

    def test_002_init(self):

        with self.assertRaises(blog.SlugNotValidException):
            blog.add_article('kl&*^%$#@m','asdsad sa','','','')


        with self.assertRaises(blog.SlugNotValidException):
            blog.add_article('!@#!@#!@#!@#', 'asd!@#!@#@!asdasd', '', '', '')


        with self.assertRaises(blog.SlugNotValidException):
            blog.add_article(' ', 'asda!sdasd', '', '', '')

        with self.assertRaises(blog.TitleNotValidException):
            blog.add_article('alkmklmlkmsd', 'asda!sdasd', '', '', '')

        blog.add_article('alkmklmlkmsd', 'asda sdasd', '', '', '')




