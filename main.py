import fb
import os
from dotenv import load_dotenv

load_dotenv()
facebook = fb.Facebook(
    facebook_login = str(os.getenv('USERNAME')),
    facebook_password = str(os.getenv('PASSWORD')),
    refresh_time = int(os.getenv('REFRESH_TIME'))
)
facebook.run()