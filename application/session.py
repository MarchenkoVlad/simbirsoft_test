def get_session_key(request):
    session_key = request.session.session_key
    return session_key


def save_session(request):
    if not request.session or not request.session.session_key:
        request.session.save()
