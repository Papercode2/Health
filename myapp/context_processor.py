# context_processors.py
def user_info(request):
    user_info = {}
    if request.user.is_authenticated:
        user_info['user_display_name'] = request.user.userprofile.display_name if hasattr(request.user, 'userprofile') else request.user.username
    return user_info
