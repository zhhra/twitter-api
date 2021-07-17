from ..models.user import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect


@login_required
def follow_unfollow(request, pk):
    user = get_object_or_404(User, username=request.user)
    account = get_object_or_404(User, pk=pk)
    if user == account:
        return redirect("auth:info", pk=pk)

    if user.followings.filter(username=account).exists():
        user.followings.remove(account)

    else:
        user.followings.add(account)

    return redirect("auth:info", pk=pk)
