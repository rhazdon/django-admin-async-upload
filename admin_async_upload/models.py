from django.db import models

from admin_async_upload.widgets import ResumableAdminWidget
from admin_async_upload.fields import FormResumableFileField


class AsyncFileField(models.FileField):
    def formfield(self, **kwargs):
        defaults = {"form_class": FormResumableFileField}
        if self.model and self.name:
            defaults["widget"] = ResumableAdminWidget(
                attrs={"model": self.model, "field_name": self.name}
            )
        kwargs.update(defaults)
        return super(AsyncFileField, self).formfield(**kwargs)
