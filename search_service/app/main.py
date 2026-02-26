from elastic_query import ElastikQueryService
import time
test = ElastikQueryService()


if __name__ == "__main__":
    while True:
        data = test.get_wepons()
        test.streamlit_get_wepons(data)
        data = test.get_most_common_words()
        test.streamlit_get_common_words(data)
        time.sleep(10)