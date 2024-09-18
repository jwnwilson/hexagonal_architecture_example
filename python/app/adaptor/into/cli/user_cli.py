from app.adaptor.out.db.user_sql import SQLAlchemyUserDataAdapter
from app.domain.user_domain import UserEntity, UserCreateDTO


if __name__ == "__main__":
    user_data_adaptor = SQLAlchemyUserDataAdapter()
    new_user = UserCreateDTO(
        name="Noel",
        address="London"
    )
    new_user_record = UserEntity(user_data_adaptor).create_user(
        new_user
    )
    print(f"Created user: {new_user_record}")
