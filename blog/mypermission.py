from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse

# for custome permission
class customepermission(PermissionRequiredMixin):

    # this check permission and return true or false
    def has_permission(self) :
        if self.request.user.is_staff:
            return True
        # return False
        
    
    # this redirect if perrmission not allowed (if has_permission return Fasle then)
    def get_login_url(self) -> str:
        return reverse('blog_post_list')