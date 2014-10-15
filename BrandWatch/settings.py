# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
# read-only access to the endpoint).
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']

# Enable reads (GET), edits (PATCH), replacements (PUT) and deletes of
# individual items  (defaults to read-only item access).
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

# "_module":"oauth2client.client",
# "token_expiry":"2014-10-15T07:37:58Z",
#    "access_token":"ya29.nwACmYl3h8vtOThaTSJR764gKksZAOsU-pOn5hUL1u-q8RTzVKWno_TG",
#    "token_uri":"https://accounts.google.com/o/oauth2/token",
#    "invalid":false,
#    "token_response":{
#       "access_token":"ya29.nwACmYl3h8vtOThaTSJR764gKksZAOsU-pOn5hUL1u-q8RTzVKWno_TG",
#       "token_type":"Bearer",
#       "expires_in":3599
#    },
#    "client_id":"404415981542-qc8uo8etog9buidhbh5hj8d3j3j87ukv.apps.googleusercontent.com",
#    "id_token":null,
#    "client_secret":"e9HfRTMlIUohJc_tmunCx7-x",
#    "revoke_uri":"https://accounts.google.com/o/oauth2/revoke",
#    "_class":"OAuth2Credentials",
#    "refresh_token":null,
#    "user_agent":null
# }


user_schema = {

    'name': {
        'type': 'string',
    },

    'email': {
        'type': 'string',
    },

    'oauth2_json': {
        'type': 'string',
    },
}

campaign_schema = {
    # Schema definition, based on Cerberus grammar. Check the Cerberus project
    # (https://github.com/nicolaiarocci/cerberus) for details.
    'owner': {
        'type': 'objectid',
        'data_relation': {
            'resource': 'user'
        },
        'required': True,
    },
    'name': {
        'type': 'string',
        'minlength': 4,
        'maxlength': 30,
        'unique': True
    },
    'start_date': {
        'type': 'datetime',
    },
    'end_date': {
        'type': 'datetime',
    },

    'vtr_target': {
        'type': 'float',
        'required': True,
    },
    'ctr_target': {
        'type': 'float',
        'required': True,
    },
    'shares_target': {
        'type': 'float',
        'required': True,
    },
    'tweets_target': {
        'type': 'float',
        'required': True,
    },
    'likes_target': {
        'type': 'float',
        'required': True,
    },
    'comments_target': {
        'type': 'float',
        'required': True,
    },
    'vtr': {
        'type': 'float',
    },
    'ctr': {
        'type': 'float',
    },
    'shares': {
        'type': 'float',
    },
    'tweets': {
        'type': 'float',
    },
    'likes': {
        'type': 'float',
    },
    'comments': {
        'type': 'float',
    },
}

quartile_schema = {
    'campaign': {
        'type': 'objectid',
        'data_relation': {
            'resource': 'campaign'
        },
        'required': True,
    },
    'name': {
        'type': 'string',
    },

    'value': {
        'type': 'integer',
    },

    'start_date': {
        'type': 'datetime',
    },

    'end_date': {
        'type': 'datetime',
    },
}

video_schema = {
    'campaign': {
        'type': 'objectid',
        'data_relation': {
            'resource': 'campaign'
        },
    },
    'name': {
        'type': 'string',
    },

    'description': {
        'type': 'string',
    },

    'embed_url': {
        'type': 'string',
    },

}

quartile = {
    # 'title' tag used in item links. Defaults to the resource title minus
    # the final, plural 's' (works fine in most cases but not for 'people')
    'item_title': 'User',


    # We choose to override global cache-control directives for this resource.
    # 'cache_control': 'max-age=10,must-revalidate',
    # 'cache_expires': 10,

    # most global settings can be overridden at resource level
    # 'resource_methods': ['GET', 'POST'],

    'schema': quartile_schema
}

campaign = {
    # 'title' tag used in item links. Defaults to the resource title minus
    # the final, plural 's' (works fine in most cases but not for 'people')
    'item_title': 'Campaign',


    # We choose to override global cache-control directives for this resource.
    # 'cache_control': 'max-age=10,must-revalidate',
    # 'cache_expires': 10,

    # most global settings can be overridden at resource level
    # 'resource_methods': ['GET', 'POST'],

    'schema': campaign_schema
}

user = {
    # 'title' tag used in item links. Defaults to the resource title minus
    # the final, plural 's' (works fine in most cases but not for 'people')
    'item_title': 'User',


    # We choose to override global cache-control directives for this resource.
    # 'cache_control': 'max-age=10,must-revalidate',
    # 'cache_expires': 10,

    # most global settings can be overridden at resource level
    # 'resource_methods': ['GET', 'POST'],

    'schema': user_schema
}

video = {
    # 'title' tag used in item links. Defaults to the resource title minus
    # the final, plural 's' (works fine in most cases but not for 'people')
    'item_title': 'User',


    # We choose to override global cache-control directives for this resource.
    # 'cache_control': 'max-age=10,must-revalidate',
    # 'cache_expires': 10,

    # most global settings can be overridden at resource level
    # 'resource_methods': ['GET', 'POST'],

    'schema': video_schema
}

DOMAIN = {
    'campaign': campaign,
    'user': user,
    'quartile': quartile,
    'video': video,
}

#database settings for eve

MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_USERNAME = 'test'
MONGO_PASSWORD = 'test'
MONGO_DBNAME = 'apitest'