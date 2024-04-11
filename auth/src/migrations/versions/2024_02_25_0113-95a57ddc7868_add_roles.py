"""add_roles

Revision ID: 95a57ddc7868
Revises: 0357d953e8b5
Create Date: 2024-02-25 01:13:43.896307

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from models.auth_orm_models import RolesOrm

# revision identifiers, used by Alembic.
revision: str = "95a57ddc7868"
down_revision: Union[str, None] = "0357d953e8b5"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.bulk_insert(
        table=RolesOrm.__table__,
        rows=[
            {
                "id": "d91454c4-a706-4d88-8b94-e843ff5021cb",
                "role_name": "DefaultUser",
                "comment": "Actions with movies",
            },
            {
                "id": "25c245c4-1a06-42c7-bb55-0261a2f743d6",
                "role_name": "Admin",
                "comment": "Actions with movies, roles, users",
            },
        ],
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute(sa.text("DELETE FROM roles r where r.id in (1, 2);"))
    # ### end Alembic commands ###
