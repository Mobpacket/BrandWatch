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
    today = now.strftime("%Y-%m-%d")
    one_day_ago = (now - timedelta(days=1)).strftime("%Y-%m-%d")
    one_week_ago = (now - timedelta(days=7)).strftime("%Y-%m-%d")

    campaign = Campaign()
    campaign.name = "Tweedy Campaign"
    campaign.user_id = "brandwatch123@gmail.com"
    campaign.start = "2014-10-12"
    campaign.end = "2014-10-30"
    campaign.score = 85
    campaign.vtr_target = 90.1
    campaign.ctr_target = 0.5
    campaign.shares_target = 400
    campaign.favorites_target = 100
    campaign.likes_target = 100
    campaign.comments_target = 50
    campaign.views_target = 150
    campaign.video_ids = ["C4ss_bScVTc"]
    campaign.save()

    campaign = Campaign()
    campaign.name = "Tweedy Campaign Live"
    campaign.user_id = "brandwatch123@gmail.com"
    campaign.start = "2014-10-12"
    campaign.end = "2014-10-30"
    campaign.score = 95
    campaign.vtr_target = 90.1
    campaign.ctr_target = 0.5
    campaign.shares_target = 400
    campaign.favorites_target = 100
    campaign.likes_target = 100
    campaign.comments_target = 50
    campaign.views_target = 150
    campaign.video_ids = ["-XY9DbQc_9c"]
    campaign.save()

    campaign = Campaign()
    campaign.name = "Apple - Will Ferrell"
    campaign.user_id = "brandwatch123@gmail.com"
    campaign.start = "2014-10-12"
    campaign.end = "2014-10-30"
    campaign.score = 98
    campaign.vtr_target = 95.1
    campaign.ctr_target = 0.7
    campaign.shares_target = 400
    campaign.favorites_target = 100
    campaign.likes_target = 100
    campaign.comments_target = 50
    campaign.views_target = 150
    campaign.video_ids = ["4ar6S_D_keM"]

    campaign.save()
