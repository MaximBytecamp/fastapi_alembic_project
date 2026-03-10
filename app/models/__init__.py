from sqlmodel import SQLModel
from app.models.membership import Membership  # noqa: F401  
from app.models.user import User  # noqa: F401
from app.models.project import Project  # noqa: F401


NAMING_CONVENTION: dict[str, str] = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}

SQLModel.metadata.naming_convention = NAMING_CONVENTION