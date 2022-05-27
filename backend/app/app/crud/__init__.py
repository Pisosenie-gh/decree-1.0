from .crud_item import item
from .crud_user import user
from .crud_eds_provider_type import eds_provider_type
from .crud_signature_resolution import signature_resolution
from .crud_decree_change_action import decree_change_action
from .crud_signature_type import signature_type
from .crud_decree_kind import decree_kind
from .crud_counter import counter
from .crud_decree_type import decree_type
from .crud_decree import decree
from .crud_signature import signature
# For a new basic set of CRUD operations you could just do

# from .base import CRUDBase
# from app.models.item import Item
# from app.schemas.item import ItemCreate, ItemUpdate

# item = CRUDBase[Item, ItemCreate, ItemUpdate](Item)
