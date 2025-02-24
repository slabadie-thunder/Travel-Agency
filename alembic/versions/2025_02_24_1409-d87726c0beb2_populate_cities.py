"""populate_cities

Revision ID: d87726c0beb2
Revises: e55a8dcabdc0
Create Date: 2025-02-24 14:09:26.323006

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import uuid


# revision identifiers, used by Alembic.
revision: str = 'd87726c0beb2'
down_revision: Union[str, None] = 'e55a8dcabdc0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Create table objects for bulk insert
    cities_table = sa.Table(
        "cities",
        sa.MetaData(),
        autoload_with=op.get_bind()
    )

    # Insert initial data into cities
    op.bulk_insert(
        cities_table,
        [
            { "id": str(uuid.uuid4()), "name": "Montevideo" },
            { "id": str(uuid.uuid4()), "name": "Canelones" },
            { "id": str(uuid.uuid4()), "name": "Rocha" },
        ]
    )


def downgrade() -> None:
    #Delete table
    op.drop_table("cities")
