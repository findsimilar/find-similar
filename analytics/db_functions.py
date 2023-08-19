from find_similar.calc_functions import calc_cosine_similarity_opt
from database.db_functions import get_base_token_by_id

# RATING_STEPS = [(1, 0), (5, 1), (10, 2), (25, 3), (50, 4), (100, 5), (500, 6), (1000, 7), (2000, 8)]
RATING_STEPS = [1, 5, 10, 25, 50, 100, 200, 300, 400]


def get_report_proximity(base_list, ratings_total: list, output=print, edge=50):
    """
    Формирование отчёта совпадений в процентном соотношении.
    :param base_list:
    :param edge:
    :param output:
    :param ratings_total:
    :return:
    """
    ratings_total_sorted = sorted(ratings_total, key=lambda item: item.rating, reverse=False)
    output(f'Рейтинг {edge} и более:')
    for rating in ratings_total_sorted:

        total_rating = rating.rating
        search_word = rating.request
        founded_word = rating.best_find

        if total_rating > edge:
            output(f'искали: {search_word.text}')
            output(f'нашли (рейтинг {total_rating}): {founded_word.text}')

            base_name = get_base_token_by_id(base_list, search_word.id_base_item)
            output(f'должно быть: {base_name.text}')

            output('Analytics: ')
            output(f'{search_word.text}///{base_name.text}')
            output(search_word.text)
            output(base_name.text)
            output(str(search_word.tokens))
            output(str(base_name.tokens))
            cos = calc_cosine_similarity_opt(search_word.tokens, base_name.tokens)
            output(f'COS: {cos}')
            output(f'-----')