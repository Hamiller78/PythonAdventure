import unittest

from World.Room import Room

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("A dark room", {}, [])
        self.neighbor_room = Room("A bright room", {}, [])
        self.room.add_connection("north", self.neighbor_room)
        self.room.add_item("Key")

    def test_get_description(self):
        self.assertEqual(self.room.get_description(), "A dark room")

    def test_set_description(self):
        self.room.set_description("A bright room")
        self.assertEqual(self.room.get_description(), "A bright room")

    def test_add_item(self):
        self.room.add_item("Key")
        self.assertIn("Key", self.room.get_items())

    def test_remove_item(self):
        self.room.remove_item("Key")
        self.assertNotIn("Key", self.room.get_items())

    def test_connects_to(self):
        self.assertTrue(self.room.connects_to("north"))
        self.assertFalse(self.room.connects_to("south"))

    def test_add_connection(self):
        new_room = Room("A new room", {}, [])
        self.room.add_connection("east", new_room)
        self.assertEqual(self.room.connects_to("east"), new_room)

    def test_remove_connection(self):
        self.room.remove_connection("north")
        self.assertIsNone(self.room.connects_to("north"))

    def test_remove_connection_not_found(self):
        with self.assertRaises(KeyError):
            self.room.remove_connection("south")

if __name__ == "__main__":
    unittest.main()
