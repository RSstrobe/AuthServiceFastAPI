"""add_actions

Revision ID: 390888ecf4d3
Revises: 95a57ddc7868
Create Date: 2024-02-25 01:48:49.976652

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from models.auth_orm_models import ActionsOrm


# revision identifiers, used by Alembic.
revision: str = "390888ecf4d3"
down_revision: Union[str, None] = "95a57ddc7868"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.bulk_insert(
        table=ActionsOrm.__table__,
        rows=[
            {
                "id": "bb29bca0-a549-4aa7-b75e-39d4ebf648a9",
                "action_name": "logout",
                "comment": "Разлогинивание пользователя",
            },
            {
                "id": "d4159fcc-6d65-4281-8303-c2c9cf969a6a",
                "action_name": "refresh_token",
                "comment": "Обновить пару токенов",
            },
            {
                "id": "6571b7fc-c0b7-42a6-bd86-f673649d074f",
                "action_name": "history",
                "comment": "Получить историю авторизации",
            },
            {
                "id": "b9702cdc-a388-4e3c-9176-5da40facc429",
                "action_name": "change_password",
                "comment": "Изменить пароль",
            },
            {
                "id": "50c54f3c-2be3-4f0e-a9da-10089e668ac9",
                "action_name": "create_role",
                "comment": "Создать роль",
            },
            {
                "id": "150c2c89-bc20-4eca-8f1e-1a2c9fef2d65",
                "action_name": "delete_role",
                "comment": "Удалить роль",
            },
            {
                "id": "4705bbf9-ddf8-411d-970f-a5fe56911863",
                "action_name": "change_role",
                "comment": "Изменить роль",
            },
            {
                "id": "e03273a9-004c-47e8-9899-a07df741bcf9",
                "action_name": "get_roles",
                "comment": "Просмотр всех ролей",
            },
            {
                "id": "73d169ee-59f5-44b2-8e5d-85dc8fd20bb4",
                "action_name": "set_role",
                "comment": "Назначить роль",
            },
            {
                "id": "4270b104-38c2-4591-a49b-e5663a970d99",
                "action_name": "grab_role",
                "comment": "Отобрать роль",
            },
            {
                "id": "9e626c81-1dfd-43d5-87d5-26a35b748e95",
                "action_name": "check_role",
                "comment": "Проверка роли у пользователя",
            },
            {
                "id": "ccd53c23-f3ea-494b-bc28-248cb8586835",
                "action_name": "films_by_similar_genre",
                "comment": "Поиск кинопроизведений по схожести жанра",
            },
            {
                "id": "e2763c8a-ae85-4414-8ca9-858f91d826a1",
                "action_name": "film_details",
                "comment": "Поиск кинопроизведения по id",
            },
            {
                "id": "d87d3e4e-830a-4376-a49b-402de653435b",
                "action_name": "persons_list",
                "comment": "Получить информацию о персоне",
            },
            {
                "id": "c44cc2b3-5ae6-4013-98b2-966652720207",
                "action_name": "search_persons",
                "comment": "Поиск по персоне",
            },
            {
                "id": "3f2124b0-858e-41a6-a8a9-cae36192b945",
                "action_name": "films_by_person",
                "comment": "Получение списка фильмов персоны",
            },
            {
                "id": "cc96fc52-0077-403d-9810-b34db300a855",
                "action_name": "verify_role",
                "comment": "Верифицировать роль пользователя",
            },
            {
                "id": "8f02e288-62db-4499-8457-e8aeb12cadef",
                "action_name": "update_role",
                "comment": "Верифицировать роль пользователя",
            },
        ],
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute(
        sa.text("DELETE FROM actions r where r.id in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10);")
    )
    # ### end Alembic commands ###