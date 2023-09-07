from analytics.models import ReportUnit
from find_similar import find_similar
from find_similar.calc_functions import TokenText
from find_similar.tokenize import tokenize
from lab.settings import TOP_ELEMENT

# RATING_STEPS = [(1, 0), (5, 1), (10, 2), (25, 3), (50, 4), (100, 5), (500, 6), (1000, 7), (2000, 8)]
RATING_STEPS = [1, 5, 10, 25, 50, 100, 200, 300, 400]


def check_item_rating(item_to_check: TokenText, base_items_tokens: list[TokenText], dictionary=None) -> int:
    """
    Определение позиции int ожидаемого наименования среди отсортированного списка найденных наименований.
    """
    rating_cos_sort = get_item_find_list(item_to_check, base_items_tokens, dictionary=dictionary)
    rating = rating_cos_sort.index(item_to_check) + 1
    return rating


def get_item_find_list(item_to_check: TokenText, base_items_tokens: list[TokenText], dictionary=None) -> list[TokenText]:
    """
    Возвращает список найденных базовых наименований TokenText, отсортированный по убыванию вероятности совпадения.
    """
    rating_cos_sort = find_similar(item_to_check, base_items_tokens, count=-1, dictionary=dictionary)
    return rating_cos_sort


def check_time(number_count, base_items_tokens: list[TokenText], dictionary=None):
    from timeit import Timer
    t = Timer(lambda: find_similar('какой то новый товар', base_items_tokens, dictionary))
    return t.timeit(number=number_count)


def check_ratings_total(base_items_tokens: list[TokenText], analog_items: list[TokenText], dictionary=None) -> list:
    """
    Возвращает список всех найденных позиций.
    """
    ratings_total = []
    for analog_item in analog_items:
        rating_cos_sort = get_item_find_list(analog_item, base_items_tokens, dictionary)
        rating = rating_cos_sort.index(analog_item) + 1
        # [то что искали, то что нашли, рейтинг]
        # ratings_total.append([analog_item, rating_cos_sort[TOP_ELEMENT], rating])
        ratings_total.append(ReportUnit(analog_item, rating_cos_sort[TOP_ELEMENT], rating))
    return ratings_total


def get_report_total(ratings_total: list, output=print):
    """
    Формирование отчёта совпадений в процентном соотношении.
    :param output:
    :param ratings_total:
    :return:
    """
    report_total = []
    for i in range(len(RATING_STEPS)):
        report_total.append(0)
    for rating in ratings_total:
        for rating_step in RATING_STEPS:
            if rating.rating in range(0, rating_step + 1):
                slot = RATING_STEPS.index(rating_step)
                report_total[slot] = report_total[slot] + 1
    total_count = len(ratings_total)
    output(f'Поиск выполнен для {total_count} позиций:')
    c = 0
    t = 0
    for rating_step in RATING_STEPS:
        count_acc = report_total[RATING_STEPS.index(rating_step)]
        count = count_acc - t
        count_percent_acc = count_acc / total_count * 100
        count_percent = (count_percent_acc - c)
        output(f'топ {rating_step} -- {count_acc} ({round(count_percent_acc, 2)} %) -- {count} ({round(count_percent, 2)} %)')
        c = count_percent_acc
        t = count_acc


def analyze_one_item(item, dictionary=None, language='russian'):
    print(item)
    tokens = tokenize(item, language=language, dictionary=dictionary)
    print(tokens)
    return tokens
