import boto3


def main():
    client = boto3.client(
        'sqs',
        endpoint_url='http://elasticmq:9324',
        region_name="ap-northeast-1"
    )
    response = client.receive_message(
        QueueUrl="http://elasticmq:9324/000000000000/queue1")
    
    print(response)


if __name__ == "__main__":
    main()
