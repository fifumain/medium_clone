from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CommonConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core_apps.common"
    # gettext_lazy() (_ in this case) postpones the loading of translations // optimisation
    verbose_name = _("Common")
