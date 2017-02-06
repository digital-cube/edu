from unittest import TestCase

import blog
import sequencer

class TestBlog(TestCase):

    def test_001_seq(self):

        self.assertEqual('u00000', sequencer.seq('users', sequencer.mock_seq))
        self.assertEqual('u00001', sequencer.seq('users', sequencer.mock_seq))


        self.assertEqual('p0000000', sequencer.seq('posts', sequencer.mock_seq))

        with self.assertRaises(sequencer.SequencerUnknownTableException):
            sequencer.seq('xxx', sequencer.mock_seq)
