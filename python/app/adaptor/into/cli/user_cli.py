from app.adaptor.out.user_data.user_sql import SQLUserDataAdapter
from app.domain.user_domain import UserEntity, UserCreateDTO


if __name__ == "__main__":
    user_data_adaptor = SQLUserDataAdapter()
    new_user = UserCreateDTO(
        name="Noel",
        address="London"
    )
    new_user_record = UserEntity(user_data_adaptor).create_user(
        new_user
    )
    print(f"Created user: {new_user_record}")
