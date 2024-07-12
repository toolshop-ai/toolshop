import unittest
from toolshop.tools.data import Sql
from unittest.mock import patch, MagicMock

class TestSql(unittest.TestCase):

    @patch('toolshop.tools.data.sa.create_engine')
    def test_call(self, mock_create_engine):
        mock_engine = MagicMock()
        mock_result = MagicMock()

        # Setup mock to return columns and rows
        mock_result.keys.return_value = ['column1', 'column2']
        mock_result.__iter__.return_value = iter([
            ('value1', 'value2'),
            ('value3', 'value4')
        ])
        mock_engine.execute.return_value = mock_result
        mock_create_engine.return_value = mock_engine

        sql_tool = Sql()
        sql_query = 'SELECT * FROM test_table'
        database_uri = 'sqlite:///:memory:'

        expected_csv = 'column1,column2\nvalue1,value2\nvalue3,value4'
        result_csv = sql_tool.call(sql_query, database_uri)

        self.assertEqual(result_csv, expected_csv)

if __name__ == '__main__':
    unittest.main()
