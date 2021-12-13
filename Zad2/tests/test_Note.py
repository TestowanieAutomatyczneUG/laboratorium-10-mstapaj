import unittest
from src.Note import Note


class TestNote(unittest.TestCase):
    def setUp(self):
        self.temp = Note('Ocena', 4)

    def test_get_name(self):
        self.assertEqual('Ocena', self.temp.get_name())

    def test_get_note(self):
        self.assertEqual(4, self.temp.get_note())

    def test_note_init_name(self):
        self.assertEqual('Ocena', self.temp.name)

    def test_note_init_note(self):
        self.assertEqual(4, self.temp.note)

    def test_note_init_name_none(self):
        with self.assertRaises(TypeError):
            Note(None, 4)

    def test_note_init_note_none(self):
        with self.assertRaises(TypeError):
            Note('Ocena', None)

    def test_note_init_none(self):
        with self.assertRaises(TypeError):
            Note(None, None)

    def test_note_init_name_object(self):
        with self.assertRaises(TypeError):
            Note({}, 4)

    def test_note_init_note_object(self):
        with self.assertRaises(TypeError):
            Note('Ocena', {})

    def test_note_init_object(self):
        with self.assertRaises(TypeError):
            Note({}, {})

    def test_note_init_name_array(self):
        with self.assertRaises(TypeError):
            Note([], 4)

    def test_note_init_note_array(self):
        with self.assertRaises(TypeError):
            Note('Ocena', [])

    def test_note_init_array(self):
        with self.assertRaises(TypeError):
            Note([], [])

    def test_note_init_name_true(self):
        with self.assertRaises(TypeError):
            Note(True, 4)

    def test_note_init_note_true(self):
        with self.assertRaises(TypeError):
            Note('Ocena', True)

    def test_note_init_true(self):
        with self.assertRaises(TypeError):
            Note(True, True)

    def test_note_init_name_false(self):
        with self.assertRaises(TypeError):
            Note(False, 4)

    def test_note_init_note_false(self):
        with self.assertRaises(TypeError):
            Note('Ocena', False)

    def test_note_init_false(self):
        with self.assertRaises(TypeError):
            Note(False, False)

    def test_note_init_name_int(self):
        with self.assertRaises(TypeError):
            Note(4, 4)

    def test_note_init_name_float(self):
        with self.assertRaises(TypeError):
            Note(4.12, 4)

    def test_note_init_name_negative_int(self):
        with self.assertRaises(TypeError):
            Note(-4, 4)

    def test_note_init_name_negative_float(self):
        with self.assertRaises(TypeError):
            Note(-4.12, 4)

    def test_note_init_note_string(self):
        with self.assertRaises(TypeError):
            Note('Ocena', 'abc')

    def test_note_init_note_string_number(self):
        with self.assertRaises(TypeError):
            Note('Ocena', '12')

    def tearDown(self):
        self.temp=None