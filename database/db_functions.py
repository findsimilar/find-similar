"""
Functions to work with db data
"""
import logging

from sqlalchemy.orm import joinedload

from find_similar.calc_functions import get_tokens, TokenText
from find_similar.calc_models import Item
from .db_main import get_session, engine
from .db_models import (
    Base,
    BaseItem,
    AnalogItem,
    BaseItemsTokens,
    AnalogItemsTokens,
    Shop,
)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


def get_all_base_items() -> list[Item]:
    """
    Get all base items
    """
    session = get_session()
    base_items = session.query(BaseItem).options(joinedload(BaseItem.tokens)).all()
    base_items_list = []
    for base_item in base_items:
        item = Item(
            id=base_item.special_id,
            label=base_item.label_text,
            part_number=base_item.part_number,
            id_shop=0,
            token_set=construct_token_set(base_item.tokens),
        )
        base_items_list.append(item)
    return base_items_list


def get_all_analog_items(id_shop=None) -> list[Item]:
    """
    Get all analog items
    """
    session = get_session()
    if id_shop:
        analog_items = (
            session.query(AnalogItem)
            .filter_by(id_shop=id_shop)
            .options(joinedload(AnalogItem.tokens))
            .all()
        )
    else:
        analog_items = (
            session.query(AnalogItem).options(joinedload(AnalogItem.tokens)).all()
        )
    analog_items_list = []
    for analog_item in analog_items:
        item = Item(
            id=analog_item.id,
            label=analog_item.label_text,
            part_number=analog_item.part_number,
            id_shop=analog_item.id_shop,
            id_base_item=analog_item.id_base_item,
            token_set=construct_token_set(analog_item.tokens),
        )
        analog_items_list.append(item)
    return analog_items_list


def create_all():
    """
    Clear all db data
    """
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


def construct_token_set(base_tokens: BaseItemsTokens) -> set:
    """
    Конструирует токен сет для одного наименования.
    :param base_tokens:
    :return:
    """
    result_set = set()
    for base_token in base_tokens:
        result_set.add(base_token.token)
    return result_set


def insert_item_bulk(items_list: list) -> int:
    """
    Вставляет в базу исходные наименования через bulk
    :param items_list:
    :return:
    """
    session = get_session()
    session.expire_on_commit = False
    try:
        session.bulk_save_objects(items_list)
        session.commit()
    # TODO: catch more concrete exception
    except Exception as ex:  # pylint: disable=broad-exception-caught
        logger.error("{ex.__class__.__name__}: %s", str(ex))
        session.rollback()


def generate_base_tokens(dictionary=None):
    """
    Generate base tokens to db items for optimization
    """
    session = get_session()
    session.expire_on_commit = False
    items = get_all_base_items()
    items_tokens = []
    for item in items:
        tokens = get_tokens(item.label, dictionary=dictionary)
        for token in tokens:
            token_add = BaseItemsTokens()
            token_add.token = token
            token_add.id_item = item.id
            items_tokens.append(token_add)
    try:
        session.bulk_save_objects(items_tokens)
        session.commit()
    # TODO: catch more concrete exception
    except Exception as ex:  # pylint: disable=broad-exception-caught
        logger.error("{ex.__class__.__name__}: %s", str(ex))
        session.rollback()


def generate_analog_tokens(dictionary=None):
    """
    Generate tokens for analog items for optimization
    """
    session = get_session()
    session.expire_on_commit = False
    items = get_all_analog_items()
    items_tokens = []
    for item in items:
        tokens = get_tokens(item.label, dictionary=dictionary)
        for token in tokens:
            token_add = AnalogItemsTokens()
            token_add.token = token
            token_add.id_item = item.id
            items_tokens.append(token_add)
    try:
        session.bulk_save_objects(items_tokens)
        session.commit()
    # TODO: catch more concrete exception
    except Exception as ex:  # pylint: disable=broad-exception-caught
        logger.error("{ex.__class__.__name__}: %s", str(ex))
        session.rollback()


def generate_tokens(dictionary=None):
    """
    Generate tokens to all db items
    """
    generate_base_tokens(dictionary)
    generate_analog_tokens(dictionary)


def get_all_base_tokens(base_list, dictionary=None) -> list[TokenText]:
    """
    Get all base tokens from db
    """
    tokens = []
    for base in base_list:
        token = TokenText(base.label, tokens=base.token_set, dictionary=dictionary)
        token.id = base.id
        token.id_base_item = base.id
        tokens.append(token)
    return tokens


def get_all_analog_tokens(id_shop=None, dictionary=None) -> list[TokenText]:
    """
    Get all analog tokens from db
    """
    item_list = get_all_analog_items(id_shop)
    tokens = []
    for item in item_list:
        token = TokenText(item.label, tokens=item.token_set, dictionary=dictionary)
        token.id = item.id
        token.id_base_item = item.id_base_item
        tokens.append(token)
    return tokens


def get_analog_token_by_name(
    name: str, id_shop: int, dictionary=None
) -> list[TokenText]:
    """
    Get analog tokens from db by id
    """
    token_list = get_all_analog_tokens(id_shop, dictionary)
    tokens = []
    for token in token_list:
        if token.text == name:
            tokens.append(token)
    return tokens


def get_base_token_by_id(base_list, base_item_id: int, dictionary=None) -> TokenText:
    """
    Get base tokens from db by id
    """
    token = None
    for base in base_list:
        if base.id == base_item_id:
            token = TokenText(base.label, tokens=base.token_set, dictionary=dictionary)
            token.id = base.id
    return token


def insert_shop(shop_name: str) -> int:
    """
    Add new shop item to database
    """
    session = get_session()
    session.expire_on_commit = False
    shop_exists = session.query(Shop).filter_by(shop_name=shop_name).one_or_none()
    if shop_exists:
        return shop_exists.id
    new_shop = Shop()
    new_shop.shop_name = shop_name
    try:
        session.add(new_shop)
        session.commit()
    # TODO: catch more concrete exception
    except Exception as ex:  # pylint: disable=broad-exception-caught
        logger.error("{ex.__class__.__name__}: %s", str(ex))
        session.rollback()
    return new_shop.id
