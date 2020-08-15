class InternalModelAdminMixin:
    """Mixin to catch all errors in the Django Admin and map them to user-visible errors."""
    def change_view(self, request, object_id, form_url='', extra_context=None):
        try:
            return super().change_view(request, object_id, form_url, extra_context)
        except Exception as e:
            self.message_user(request, 'Error changing model: %s' % e.msg, level=logging.ERROR)
            # This logic was cribbed from the `change_view()` handling here:
            # django/contrib/admin/options.py:response_post_save_add()
            # There might be a simpler way to do this, but it seems to do the job.
            return HttpResponseRedirect(request.path)