from DEVILMUSIC.core.bot import DEVIL
from DEVILMUSIC.core.dir import dirr
from DEVILMUSIC.core.git import git
from DEVILMUSIC.core.userbot import Userbot
from DEVILMUSIC.misc import dbb, heroku

from SafoneAPI import SafoneAPI
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = DEVIL()
api = SafoneAPI()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()