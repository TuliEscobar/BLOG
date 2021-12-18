from django.core.exceptions import PermissionDenied

class AdminRequiredMixins():
	def dispatch(self, request, *arg, **kwargs):	
		if not request.user.is_admin:
			raise PermissionDenied	
		return super(AdminRequiredMixins,self).dispatch(request,*arg,**kwargs)

        