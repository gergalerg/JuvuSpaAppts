

def norm_query_dict(post):
    '''
    Return a real dict from a Django QueryDict thing.
    '''
    return dict((k, post.get(k)) for k in post)
