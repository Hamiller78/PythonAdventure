import unittest

from World.Player import Player

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player("TestPlayer")

    def test_add_to_inventory(self):
        self.player.add_to_inventory("Sword")
        self.assertIn("Sword", self.player.get_inventory())

    def test_remove_from_inventory(self):
        self.player.add_to_inventory("Shield")
        self.player.remove_from_inventory("Shield")
        self.assertNotIn("Shield", self.player.get_inventory())

    def test_remove_from_inventory_item_not_found(self):
        with self.assertRaises(ValueError) as context:
            self.player.remove_from_inventory("Potion")
        self.assertEqual(str(context.exception), "Item 'Potion' not found in inventory.")

    def test_inventory_initially_empty(self):
        self.assertEqual(self.player.get_inventory(), [])

    def test_add_multiple_items_to_inventory(self):
        items = ["Sword", "Shield", "Potion"]
        for item in items:
            self.player.add_to_inventory(item)
        self.assertEqual(self.player.get_inventory(), items)

    def test_remove_item_not_affect_others(self):
        self.player.add_to_inventory("Sword")
        self.player.add_to_inventory("Shield")
        self.player.remove_from_inventory("Sword")
        self.assertIn("Shield", self.player.get_inventory())
        self.assertNotIn("Sword", self.player.get_inventory())

    def test_set_current_room_to_none(self):
        self.player.set_current_room("Kitchen")
        self.player.set_current_room(None)
        self.assertIsNone(self.player.get_current_room())

if __name__ == "__main__":
    unittest.main()