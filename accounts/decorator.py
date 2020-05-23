from functools import wraps

from django.shortcuts import HttpResponseRedirect


def login_register_check(url):
    def decorator(view_func):
        @wraps(view_func)
        def _is_logged_in(req,*args,**kwargs):
            if req.user.is_authenticated:
                return HttpResponseRedirect(url)
            else:
                return view_func(req,*args,**kwargs)
        return _is_logged_in
    return decorator