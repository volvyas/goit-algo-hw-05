import timeit
from typing import Final

from boyer_moore_search import boyer_moore_search
from kmp_search import kmp_search
from rabin_karp_search import rabin_karp_search

NUM_TESTS: Final = 200
POSITIVE_SEARCH_STRING: Final = "систем"
NEGATIVE_SEARCH_STRING: Final = "абракадабра"

def get_text(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        return file.read()


article_1 = get_text("Article1.txt")
article_2 = get_text("Article2.txt")

def perform_test(search_algo: str, text_name: str, is_positive: bool):
    pattern = "POSITIVE" if is_positive else "NEGATIVE"
    call_str = search_algo + "(" +text_name+ "," + pattern + "_SEARCH_STRING)" 
    result = timeit.timeit(call_str, number=NUM_TESTS, globals=globals())
    print(f"|   {text_name}   |  {pattern.lower()}  |   {result:.3f}  |")

print("Results for KMP Search:")
print("|  Text Source  |  Scenario  |  Result  |")

perform_test('kmp_search', 'article_1', is_positive=True)
perform_test('kmp_search', 'article_2', is_positive=True)
perform_test('kmp_search', 'article_1', is_positive=False)
perform_test('kmp_search', 'article_2', is_positive=False)
             
print("\n\nResults for Boyer-Moore Search:")
print("|  Text Source  |  Scenario  |  Result  |")             
perform_test('boyer_moore_search', 'article_1', is_positive=True)
perform_test('boyer_moore_search', 'article_2', is_positive=True)
perform_test('boyer_moore_search', 'article_1', is_positive=False)
perform_test('boyer_moore_search', 'article_2', is_positive=False)

print("\n\nResults for Rabin-Karp Search:")
print("|  Text Source  |  Scenario  |  Result  |")    

perform_test('rabin_karp_search', 'article_1', is_positive=True)
perform_test('rabin_karp_search', 'article_2', is_positive=True)
perform_test('rabin_karp_search', 'article_1', is_positive=False)
perform_test('rabin_karp_search', 'article_2', is_positive=False)


