import unittest
from src.NotesService import NotesService
from src.NotesStorage import NotesStorage
from src.Note import Note
from unittest.mock import patch


class TestNotesService(unittest.TestCase):

    def setUp(self):
        self.temp = NotesService()

    @patch.object(NotesStorage, 'add')
    def test_NotesService_add(self, mock_method):
        mock_method.return_value = ['Text']
        note = Note('Text', 4)
        self.assertEqual(['Text'], self.temp.add(note))

    @patch.object(NotesStorage, 'add')
    def test_NotesService_add_2(self, mock_method):
        mock_method.return_value = ['abc', 'def', 'Text']
        note = Note('Text', 4)
        self.assertEqual(['abc', 'def', 'Text'], self.temp.add(note))

    @patch.object(NotesStorage, 'add')
    def test_NotesService_add_none(self, mock_method):
        mock_method.side_effect = TypeError
        self.assertRaises(TypeError, self.temp.add, None)

    @patch.object(NotesStorage, 'add')
    def test_NotesService_add_object(self, mock_method):
        mock_method.side_effect = TypeError
        self.assertRaises(TypeError, self.temp.add, {})

    @patch.object(NotesStorage, 'add')
    def test_NotesService_add_array(self, mock_method):
        mock_method.side_effect = TypeError
        self.assertRaises(TypeError, self.temp.add, [])

    @patch.object(NotesStorage, 'add')
    def test_NotesService_add_true(self, mock_method):
        mock_method.side_effect = TypeError
        self.assertRaises(TypeError, self.temp.add, True)

    @patch.object(NotesStorage, 'add')
    def test_NotesService_add_false(self, mock_method):
        mock_method.side_effect = TypeError
        self.assertRaises(TypeError, self.temp.add, False)

    @patch.object(NotesStorage, 'add')
    def test_NotesService_add_int(self, mock_method):
        mock_method.side_effect = TypeError
        self.assertRaises(TypeError, self.temp.add, 3)

    @patch.object(NotesStorage, 'add')
    def test_NotesService_add_float(self, mock_method):
        mock_method.side_effect = TypeError
        self.assertRaises(TypeError, self.temp.add, 4.12)

    @patch.object(NotesStorage, 'add')
    def test_NotesService_add_negative_int(self, mock_method):
        mock_method.side_effect = TypeError
        self.assertRaises(TypeError, self.temp.add, -5)

    @patch.object(NotesStorage, 'add')
    def test_NotesService_add_negative_float(self, mock_method):
        mock_method.side_effect = TypeError
        self.assertRaises(TypeError, self.temp.add, -1.23)

    @patch.object(NotesStorage, 'getAllNotesOf')
    def test_averageOf_note(self, mock_method):
        mock_method.return_value = [Note("note", 2), Note("note", 4), Note("note", 5), Note("note", 3)]
        self.assertEqual(self.temp.averageOf("note"), 3.5)

    @patch.object(NotesStorage, 'getAllNotesOf')
    def test_averageOf_note_2(self, mock_method):
        mock_method.return_value = [Note("note", 3)]
        self.assertEqual(self.temp.averageOf("note"), 3)

    @patch.object(NotesStorage, 'getAllNotesOf')
    def test_averageOf_note(self, mock_method):
        mock_method.return_value = [Note("note", 2), Note("note", 4), Note("note", 5), Note("note", 2), Note("note", 2),
                                    Note("note", 2), Note("note", 3), Note("note", 3), Note("note", 3), Note("note", 3)]
        self.assertEqual(self.temp.averageOf("note"), 2.9)

    @patch.object(NotesStorage, 'getAllNotesOf')
    def test_averageOf_zero_notes(self, mock_method):
        mock_method.return_value = []
        self.assertEqual(self.temp.averageOf("note"), 0)

    @patch.object(NotesStorage, 'getAllNotesOf')
    def test_averageOf_none(self, mock_method):
        mock_method.side_effect = TypeError
        self.assertRaises(TypeError, self.temp.averageOf, None)

    @patch.object(NotesStorage, 'getAllNotesOf')
    def test_averageOf_object(self, mock_method):
        mock_method.side_effect = TypeError
        self.assertRaises(TypeError, self.temp.averageOf, {})

    @patch.object(NotesStorage, 'getAllNotesOf')
    def test_averageOf_array(self, mock_method):
        mock_method.side_effect = TypeError
        self.assertRaises(TypeError, self.temp.averageOf, [])

    @patch.object(NotesStorage, 'getAllNotesOf')
    def test_averageOf_true(self, mock_method):
        mock_method.side_effect = TypeError
        self.assertRaises(TypeError, self.temp.averageOf, True)

    @patch.object(NotesStorage, 'getAllNotesOf')
    def test_averageOf_false(self, mock_method):
        mock_method.side_effect = TypeError
        self.assertRaises(TypeError, self.temp.averageOf, False)

    @patch.object(NotesStorage, 'getAllNotesOf')
    def test_averageOf_int(self, mock_method):
        mock_method.side_effect = TypeError
        self.assertRaises(TypeError, self.temp.averageOf, 3)

    @patch.object(NotesStorage, 'getAllNotesOf')
    def test_averageOf_float(self, mock_method):
        mock_method.side_effect = TypeError
        self.assertRaises(TypeError, self.temp.averageOf, 2.11)

    @patch.object(NotesStorage, 'getAllNotesOf')
    def test_averageOf_negative_int(self, mock_method):
        mock_method.side_effect = TypeError
        self.assertRaises(TypeError, self.temp.averageOf, -4)

    @patch.object(NotesStorage, 'getAllNotesOf')
    def test_averageOf_negative_float(self, mock_method):
        mock_method.side_effect = TypeError
        self.assertRaises(TypeError, self.temp.averageOf, -4.31)

    @patch.object(NotesStorage, "clear")
    def test_clear(self, mock_method):
        mock_method.return_value = []
        self.assertEqual(self.temp.clear(), [])
