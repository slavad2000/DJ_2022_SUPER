from .models import *
from .forms import *


class spr_typemenuForm(spr_defaultForm):
    class Meta:
        model = spr_typemenu
        exclude = ['reg_global']