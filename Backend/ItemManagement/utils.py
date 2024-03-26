from django.db.models import Model
from exceptions import InvalidItemStringException

ITEM_MODEL_STRING_TO_ITEM_MODEL: dict = {
    "Blazer": BlazerItemModel
}


def get_item_model(item_model_string: str) -> Model:
    try:
        return ITEM_MODEL_STRING_TO_ITEM_MODEL[item_model_string]
    except InvalidItemStringException as exception:
        raise exception
