"""
Functions to analyze main algorithm proximity
"""
from timeit import Timer
from analytics.models import ReportUnit
from find_similar import find_similar
from find_similar.calc_functions import TokenText
from find_similar.tokenize import tokenize
from lab.settings import TOP_ELEMENT


RATING_STEPS = [0, 1, 5, 10, 25, 50, 100, 200, 300, 400]


def check_item_rating(
    item_to_check: TokenText, base_items_tokens: list[TokenText], dictionary=None
) -> int:
    """
    Определение позиции int ожидаемого наименования
    среди отсортированного списка найденных наименований.
    """
    rating_cos_sort = get_item_find_list(
        item_to_check, base_items_tokens, dictionary=dictionary
    )
    rating = rating_cos_sort.index(item_to_check) + 1
    return rating


def get_item_find_list(
    item_to_check: TokenText, items_tokens_pile: list[TokenText], dictionary=None, keywords=None
) -> list[TokenText]:
    """
    Возвращает список найденных базовых наименований TokenText,
    отсортированный по убыванию вероятности совпадения.
    """
    rating_cos_sort = find_similar(
        item_to_check, items_tokens_pile, count=-1, dictionary=dictionary, keywords=keywords
    )
    return rating_cos_sort


def check_time(number_count, base_items_tokens: list[TokenText], dictionary=None):
    """
    find_similar function execute time
    """
    timer = Timer(
        lambda: find_similar("какой то новый товар", base_items_tokens, dictionary)
    )
    return timer.timeit(number=number_count)


def check_ratings_total(
    items_pile_to_check: list[TokenText], items_pile: list[TokenText], dictionary=None
) -> list:
    """
    Возвращает список всех найденных позиций.
    """
    ratings_total = []
    for item_to_check in items_pile_to_check:
        rating_cos_sort = get_item_find_list(item_to_check, items_pile, dictionary)
        try:
            rating = rating_cos_sort.index(item_to_check) + 1
        except ValueError:
            rating = 0
        # [то что искали, то что нашли, рейтинг]
        ratings_total.append(
            ReportUnit(item_to_check, rating_cos_sort[TOP_ELEMENT], rating)
        )
    return ratings_total


def get_report_total(ratings_total: list, output=print):
    """
    Формирование отчёта совпадений в процентном соотношении.
    :param output:
    :param ratings_total:
    :return:
    """
    report_total = []
    for _ in range(len(RATING_STEPS)):
        report_total.append(0)
    for rating in ratings_total:
        prev_rating_step = 0
        for rating_step in RATING_STEPS:
            if rating.rating in range(prev_rating_step, rating_step + 1):
                slot = RATING_STEPS.index(rating_step)
                report_total[slot] = report_total[slot] + 1
            prev_rating_step = rating_step + 1
    total_count = len(ratings_total)
    output(f"Поиск выполнен для {total_count} позиций:")
    count_acc = 0
    count_percent_acc = 0
    for rating_step in RATING_STEPS:
        count = report_total[RATING_STEPS.index(rating_step)]
        count_percent = count / total_count * 100
        if rating_step == 0:
            output(
                f"*вероятность совпадения не определена для {count} ({round(count_percent, 2)} %) "
            )
            total_count = total_count - count
        else:
            if count > 0:
                count_acc = count_acc + count
                count_percent_acc = count_percent_acc + count_percent
                output(
                    f"топ {rating_step} -- {count_acc} ({round(count_percent_acc, 2)} %) "
                    f"-- {count} ({round(count_percent, 2)} %)"
                )


def analyze_one_item(item, dictionary=None, language="russian"):
    """
    Analyze one item for tokenize
    """
    tokens = tokenize(item, language=language, dictionary=dictionary)
    return tokens
