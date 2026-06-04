import pytest
from pyspark.sql import SparkSession
from src.transformations import clean_records, add_ingestion_timestamp

@pytest.fixture
def spark_session():
    return SparkSession.builder.appName("Test").getOrCreate()

def test_clean_records_drops_null_id(spark_session):
    df = spark_session.createDataFrame([(1, "a"), (None, "b")], schema="id LONG, status STRING")
    result = clean_records(df)
    assert result.count() == 1
    assert result.collect()[0]["id"] == 1
def test_clean_records_removes_deleted(spark):
    df = spark.createDataFrame(
        [(1, "active"), (2, "deleted")],
        schema="id LONG, status STRING"
    )
    result = clean_records(df)
    assert result.count() == 1
def test_add_ingestion_timestamp_adds_column(spark):
    df = spark.createDataFrame([(1, "active")], schema="id LONG, status STRING")
    result = add_ingestion_timestamp(df)
    assert "ingested_at" in result.columns