import unittest
import blog

import sequencer


class TestBlog(unittest.TestCase):

    def randomword(self, length, type):

        import random
        random_string = ""

        if type == 'id':
            for i in range(length):
                random_string += (str(chr(random.randint(97, 122))))  # intended to put tab space.

        if type == 'words':
            a = ('hello', 'work', 'welcome', 'people', 'good', 'programming')
            for i in range(0,length):
                s = random.choice(a)
                if i >= 1:
                    s = ' '+s
                random_string += s

        return random_string

    def add_user(self, email):
        id_user = blog.add_user(email)
        return id_user

    def add_article(self, id_user=None, email=None):
        title = self.randomword(10, 'words')
        if not id_user:
            id_user = self.add_user(email)
            print(id_user)
        return blog.add_article('', title, id_user, '', '')

    #sequencer tests
    def test_0000_test_sequencer(self):

        self.assertEqual('u00000', sequencer.seq('users', sequencer.mock_seq))
        self.assertEqual('u00001', sequencer.seq('users', sequencer.mock_seq))


        self.assertEqual('p0000000', sequencer.seq('posts', sequencer.mock_seq))

        with self.assertRaises(sequencer.SequencerUnknownTableException):
            sequencer.seq('xxx', sequencer.mock_seq)




    #user tests

    def test_000_delete_all_users(self):

        self.assertEqual(0, blog.get_sum_users())

        id = self.add_user('newuser@dcube.rs')

        self.assertEqual(1, blog.get_sum_users())

        self.assertTrue(blog.delete_all_users())

        self.assertEqual(0, blog.get_sum_users())

    def test_001_get_users(self):

        self.assertEqual(0, blog.get_sum_users())
        #users doesnt exist
        with self.assertRaises(blog.UsersDoesntExist):
            blog.get_users()

        #add 2 users and get list of users
        blog.add_user('mladen0@digital.com')
        blog.add_user('mladen1@digital.com')
        blog.add_user('mladen3@digital.com')
        self.assertEqual(3,blog.get_sum_users())

        self.assertTrue(blog.get_users())
        blog.delete_all_users()

    def test_002_add_user(self):

        #not valid size
        with self.assertRaises(blog.EmailNotValidSize):
            self.assertTrue(blog.add_user('mla'))

        #not valid email
        with self.assertRaises(blog.EmailNotValidException):
           self.assertTrue(blog.add_user('mladen'))

        #not valid duplicate @
        with self.assertRaises(blog.EmailNotValidException):
           self.assertTrue(blog.add_user('ml@den@digitalcube.rs'))

        #invalid char ^
        with self.assertRaises(blog.EmailNotValidException):
            self.assertTrue(blog.add_user('mla^den@digitalcube.rs'))

        #not valid dot at the end of email
        with self.assertRaises(blog.EmailNotValidException):
            self.assertTrue(blog.add_user('msdasdn@digitalcube.rs.'))

        self.assertEqual(0, blog.get_sum_users())

        #add new user
        self.add_user('nikola@nnn.com')

        self.assertEqual(1, blog.get_sum_users())

        #user already exist
        with self.assertRaises(blog.UserAlreadyExistsException):
            self.assertTrue(self.add_user('nikola@nnn.com'))

        blog.delete_all_users()

    def test_003_get_user(self):
        #user with given id doesnt exist
        self.assertEqual(0, blog.get_sum_users())

        with self.assertRaises(blog.UserDoesntExist):
            blog.get_user('uOOO1')

        # add new user with given email, get id and check user exists
        id = blog.add_user('mladen@digital.com')
        self.assertEqual(1, blog.get_sum_users())

        self.assertTrue(blog.get_user(id))

        blog.delete_all_users()

    def test_004_delete_user(self):

        self.assertEqual(0, blog.get_sum_users())
        # add user with given email, delete it and check it again. Except user doesent exist
        id = self.add_user('newuser@dcube.rs')

        self.assertEqual(1, blog.get_sum_users())

        self.assertTrue(blog.delete_user(id))
        #ispitaj da li je skinuo jednog
        with self.assertRaises(blog.UserDoesntExist):
            blog.delete_user(id)

        self.assertEqual(0, blog.get_sum_users())




    #article tests
    def test_005_delete_all_articles(self):

        self.assertEqual(0, blog.get_sum_articles())

        id = self.add_article(None,'newuser@dcube.rs')

        self.assertEqual(1, blog.get_sum_articles())

        self.assertTrue(blog.delete_all_articles())

        self.assertEqual(0, blog.get_sum_articles())

    def test_006_delete_article(self):


        self.assertEqual(0, blog.get_sum_articles())

        id_article = self.add_article(None,'mlasadd@mladen.com')

        self.assertEqual(1, blog.get_sum_articles())

        self.assertTrue(blog.delete_article(id_article))

        self.assertEqual(0, blog.get_sum_articles())

    def test_007_add_article(self):
        self.assertEqual(0, blog.get_sum_articles())

        id_user = self.add_user('mlad@mladen.com')

        with self.assertRaises(blog.SlugNotValidException):
            blog.add_article('slug E! rorsti', 'Artical title', id_user,'', '')

        with self.assertRaises(blog.SlugNotValidException):
            blog.add_article('Slug Eror!@#!@#!@#!@#', 'Title with some char', id_user, '', '')

        with self.assertRaises(blog.TitleNotValidException):
            blog.add_article(' ', 'Title with Not valid Char !sdasd', id_user, '', '')

        with self.assertRaises(blog.TitleNotValidException):
            blog.add_article('correctslug', 'not Valid Title !sdasd', id_user, '', '')

        blog.add_article('correctslugsd', 'asda sdasd', id_user, '', '')

        self.assertEqual(1, blog.get_sum_articles())

        with self.assertRaises(blog.ArticleAlreadyExistsException):
            blog.add_article('correctslugsd', 'asda sdasd', id_user, '', '')

        with self.assertRaises(blog.ArticleAlreadyExistsException):
            blog.add_article('', 'ispravan stitle', id_user, '', '')

        self.assertTrue(blog.delete_all_articles())
        self.assertTrue(blog.delete_all_users())

    def test_008_get_articles(self):
        self.assertEqual(0, blog.get_sum_articles())
        self.assertEqual(0, blog.get_sum_users())

        self.add_article(None,'aSasa@sads.com')
        self.add_article(None,'aSassa@sads.com')
        self.add_article(None,'aSasssa@sads.com')

        self.assertEqual(3, blog.get_sum_articles())
        self.assertEqual(3, blog.get_sum_users())

        self.assertTrue(blog.delete_all_users())
        self.assertTrue(blog.delete_all_articles())

    def test_009_get_article(self):
        self.assertEqual(0, blog.get_sum_articles())
        self.assertEqual(0, blog.get_sum_users())

        id = self.add_article(None, 'aSasaasd@sads.com')
        id2 =self.add_article(None, 'aSassa@sads.com')
        #didati get artikal sa errorom
        self.assertEqual(2, blog.get_sum_articles())
        self.assertEqual(2, blog.get_sum_users())

        title = blog.get_article(id2).title
        self.assertEqual(title, blog.get_article(id2).title)
        self.assertFalse(blog.get_article('asdasdas'))

        self.assertTrue(blog.delete_all_users())
        self.assertTrue(blog.delete_all_articles())

    def test_010_edit_article(self):
        self.assertEqual(0, blog.get_sum_articles())
        self.assertEqual(0, blog.get_sum_users())

        with self.assertRaises(blog.ArticleDoesntExist):
            blog.edit_article('psadasdsa','asdasdasd','asdasdasdasdasd')
        # self.assertTrue(blog.delete_all_articles())

        id_article = self.add_article(None,'mmm@mmm.com')
        self.assertEqual(1, blog.get_sum_users())
        self.assertEqual(1, blog.get_sum_articles())

        title = blog.get_article(id_article).title
        self.assertEqual(title, blog.get_article(id_article).title)

        self.assertTrue(blog.edit_article(id_article, 'askkdakjkjsdasd', 'asdasdasdasdasd'))

        title = blog.get_article(id_article).title
        self.assertEqual(title, blog.get_article(id_article).title)






    #article - tags and comment
    def test_011_add_edit_tags_init(self):
        id_article = self.add_article(None,'artikal@from.tags')

        # tags = set(self.randomword(i, 'words') for i in range(1,3))
        # tags0 = set(self.randomword(i, 'words') for i in range(1,3))
        tags1 = [self.randomword(i, 'words') for i in range(1,3)]

        #tags not walid
        with self.assertRaises(blog.TagsNotValidException):
            blog.add_edit_tags(id_article, tags1)

        #add new tags
        self.assertTrue(blog.add_edit_tags(id_article, {'prvi','drugi','treci'}))

        #check is alredy in db and add only new tags
        self.assertTrue(blog.add_edit_tags(id_article, {'prvi','drugi','treci','cetvrti','peti'}))

        #
        # blog.add_article('xxxalkmklmlkmsd', 'sss asda sdasd', '')
        # blog.add_edit_tags('xxxalkmklmlkmsd', {'mladen', 'peric'})

    def test_012_get_tags(self):
        with self.assertRaises(blog.TagsDoesntExist):
             self.assertTrue(blog.get_tags('asdasda'))

        # id_user = self.add_user('mlasdad@mladen.com')

    def test_013_add_comment(self):
        pass
    def test_014_edit_comment(self):
        pass
    def test_015_delete_comment(self):
        pass
    def test_016_get_comments(self):
        pass


    #other
    def test_017_edit_number_of_likes(self):
        pass
    def test_018_edit_number_of_comments(self):
        pass
    def test_019_approve_comment(self):
        pass
    def test_020_change_slug(self):
        pass
