from api.models import Posts

def activity(request):
    if request.user.is_authenticated:
        cnt=Posts.objects.filter(user=request.user).count()
        pup=Posts.objects.filter(upvote=request.user).count()
        return {"pcount":cnt,"punt":pup}
    else:
        return {"pcount":0}