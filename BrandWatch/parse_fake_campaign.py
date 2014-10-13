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

    campaign = Campaign()
    campaign.name = "Tweedy Campaign"
    campaign.quartile25Count = 5
    campaign.quartile50Count = 7
    campaign.quartile75Count = 23
    campaign.quartile100Count = 200
    campaign.score = 85
    campaign.vtr = 85.3
    campaign.ctr = 0.2
    campaign.shares = 40
    campaign.tweets = 20
    campaign.likes = 10
    campaign.comments = 5
    campaign.save()

    campaign = Campaign()
    campaign.name = "Tweedy Campaign Live"
    campaign.quartile25Count = 0
    campaign.quartile50Count = 10
    campaign.quartile75Count = 10
    campaign.quartile100Count = 300
    campaign.score = 95
    campaign.vtr = 94.9
    campaign.ctr = 0.3
    campaign.shares = 1205
    campaign.tweets = 200
    campaign.likes = 1000
    campaign.comments = 50
    campaign.save()
