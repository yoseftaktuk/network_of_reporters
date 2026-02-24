from consumer import get_from_kafka

def main():
    while True:
        get_from_kafka('raw')
        get_from_kafka('clean')
        get_from_kafka('analytics')


if __name__ == "__main__":
    main()        