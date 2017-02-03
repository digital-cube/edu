
import unittest

from stack import Stack, are_brackets_correct, StackIsEmptyException, Queue, QueueIsEmptyException

class TestQueue(unittest.TestCase):

    def test_queue_001(self):
        q = Queue()
        self.assertTrue(q.is_empty())

    def test_queue_002(self):
        q = Queue()
        self.assertTrue(q.is_empty())
        q.enqueue('A')
        self.assertFalse(q.is_empty())
        self.assertFalse(q.is_empty())
        self.assertEqual(q.dequeue(), 'A')
        self.assertTrue(q.is_empty())

    def test_queue_003(self):
        q = Queue()
        self.assertTrue(q.is_empty())
        with self.assertRaises(QueueIsEmptyException):
            self.assertEqual(q.dequeue(), 'A')


    def test_queue_004(self):
        q = Queue()
        self.assertTrue(q.is_empty())
        q.enqueue('A')
        self.assertFalse(q.is_empty())
        self.assertFalse(q.is_empty())
        q.enqueue('B')
        self.assertFalse(q.is_empty())
        self.assertFalse(q.is_empty())
        self.assertEqual(q.dequeue(), 'A')
        self.assertEqual(q.dequeue(), 'B')
        self.assertTrue(q.is_empty())


class TestStack(unittest.TestCase):

    def test_stack_001(self):
        s = Stack()
        self.assertEqual(len(s), 0)
        self.assertTrue(s.is_empty())

    def test_stack_002(self):
        s = Stack()
        s.push('[')
        self.assertEqual(len(s), 1)
        self.assertFalse(s.is_empty())

    def test_stack_003(self):
        s = Stack()
        s.push('[')
        self.assertEqual(len(s), 1)
        self.assertFalse(s.is_empty())
        self.assertEqual(s.pop(),'[')
        self.assertEqual(len(s), 0)
        self.assertTrue(s.is_empty())

    def test_stack_004(self):
        s = Stack()
        s.push('[')
        s.push('{')
        self.assertEqual(len(s), 2)
        self.assertFalse(s.is_empty())
        self.assertEqual(s.pop(), '{')
        self.assertEqual(len(s), 1)
        self.assertFalse(s.is_empty())
        self.assertEqual(s.pop(), '[')
        self.assertEqual(len(s), 0)
        self.assertTrue(s.is_empty())

    def test_stack_005(self):
        s = Stack()
        self.assertEqual(len(s), 0)
        self.assertTrue(s.is_empty())
        with self.assertRaises(StackIsEmptyException):
            s.pop()


class TestBrackets(unittest.TestCase):

    def test_brackets_01(self):
        self.assertTrue(are_brackets_correct("([]())[]"))

    def test_brackets_02(self):
        self.assertFalse(are_brackets_correct("((())"))

    def test_brackets_03(self):
        self.assertFalse(are_brackets_correct("()[]())[]"))

    def test_brackets_04(self):
        self.assertFalse(are_brackets_correct(")[]"))
