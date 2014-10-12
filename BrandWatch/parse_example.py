from parse_rest.connection import register
from parse_rest.datatypes import Object


APPLICATION_ID = "OXkpE2XPHyUMnVGWZ3iUjAGgnKgUJ7pfVQsPzgD2"
REST_API_KEY = "3jSm0LzdeFzBGKBonGuHmfmPpiMGo3wAjJ9buK5T"
MASTER_KEY = "DGwQhzvyfqIuALuU8KPWicwP9XAV2XWEJojxhTxz"

class Playlist(Object):
    pass

try:
    import settings_local
except ImportError:
    sys.exit('You must create a settings_local.py file with APPLICATION_ID REST_API_KEY, MASTER_KEY variables set')

if __name__ == "__main__":
    print("starting sample application")

    register(app_id=APPLICATION_ID, rest_key=REST_API_KEY, master_key=MASTER_KEY)

    playlist = Playlist(name="TestPlaylist")
    playlist.save()






