from toolshop.tools.data import Sql
from toolshop.tools.gcp import AuthenticateToGCP


def test_bq_sql_query():
    AuthenticateToGCP(require_confirmation=False)()

    sql = Sql()

    res = sql(
        sql_query="SELECT * FROM `bigquery-public-data.samples.shakespeare` LIMIT 10",
        database_uri="bigquery://",
    )

    assert "word" in res
    assert "word_count" in res 


