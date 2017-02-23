from unittest import TestCase

import blog
import sequencer

DEFAULT_TEST_PASSWORD = '123qweQWE!@#'
DEFAULT_AUTHOR_ID = 'u00003'
DEFAULT_POST_ID = 'p0000001'

from db import session, User
from sequencer import seq

# INTEGRACIONI TEST JER SE KORISTI BAZA..

sequencer.seq.f = sequencer.mock_seq

class TestBlog(TestCase):

    #user tests
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



    #post tests
    def test_005_add_blog_post(self):

        author = blog.get_blog().get_user_by_id(DEFAULT_AUTHOR_ID)

        blog.get_blog().add_post(author, 'my-first-post', 'My first post', 'Hi')
        blog.get_blog().add_post(author, 'my-second-post', 'My second post', 'Hi')

        with self.assertRaises(blog.InvalidSlugException):
            blog.get_blog().add_post(author, 'my first-post', 'My first post', 'Hi')

        blog.get_blog().add_post(author, 'my-first-post', 'My second post second', 'Hi')

        blog.get_blog().add_post(author, 'my-first-post', 'My second post second', 'Hi')

    def test_014_get_blog_by_id(self):
        self.assertEqual('My first post', blog.get_blog().get_post(DEFAULT_POST_ID).title)

    def test_013_get_all_posts(self):
        # print(blog.get_blog().get_all_post())
        # print(blog.get_blog().get_all_post(date='2017-02-20'))
        list2 =[]
        list = ['My first post', 'My second post',  'My second post second', 'My second post second', 'My 3rd post', 'My 4th post']
        for i in range(len(list)):

            # print(blog.get_blog().get_all_post()[i].title)
            self.assertEqual(list[i],blog.get_blog().get_all_post()[i].title)
            self.assertEqual(list2, blog.get_blog().get_all_post(date='2017-02-20'))

        self.assertEqual('My first post',blog.get_blog().get_all_post(word='My first')[0].title)

    def test_015_edit_blog_post(self):

        self.assertEqual('My first post', blog.get_blog().get_post(DEFAULT_POST_ID).title)
        blog.get_blog().edit_post(DEFAULT_POST_ID, 'My first sss', 'Hi ss')
        self.assertEqual('My first sss', blog.get_blog().get_post(DEFAULT_POST_ID).title)

    def test_017_delete_blog_post(self):
        self.assertTrue(blog.get_blog().delete_post('p0000004'))
        self.assertEqual(None, blog.get_blog().get_post('p0000004'))
        # blog.get_blog().edit_post(DEFAULT_POST_ID, 'My first sss', 'Hi ss')
        # self.assertEqual('My first sss', blog.get_blog().get_post(DEFAULT_POST_ID).title)

    def test_010_get_post_by_slug(self):

        self.assertEqual(['my-first-post', 'my-second-post','my-second-post-second','my-second-post-second-1'],
                         [post.slug for post in
                          blog.get_blog().get_user_by_id(DEFAULT_AUTHOR_ID).posts])

        self.assertEqual('My first post',
                         blog.get_blog().get_post_by_slug('my-first-post').title)

        self.assertEqual('author@digitalcube.rs',
                         blog.get_blog().get_post_by_slug('my-first-post').author.username)


    #slug tests
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


    #tags test
    def test_011_post_tags(self):
        author = blog.get_blog().get_user_by_id(DEFAULT_AUTHOR_ID)
        post = blog.get_blog().add_post(author, 'my-tagged-post', 'My 3rd post', 'Hi5')

        self.assertEqual('my-tagged-post',
                         [post.slug for post in
                          blog.get_blog().get_user_by_id(DEFAULT_AUTHOR_ID).posts][-1])

        blog.get_blog().tag_it(post, ['novo', 'aktuelno', 'interesantno'])

        self.assertEqual(['novo', 'aktuelno', 'interesantno'],
                         [tag.name for tag in post.tags])

        post2 = blog.get_blog().add_post(author, 'my-tagged2-post', 'My 4th post', 'hi4')

        self.assertEqual('my-tagged2-post',
                         [post.slug for post in
                          blog.get_blog().get_user_by_id(DEFAULT_AUTHOR_ID).posts][-1])

        blog.get_blog().tag_it(post2, ['novo', 'plavo'])
        self.assertEqual(['novo', 'plavo'],
                         [tag.name for tag in post2.tags])

        self.assertEqual(['my-tagged-post', 'my-tagged2-post'],
                         [post.slug for post in
                          blog.get_blog().all_posts_tagged_with('Novo')])

        self.assertEqual(['my-tagged2-post'],
                         [post.slug for post in
                          blog.get_blog().all_posts_tagged_with('PLAVO')])

    #post commentars
    def test_012_user_add_comments(self):
        id = blog.get_blog().create_guest('author@digitalcube.rs', 'Mladen', 'Milicevic')

        author = blog.get_blog().get_user_by_id(DEFAULT_AUTHOR_ID)
        guest = blog.get_blog().get_user_by_id('g000000000')
        post = blog.get_blog().get_post_by_slug('my-tagged2-post')

        self.assertEqual([], post.comments)

        post.add_comment(author,None,'bas je dobar ovaj post', False)
        post.add_comment(None,guest, 'jes vala', False)

        self.assertEqual(['bas je dobar ovaj post', 'jes vala'], [comment.comment_text for comment in post.comments])



    def test_024_guest_add_comment(self):
        author = blog.get_blog().get_user_by_id(DEFAULT_AUTHOR_ID)
        post = blog.get_blog().add_post(author, 'my-tagged-post', 'My 3rd post', 'Hi5')

        comments = post.comments

        pass

    def test_018_edit_comment(self):
        post = blog.get_blog().get_post_by_slug('my-tagged2-post')
        self.assertEqual(['bas je dobar ovaj post', 'jes vala'], [comment.comment_text for comment in post.comments])

        newComments = ['New je dobar ovaj post', 'New jes vala']
        for i in (0,len(post.comments)-1):
            self.assertTrue(blog.get_blog().edit_comment(post.comments[i].id, newComments[i]))

        post = blog.get_blog().get_post_by_slug('my-tagged2-post')

        self.assertEqual(['New je dobar ovaj post', 'New jes vala'],[comment.comment_text for comment in post.comments])

    # def test_026_add_guest_to_db(self):
    #
    #     with self.assertRaises(blog.EmailNotValid):
    #         blog.get_blog().create_guest('Mladen','Milicevic','authordigitalcube.rs')
    #
    #     blog.get_blog().create_guest('Mladen','Milicevic','author@digitalcube.rs')





    def test_020_delete_comment(self):
        post = blog.get_blog().get_post_by_slug('my-tagged2-post')

        self.assertTrue(blog.get_blog().delete_comment(post.comments[0].id))

        post = blog.get_blog().get_post_by_slug('my-tagged2-post')
        self.assertEqual(1,len(post.comments))

        self.assertEqual(['New jes vala'], [comment.comment_text for comment in post.comments])

    def test_022_approve_comment(self):
        # status
        pass

    def test_023_get_num_comments(self):
        pass

