from utils import CleaningService
from cunsomer import get_from_kafka

def main():
    clean = CleaningService()
    get_from_kafka('raw', 'words', clean.clean_all)

if __name__ == "__main__":
    main()   