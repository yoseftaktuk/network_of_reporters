from logic import AnalyticsService
from consumer import get_from_kafka


analytics = AnalyticsService()
def main():
    get_from_kafka('clean', analytics.do_all)

if __name__ == "__main__":
    main()    