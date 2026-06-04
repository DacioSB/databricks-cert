from pyspark.sql import DataFrame
from pyspark.sql import functions as F
from src.utils import get_logger

logger = get_logger(__name__)


def clean_records(df: DataFrame) -> DataFrame:
    """Drop rows with null primary keys and remove soft-deleted records."""
    logger.info("Cleaning records: dropping nulls and deleted rows")
    return (
        df
        .dropna(subset=["id"])
        .filter(F.col("status") != "deleted")
    )


def add_ingestion_timestamp(df: DataFrame) -> DataFrame:
    """Add a column recording when this record was ingested."""
    return df.withColumn("ingested_at", F.current_timestamp())