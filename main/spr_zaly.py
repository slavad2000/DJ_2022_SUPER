from .models import *
from .forms import *


class spr_zalyForm(spr_defaultForm):
    class Meta:
        model = spr_zaly
        exclude = ['reg_global']