import pytest

from src.hash_table import HashTable


class TestHashTable:
    def test_create_hash_table_with_given_size_and_check_size(self):
        # given
        hash_table_size = 5

        # when
        hash_table = HashTable(hash_table_size)

        # then
        assert hash_table.get_size() == hash_table_size

    def test_insert_two_elements_to_hahs_table_and_get_them(self):
        # given
        table = HashTable(5)

        # when
        table.insert("key1", "value1")
        table.insert("key2", "value2")

        # then
        assert table.get("key1") == "value1"
        assert table.get("key2") == "value2"

    def test_insert_two_elements_and_handle_collision(self):
        # given
        table = HashTable(10)

        # when
        table.insert("key", "value")
        table.insert("key2", "value2")

        # then
        assert table.get("key") == "value"
        assert table.get("key2") == "value2"

    def test_update_existing_key(self):
        # given
        table = HashTable(10)

        # when
        table.insert("key1", "value1")
        table.insert("key1", "new_value")

        # then
        assert table.get("key1") == "new_value"

    def test_remove_existing_element(self):
        # given
        table = HashTable(10)
        table.insert("key", "value")
        table.insert("key1", "value1")

        # when
        table.remove("key")

        # then
        with pytest.raises(KeyError):
            table.get("key")
        assert table.get("key1") == "value1"

    def test_remove_nonexistent_key(self):
        # given
        table = HashTable(10)

        # when
        table.insert("key1", "value1")

        # then
        with pytest.raises(KeyError):
            table.remove("nonexistent_key")
