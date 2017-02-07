import unittest
import blog


class TestBlog(unittest.TestCase):

    def randomword(self,length,type):

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

    def test_add_user(self):

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

        self.add_user('nikola@nnn.com')

        with self.assertRaises(blog.UserAlreadyExistsException):
            self.assertTrue(self.add_user('nikola@nnn.com'))

    def test_delete_article(self):

        id_user = self.add_user('mlad@mladen.com')
        with self.assertRaises(blog.ArticleDoesntExist):
            blog.delete_article('asdasdasd')

        id_article = blog.add_article('slug rorsti', 'Artical title', id_user, '', '')
        self.assertTrue(blog.delete_article(id_article))
            # with self.assertRaises(blog.ArticleDoesntExist):
        #     blog.delete_article(id_article)

        # with self.assertRaises(blog.ArticleDoesntExist):
        #     blog.delete_article('somesaid')

    def test_add_article(self):
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

        with self.assertRaises(blog.ArticleAlreadyExistsException):
            blog.add_article('correctslugsd', 'asda sdasd', id_user, '', '')

        with self.assertRaises(blog.ArticleAlreadyExistsException):
            blog.add_article('', 'ispravan stitle', id_user, '', '')

    def test_add_edit_tags_init(self):
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

    def test_edit_article(self):
        id_user = self.add_user('mlad@mladen.com')
        with self.assertRaises(blog.SlugNotValidException):
            blog.edit_article('slugneki', 'Articsal title', id_user,'', '')

    def test_get_user(self):
        with self.assertRaises(blog.UserDoesntExist):
             blog.get_users('asdasdas')

        id = blog.add_user('mladen@digital.com')
        # self.assertTrue(blog.get_users(id))

    def test_get_users(self):
        with self.assertRaises(blog.UsersDoesntExist):
             self.assertTrue(blog.get_all_users())

        id = blog.add_user('mladen@digital.com')
        self.assertTrue(blog.get_all_users())

    #not yet
    def test_get_tags(self):
        with self.assertRaises(blog.TagsDoesntExist):
             self.assertTrue(blog.get_tags('asdasda'))

        # id_user = self.add_user('mlasdad@mladen.com')

    def test_get_articles(self):
        pass
    def test_get_article(self):
        pass
    def test_add_comment(self):
        pass
    def test_edit_comment(self):
        pass
    def test_delete_comment(self):
        pass
    def test_get_comments(self):
        pass
    def test_edit_number_of_likes(self):
        pass
    def test_edit_number_of_comments(self):
        pass
