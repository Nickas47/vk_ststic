from django.shortcuts import render
from .vk import MyVk
import vk

def index(request):
    return render(request, 'vkapp/index.html')


def result(request):
    user_id = request.POST['user_id']

    session = vk.AuthSession(app_id=MyVk.appId, user_login=MyVk.login, user_password=MyVk.password)
    vkapi = vk.API(session)
    groups = vkapi.groups.get(user_id=user_id, extended=1)
    friends = vkapi.friends.get(user_id=user_id, fields=['name', 'photo_100'])
    profile = vkapi.users.get(user_id=user_id, fields=['occupation','counters','photo_400_orig', 'name', 'sex', 'followers_count', 'bdate', 'home_town', 'status'])
    context = {'profile': profile, 'all_groups': groups, 'friends': friends}
    del user_id

    return render(request, 'vkapp/profile.html', context)
