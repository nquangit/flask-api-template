from google.auth.transport import requests
from google.oauth2 import id_token
from models.user import User
from extensions.ext_database import db
from libs.passport import PassportService
from datetime import datetime, timedelta, timezone
from configs import app_config
from models.user import User


class AccountService:

    @staticmethod
    def authenticate_with_google(token, remote_ip):
        try:
            import urllib.parse

            token = urllib.parse.unquote(token)
            # Xác minh token với Google
            id_info = id_token.verify_oauth2_token(
                token, requests.Request()
            )

            # Check Audience
            if id_info["aud"] not in app_config.GOOGLE_CLIENT_IDS:
                raise ValueError("Could not verify the audience.")

            # Lấy thông tin người dùng từ token
            google_id = id_info.get("sub")
            email = id_info.get("email")
            name = id_info.get("name")
            picture = id_info.get("picture")

            # Tìm hoặc tạo người dùng trong database
            user = User.query.filter_by(google_id=google_id).first()
            if not user:
                user = User(
                    google_id=google_id,
                    email=email,
                    name=name,
                    picture=picture,
                    last_login_ip=remote_ip,
                )
                db.session.add(user)
                db.session.commit()

            token = AccountService.get_account_jwt_token(user)

            return {
                "token": token,
            }
        except ValueError:
            return None

    @staticmethod
    def get_account_jwt_token(
        user: User, *, exp: timedelta = timedelta(days=30)
    ) -> str:
        payload = {
            "user_id": user.id,
            "exp": datetime.now(timezone.utc).replace(tzinfo=None) + exp,
            "iss": app_config.EDITION,
            "sub": "User Account Token",
        }

        token = PassportService().issue(payload)
        return token

    @staticmethod
    def load_user_account(*, account_id) -> None | User:
        user = User.query.filter_by(id=account_id).first()
        if not user:
            return None

        return user