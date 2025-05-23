from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    ForeignKey,
    UUID,
    func,
    DateTime,
)
from app.core.settings import settings
from sqlalchemy.orm import relationship
from app.core.database import Base, engine
import uuid
from enum import Enum
from sqlalchemy import Enum as SQLAlchemyEnum


class UserRole(str, Enum):
    ADMIN = "admin"
    STAFF = "staff"
    CUSTOMER = "customer"


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    uuid = Column(UUID(as_uuid=True), default=uuid.uuid4, index=True)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    email = Column(String, unique=True, index=True, nullable=False)
    role = Column(SQLAlchemyEnum(UserRole), nullable=False, default=UserRole.CUSTOMER)
    avatar_url = Column(String, nullable=True)
    hashed_password = Column(String, nullable=True)  # Store hashed password
    created_at = Column(DateTime, server_default=func.now())  # Auto-set on insert
    updated_at = Column(
        DateTime, server_default=func.now(), onupdate=func.now()
    )  # Auto-update on changes