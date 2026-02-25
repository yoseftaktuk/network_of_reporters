from consumer import get_from_kafka, connect_to_kafka

def main():
    consumer_raw = connect_to_kafka('raw')
    consumer_clean = connect_to_kafka('clean')
    consumer_analytics = connect_to_kafka('analytics')
    while True:
        get_from_kafka([consumer_raw, consumer_clean, consumer_analytics])
if __name__ == "__main__":
    main()        