from rest_framework.permissions import BasePermission


class GlobalPermissionClass(BasePermission):
    def has_permission(self, request, view):
        permission_codename = self.__get_model_permission_codename(method=request.method, view=view)
        if not permission_codename:
            return False
        return request.user.has_perm(permission_codename)
    
    def __get_model_permission_codename(self, method, view):
        try:
            model_name = view.queryset.model._meta.model_name
            app_label = view.queryset.model._meta.app_label
            action = self.__get_action_sufix(method)
            return f"{app_label}.{action}_{model_name}"
        except AttributeError:
            return None
    
    def __get_action_sufix(self, method):
        sufix = {
            "GET": "view",
            "HEAD": "view",
            "OPTIONS": "view",
            "POST": "add",
            "PUT": "change",
            "PATCH": "change",
            "DELETE": "delete",
        }
        return sufix[method]