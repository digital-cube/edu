from unittest import TestCase

import blog
import sequencer

DEFAULT_TEST_PASSWORD = '123'
DEFAULT_AUTHOR_ID = 'u00003'

# INTEGRACIONI TEST JER SE KORISTI BAZA..

sequencer.seq.f = sequencer.mock_seq

class TestBlog(TestCase):

    def test_001_seq(self):

        self.assertEqual('u00000', sequencer.seq('users'))
        self.assertEqual('u00001', sequencer.seq('users'))


        self.assertEqual('p0000000', sequencer.seq('posts'))

        with self.assertRaises(sequencer.SequencerUnknownTableException):
            sequencer.seq('xxx')



    def test_002_blog_check_password(self):
        self.assertFalse(blog.get_blog().check_password('123'))
        self.assertFalse(blog.get_blog().check_password('12'))

    def test_003_add_user_to_db(self):

        with self.assertRaises(blog.UserPasswordNotStrongEnough):
            blog.get_blog().create_user('author@digitalcube.rs', '12')

        blog.get_blog().create_user('author@digitalcube.rs', DEFAULT_TEST_PASSWORD)
        with self.assertRaises(blog.UsernameAlreadyExistsException):
            blog.get_blog().create_user('author@digitalcube.rs', DEFAULT_TEST_PASSWORD)


    def test_004_blog_login_user(self):

        self.assertFalse(blog.get_blog().login_user('author@digitalcube.rs', 'abc'))
        self.assertEquals(DEFAULT_AUTHOR_ID, blog.get_blog().login_user('author@digitalcube.rs', DEFAULT_TEST_PASSWORD))

    def test_005_add_blog_post(self):

        author = blog.get_blog().get_user_by_id(DEFAULT_AUTHOR_ID)


        blog.get_blog().add_post(author, 'my-first-post', 'My first post', 'Hi')

        with self.assertRaises(blog.InvalidSlugException):
            blog.get_blog().add_post(author, 'my first-post', 'My first post', 'Hi')

        with self.assertRaises(blog.InvalidSlugException):
            blog.get_blog().add_post(author, 'my-first-post', 'My first post', 'Hi')

    def test_006_is_slug_in_db(self):

        self.assertTrue(blog.get_blog().is_slug_in_db('my-first-post'))
        self.assertFalse(blog.get_blog().is_slug_in_db('x-my-first-post'))

    def test_007_check_slug(self):
        self.assertTrue(blog.get_blog().check_slug('this-is-slug'))
        self.assertFalse(blog.get_blog().check_slug('this-is slug'))
        self.assertFalse(blog.get_blog().check_slug('This-is-slug'))
        self.assertTrue(blog.get_blog().check_slug('this.is.slug'))

    def test_008_check_slug_aviability(self):
        self.assertFalse(blog.get_blog().check_slug_aviability('my-first-post'))
        self.assertTrue(blog.get_blog().check_slug('this-is-slug'))

    def test_009_blog_make_slug(self):
        self.assertEqual('slug', blog.get_blog().make_slug('Slug'))
        self.assertEqual('my-title', blog.get_blog().make_slug('My Title'))
        self.assertEqual('my-first-title', blog.get_blog().make_slug('My "First" Title'))

    def test_010_get_post_by_slug(self):

        post = blog.get_blog().get_post_by_slug('my-first-post')

        print(post.title)
        print(post.author.username)

    def test_011_check_pass(self):

        DEFAULT_TEST_PASSWORD = 'aLek.san1dar)'

        self.assertFalse(blog.get_blog().check_password('aleksandar'))
        self.assertFalse(blog.get_blog().check_password('ALEKSANDAR'))
        self.assertFalse(blog.get_blog().check_password('1231234343'))
        self.assertTrue(blog.get_blog().check_password('aLek.san1dar)'))
        self.assertTrue(blog.get_blog().check_password('5454567d'))
        self.assertFalse(blog.get_blog().check_password('123GooD.2'))
        self.assertFalse(blog.get_blog().check_password('qweGooD.2'))
        self.assertFalse(blog.get_blog().check_password('asdGooD.2'))
        self.assertFalse(blog.get_blog().check_password('zxcGooD.2'))
        self.assertFalse(blog.get_blog().check_password('11111111'))

        with self.assertRaises(blog.UserPasswordNotValid):
            blog.get_blog().create_user('author@digitalcube.rs', 'aleksandar')
        with self.assertRaises(blog.UserPasswordNotValid):
            blog.get_blog().create_user('author@digitalcube.rs', '1231234343')
        blog.get_blog().create_user('autuuor@digitalcube.rs', DEFAULT_TEST_PASSWORD)
        with self.assertRaises(blog.UsernameAlreadyExistsException):
            blog.get_blog().create_user('autuuor@digitalcube.rs', DEFAULT_TEST_PASSWORD)

