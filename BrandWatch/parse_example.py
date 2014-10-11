from parse_rest.connection import register
from parse_rest.datatypes import Object


class Playlist(Object):
    pass

try:
    import settings_local
except ImportError:
    sys.exit('You must create a settings_local.py file with APPLICATION_ID REST_API_KEY, MASTER_KEY variables set')

if __name__ == "__main__":
    print("starting sample application")

    register(
        getattr(settings_local, 'APPLICATION_ID'),
        getattr(settings_local, 'REST_API_KEY'),
        master_key=getattr(settings_local, 'MASTER_KEY')
    )

    playlist = Playlist(name="TestPlaylist")
    playlist.save()






