def image_url(n):
    return '/static/image/login_%02i.jpg' % (n,)

LOGIN_IMAGES = [
    dict(
        image_URL=image_url(1),
        top='37%',
        left='22%',
        color='#3998C2',
        ),
    dict(
        image_URL=image_url(2),
        top='19%',
        left='52%',
        color='#C7AA9C',
        ),
    dict(
        image_URL=image_url(3),
        top='38%',
        left='52%',
        color='#6A8CA9',
        ),
    dict(
        image_URL=image_url(4),
        top='40%',
        left='52%',
        color='#E8711F',
        ),
    dict(
        image_URL=image_url(5),
        top='20%',
        left='48%',
        color='#C7452E',
        ),
    dict(
        image_URL=image_url(6),
        top='15%',
        left='45%',
        color='#7B4730',
        ),
    ]

