from .signal import object_viewed_signal
class objectviewmixin:
    def dispatch(self,request,*args,**kwargs):
        try:
            instance=self.get_object()
        except self.model.DoesNotExist:
            instance=None
        if instance is not None and request.user.is_authenticate:
            object_viewed_signal.send(instance.__class__,instance=instance,request=request)
        return super(objectviewmixin,self).dispatch(request,*args,**kwargs)