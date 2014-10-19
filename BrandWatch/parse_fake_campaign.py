from datetime import datetime, timedelta
from parse_rest.connection import register
from parse_rest.datatypes import Object


APPLICATION_ID = "OXkpE2XPHyUMnVGWZ3iUjAGgnKgUJ7pfVQsPzgD2"
REST_API_KEY = "3jSm0LzdeFzBGKBonGuHmfmPpiMGo3wAjJ9buK5T"
MASTER_KEY = "DGwQhzvyfqIuALuU8KPWicwP9XAV2XWEJojxhTxz"

class Campaign(Object):
    pass

try:
    import settings_local
except ImportError:
    sys.exit('You must create a settings_local.py file with APPLICATION_ID REST_API_KEY, MASTER_KEY variables set')

if __name__ == "__main__":
    print("starting campaign fake data")

    register(app_id=APPLICATION_ID, rest_key=REST_API_KEY, master_key=MASTER_KEY)

    now = datetime.now()
    one_day_ago = (now - timedelta(days=1))
    one_week_ago = (now - timedelta(days=7))

    campaign = Campaign()
    campaign.name = "Tweedy Campaign"
    campaign.user_id = "user232"
    campaign.start = one_week_ago
    campaign.end = one_day_ago
    campaign.score = 85
    campaign.vtr_target = 90.1
    campaign.ctr_target = 0.5
    campaign.shares_target = 400
    campaign.favorites_target = 100
    campaign.likes_target = 100
    campaign.comments_target = 50
    campaign.video_ids = ['2', '4', '7']
    campaign.save()

    campaign = Campaign()
    campaign.name = "Tweedy Campaign Live"
    campaign.user_id = "user232"
    campaign.start = one_week_ago
    campaign.end = one_day_ago
    campaign.score = 95
    campaign.vtr_target = 90.1
    campaign.ctr_target = 0.5
    campaign.shares_target = 400
    campaign.favorites_target = 100
    campaign.likes_target = 100
    campaign.comments_target = 50
    campaign.video_ids = ['2', '4', '7']

    campaign.save()
