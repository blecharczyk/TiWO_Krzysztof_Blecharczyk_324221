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
