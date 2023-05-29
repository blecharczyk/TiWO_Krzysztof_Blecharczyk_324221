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
        #given
        table = HashTable(5)

        #when
        table.insert("key1", "value1")
        table.insert("key2", "value2")

        #then
        assert table.get("key1") == "value1"
        assert table.get("key2") == "value2"
