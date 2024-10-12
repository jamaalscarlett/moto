import boto3

from moto import mock_aws, settings
from moto.core import DEFAULT_ACCOUNT_ID as ACCOUNT_ID
from moto.moto_api._internal import mock_random

TEST_REGION = "us-east-1" if settings.TEST_SERVER_MODE else "us-west-2"


def create_extended_s3_delivery_stream(client, stream_name):
    """Return ARN of a delivery stream created with an S3 destination."""
    return client.create_delivery_stream(
        DeliveryStreamName=stream_name,
        DeliveryStreamType="DirectPut",
        ExtendedS3DestinationConfiguration={
            "RoleARN": f"arn:aws:iam::{ACCOUNT_ID}:role/firehose_delivery_role",
            "BucketARN": "arn:aws:s3:::firehose-test",
            "Prefix": "myFolder/",
            "CompressionFormat": "UNCOMPRESSED",
            "DataFormatConversionConfiguration": {
                "Enabled": True,
                "InputFormatConfiguration": {"Deserializer": {"HiveJsonSerDe": {}}},
                "OutputFormatConfiguration": {
                    "Serializer": {"ParquetSerDe": {"Compression": "SNAPPY"}}
                },
                "SchemaConfiguration": {
                    "DatabaseName": stream_name,
                    "RoleARN": f"arn:aws:iam::{ACCOUNT_ID}:role/firehose_delivery_role",
                    "TableName": "outputTable",
                },
            },
        },
    )


def create_redshift_delivery_stream(client, stream_name):
    """Return ARN of a delivery stream created with a Redshift destination."""
    return client.create_delivery_stream(
        DeliveryStreamName=stream_name,
        RedshiftDestinationConfiguration={
            "RoleARN": f"arn:aws:iam::{ACCOUNT_ID}:role/firehose_delivery_role",
            "ClusterJDBCURL": "jdbc:redshift://host.amazonaws.com:5439/database",
            "CopyCommand": {
                "DataTableName": "outputTable",
                "CopyOptions": "CSV DELIMITER ',' NULL '\\0'",
            },
            "Username": "username",
            "Password": "password",
            "S3Configuration": {
                "RoleARN": f"arn:aws:iam::{ACCOUNT_ID}:role/firehose_delivery_role",
                "BucketARN": "arn:aws:s3:::firehose-test",
                "Prefix": "myFolder/",
                "BufferingHints": {"SizeInMBs": 123, "IntervalInSeconds": 124},
                "CompressionFormat": "UNCOMPRESSED",
            },
        },
    )


def create_elasticsearch_delivery_stream(client, stream_name):
    """Return delivery stream ARN of an ElasticSearch destination."""
    return client.create_delivery_stream(
        DeliveryStreamName=stream_name,
        DeliveryStreamType="DirectPut",
        ElasticsearchDestinationConfiguration={
            "RoleARN": f"arn:aws:iam::{ACCOUNT_ID}:role/firehose_delivery_role",
            "DomainARN": "arn:aws:es:::domain/firehose-test",
            "IndexName": "myIndex",
            "TypeName": "UNCOMPRESSED",
            "IndexRotationPeriod": "NoRotation",
            "BufferingHints": {"IntervalInSeconds": 123, "SizeInMBs": 123},
            "RetryOptions": {"DurationInSeconds": 123},
            "S3Configuration": {
                "RoleARN": f"arn:aws:iam::{ACCOUNT_ID}:role/firehose_delivery_role",
                "BucketARN": "arn:aws:s3:::firehose-test",
                "Prefix": "myFolder/",
                "BufferingHints": {"SizeInMBs": 123, "IntervalInSeconds": 124},
                "CompressionFormat": "UNCOMPRESSED",
            },
        },
    )


def create_http_delivery_stream(client, stream_name):
    """Return delivery stream ARN of an Http destination."""
    return client.create_delivery_stream(
        DeliveryStreamName=stream_name,
        DeliveryStreamType="DirectPut",
        HttpEndpointDestinationConfiguration={
            "EndpointConfiguration": {"Url": "google.com"},
            "RetryOptions": {"DurationInSeconds": 100},
            "BufferingHints": {"SizeInMBs": 123, "IntervalInSeconds": 124},
            "CloudWatchLoggingOptions": {"Enabled": False},
            "S3Configuration": {
                "RoleARN": f"arn:aws:iam::{ACCOUNT_ID}:role/firehose_delivery_role",
                "BucketARN": "arn:aws:s3:::firehose-test",
                "Prefix": "myFolder/",
                "BufferingHints": {"SizeInMBs": 123, "IntervalInSeconds": 124},
                "CompressionFormat": "UNCOMPRESSED",
            },
        },
    )


def create_snowflake_delivery_stream(client, stream_name):
    """Return delivery stream ARN of a Snowflake destination."""
    return client.create_delivery_stream(
        DeliveryStreamName=stream_name,
        DeliveryStreamType="DirectPut",
        SnowflakeDestinationConfiguration={
            "RoleARN": f"arn:aws:iam::{ACCOUNT_ID}:role/firehose_delivery_role",
            "AccountUrl": f"fake-account.{TEST_REGION}.snowflakecomputing.com",
            "Database": "myDatabase",
            "Schema": "mySchema",
            "Table": "myTable",
            "S3BackupMode": "FailedDataOnly",
            "S3Configuration": {
                "RoleARN": f"arn:aws:iam::{ACCOUNT_ID}:role/firehose_delivery_role",
                "BucketARN": "arn:aws:s3:::firehose-test",
            },
        },
    )


@mock_aws
def test_create_snowflake_delivery_stream():
    """Verify fields of a Snowflake delivery stream."""
    client = boto3.client("firehose", region_name=TEST_REGION)

    stream_name = f"stream_{mock_random.get_random_hex(6)}"
    response = create_snowflake_delivery_stream(client, stream_name)
    stream_arn = response["DeliveryStreamARN"]

    response = client.describe_delivery_stream(DeliveryStreamName=stream_name)
    stream_description = response["DeliveryStreamDescription"]

    # Sure and Freezegun don't play nicely together
    stream_description.pop("CreateTimestamp")
    stream_description.pop("LastUpdateTimestamp")

    assert stream_description == {
        "DeliveryStreamName": stream_name,
        "DeliveryStreamARN": stream_arn,
        "DeliveryStreamStatus": "ACTIVE",
        "DeliveryStreamType": "DirectPut",
        "Destinations": [
            {
                "DestinationId": "destinationId-000000000001",
                "SnowflakeDestinationDescription": {
                    "AccountUrl": f"fake-account.{TEST_REGION}.snowflakecomputing.com",
                    "Database": "myDatabase",
                    "RoleARN": f"arn:aws:iam::{ACCOUNT_ID}:role/firehose_delivery_role",
                    "S3BackupMode": "FailedDataOnly",
                    "S3DestinationDescription": {
                        "RoleARN": f"arn:aws:iam::{ACCOUNT_ID}:role/firehose_delivery_role",
                        "BucketARN": "arn:aws:s3:::firehose-test",
                    },
                    "Schema": "mySchema",
                    "Table": "myTable",
                },
            },
        ],
        "HasMoreDestinations": False,
        "VersionId": "1",
    }


@mock_aws
def test_create_redshift_delivery_stream():
    """Verify fields of a Redshift delivery stream."""
    client = boto3.client("firehose", region_name=TEST_REGION)

    stream_name = f"stream_{mock_random.get_random_hex(6)}"
    response = create_redshift_delivery_stream(client, stream_name)
    stream_arn = response["DeliveryStreamARN"]

    response = client.describe_delivery_stream(DeliveryStreamName=stream_name)
    stream_description = response["DeliveryStreamDescription"]

    # Sure and Freezegun don't play nicely together
    stream_description.pop("CreateTimestamp")
    stream_description.pop("LastUpdateTimestamp")

    assert stream_description == {
        "DeliveryStreamName": stream_name,
        "DeliveryStreamARN": stream_arn,
        "DeliveryStreamStatus": "ACTIVE",
        "DeliveryStreamType": "DirectPut",
        "VersionId": "1",
        "Destinations": [
            {
                "DestinationId": "destinationId-000000000001",
                "RedshiftDestinationDescription": {
                    "RoleARN": f"arn:aws:iam::{ACCOUNT_ID}:role/firehose_delivery_role",
                    "ClusterJDBCURL": "jdbc:redshift://host.amazonaws.com:5439/database",
                    "CopyCommand": {
                        "DataTableName": "outputTable",
                        "CopyOptions": "CSV DELIMITER ',' NULL '\\0'",
                    },
                    "Username": "username",
                    "S3DestinationDescription": {
                        "RoleARN": f"arn:aws:iam::{ACCOUNT_ID}:role/firehose_delivery_role",
                        "BucketARN": "arn:aws:s3:::firehose-test",
                        "Prefix": "myFolder/",
                        "BufferingHints": {
                            "SizeInMBs": 123,
                            "IntervalInSeconds": 124,
                        },
                        "CompressionFormat": "UNCOMPRESSED",
                    },
                },
            }
        ],
        "HasMoreDestinations": False,
    }


@mock_aws
def test_create_extended_s3_delivery_stream():
    """Verify fields of a S3 delivery stream."""
    client = boto3.client("firehose", region_name=TEST_REGION)

    stream_name = f"stream_{mock_random.get_random_hex(6)}"
    response = create_extended_s3_delivery_stream(client, stream_name)
    stream_arn = response["DeliveryStreamARN"]

    response = client.describe_delivery_stream(DeliveryStreamName=stream_name)
    stream_description = response["DeliveryStreamDescription"]

    # Sure and Freezegun don't play nicely together
    stream_description.pop("CreateTimestamp")
    stream_description.pop("LastUpdateTimestamp")

    assert stream_description == {
        "DeliveryStreamName": stream_name,
        "DeliveryStreamARN": stream_arn,
        "DeliveryStreamStatus": "ACTIVE",
        "DeliveryStreamType": "DirectPut",
        "VersionId": "1",
        "Destinations": [
            {
                "DestinationId": "destinationId-000000000001",
                "ExtendedS3DestinationDescription": {
                    "RoleARN": f"arn:aws:iam::{ACCOUNT_ID}:role/firehose_delivery_role",
                    "BucketARN": "arn:aws:s3:::firehose-test",
                    "Prefix": "myFolder/",
                    "CompressionFormat": "UNCOMPRESSED",
                    "DataFormatConversionConfiguration": {
                        "Enabled": True,
                        "InputFormatConfiguration": {
                            "Deserializer": {"HiveJsonSerDe": {}}
                        },
                        "OutputFormatConfiguration": {
                            "Serializer": {"ParquetSerDe": {"Compression": "SNAPPY"}}
                        },
                        "SchemaConfiguration": {
                            "DatabaseName": stream_name,
                            "RoleARN": f"arn:aws:iam::{ACCOUNT_ID}:role/firehose_delivery_role",
                            "TableName": "outputTable",
                        },
                    },
                },
                "S3DestinationDescription": {
                    "RoleARN": f"arn:aws:iam::{ACCOUNT_ID}:role/firehose_delivery_role",
                    "BucketARN": "arn:aws:s3:::firehose-test",
                    "Prefix": "myFolder/",
                    "CompressionFormat": "UNCOMPRESSED",
                },
            }
        ],
        "HasMoreDestinations": False,
    }


@mock_aws
def test_create_elasticsearch_delivery_stream():
    """Verify fields of an Elasticsearch delivery stream."""
    client = boto3.client("firehose", region_name=TEST_REGION)

    stream_name = f"stream_{mock_random.get_random_hex(6)}"
    response = create_elasticsearch_delivery_stream(client, stream_name)
    stream_arn = response["DeliveryStreamARN"]

    response = client.describe_delivery_stream(DeliveryStreamName=stream_name)
    stream_description = response["DeliveryStreamDescription"]

    # Sure and Freezegun don't play nicely together
    _ = stream_description.pop("CreateTimestamp")
    _ = stream_description.pop("LastUpdateTimestamp")

    assert stream_description == {
        "DeliveryStreamName": stream_name,
        "DeliveryStreamARN": stream_arn,
        "DeliveryStreamStatus": "ACTIVE",
        "DeliveryStreamType": "DirectPut",
        "VersionId": "1",
        "Destinations": [
            {
                "DestinationId": "destinationId-000000000001",
                "ElasticsearchDestinationDescription": {
                    "RoleARN": f"arn:aws:iam::{ACCOUNT_ID}:role/firehose_delivery_role",
                    "DomainARN": "arn:aws:es:::domain/firehose-test",
                    "IndexName": "myIndex",
                    "TypeName": "UNCOMPRESSED",
                    "IndexRotationPeriod": "NoRotation",
                    "BufferingHints": {"IntervalInSeconds": 123, "SizeInMBs": 123},
                    "RetryOptions": {"DurationInSeconds": 123},
                    "S3DestinationDescription": {
                        "RoleARN": f"arn:aws:iam::{ACCOUNT_ID}:role/firehose_delivery_role",
                        "BucketARN": "arn:aws:s3:::firehose-test",
                        "Prefix": "myFolder/",
                        "BufferingHints": {
                            "SizeInMBs": 123,
                            "IntervalInSeconds": 124,
                        },
                        "CompressionFormat": "UNCOMPRESSED",
                    },
                },
            }
        ],
        "HasMoreDestinations": False,
    }


@mock_aws
def test_create_s3_delivery_stream():
    """Verify fields of an S3 delivery stream."""
    client = boto3.client("firehose", region_name=TEST_REGION)

    stream_name = f"stream_{mock_random.get_random_hex(6)}"
    response = client.create_delivery_stream(
        DeliveryStreamName=stream_name,
        S3DestinationConfiguration={
            "RoleARN": f"arn:aws:iam::{ACCOUNT_ID}:role/firehose_delivery_role",
            "BucketARN": "arn:aws:s3:::firehose-test",
            "Prefix": "myFolder/",
            "BufferingHints": {"SizeInMBs": 123, "IntervalInSeconds": 124},
            "CompressionFormat": "UNCOMPRESSED",
        },
    )
    stream_arn = response["DeliveryStreamARN"]

    response = client.describe_delivery_stream(DeliveryStreamName=stream_name)
    stream_description = response["DeliveryStreamDescription"]

    # Sure and Freezegun don't play nicely together
    stream_description.pop("CreateTimestamp")
    stream_description.pop("LastUpdateTimestamp")

    assert stream_description == {
        "DeliveryStreamName": stream_name,
        "DeliveryStreamARN": stream_arn,
        "DeliveryStreamStatus": "ACTIVE",
        "DeliveryStreamType": "DirectPut",
        "VersionId": "1",
        "Destinations": [
            {
                "DestinationId": "destinationId-000000000001",
                "S3DestinationDescription": {
                    "RoleARN": f"arn:aws:iam::{ACCOUNT_ID}:role/firehose_delivery_role",
                    "BucketARN": "arn:aws:s3:::firehose-test",
                    "Prefix": "myFolder/",
                    "BufferingHints": {"SizeInMBs": 123, "IntervalInSeconds": 124},
                    "CompressionFormat": "UNCOMPRESSED",
                },
            }
        ],
        "HasMoreDestinations": False,
    }
