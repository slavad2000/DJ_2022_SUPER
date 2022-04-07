from django.shortcuts import render, redirect
from .vspomogatelnuy import *
from django.http.response import JsonResponse
from django.apps import apps
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.forms.models import inlineformset_factory
from .models import *
from .forms import *


'''Шаблоны форм соответствия модели'''
def template(nameSpr,param = ''): 
    CT_MODEL_CLASS = {
        'spr_company': {
                            'class_object_create':create_spr,
                            'class_object_update':update_spr,
                            'form_list': {
                                'classForm': None,
                                'template':'main/list_default.html'
                            },
                            'form_el': {
                                'classForm': spr_companyForm,
                                'template': 'main/spr_company_form.html'
                            },
                        },  
        'spr_object': {
                            'class_object_create':create_spr_object,
                            'class_object_update':update_spr_object,
                            'form_list': {
                                'classForm': None,
                                'template':'main/list_default.html'
                            },
                            'form_el': {
                                'classForm': spr_objectForm,
                                'template': 'main/spr_object_form.html'
                            },
                        },
        'spr_typemenu': {
                            'class_object_create':create_spr,
                            'class_object_update':update_spr,
                            'form_list': {
                                'classForm': None,
                                'template':'main/list_default.html'
                            },
                            'form_el': {
                                'classForm': spr_typemenuForm,
                                'template': 'main/base_formSpr.html'
                            },
                        },
        'spr_zaly': {
                            'class_object_create':create_spr,
                            'class_object_update':update_spr,
                            'form_list': {
                                'classForm': None,
                                'template':'main/list_default.html'
                            },
                            'form_el': {
                                'classForm': spr_zalyForm,
                                'template': 'main/base_formSpr.html'
                            },
                        },   
        'spr_doljnosty': {
                            'class_object_create':create_spr,
                            'class_object_update':update_spr,
                              'form_list': {
                                'classForm': None,
                                'template':'main/list_default.html'
                            },
                            'form_el': {
                                'classForm': spr_doljnostyForm,
                                'template': 'main/base_formSpr.html'
                            },
                        },
        'spr_fizlitso': {
                            'class_object_create':create_spr,
                            'class_object_update':update_spr,
                            'form_list': {
                                'classForm': None,
                                'template':'main/list_default.html'
                            },
                            'form_el': {
                                'classForm': spr_fizlitsoForm,
                                'template': 'main/base_formSpr.html'
                            },
                        },
        'spr_role': {
                            'class_object_create':create_spr,
                            'class_object_update':update_spr,
                            'form_list': {
                                'classForm': None,
                                'template':'main/list_default.html'
                            },
                            'form_el': {
                                'classForm': spr_roleForm,
                                'template': 'main/base_formSpr.html'
                            },
                        }, 
        'spr_units': {
                            'class_object_create':create_spr,
                            'class_object_update':update_spr,
                            'form_list': {
                                'classForm': None,
                                'template':'main/list_default.html'
                            },
                            'form_el': {
                                'classForm': spr_unitsForm,
                                'template': 'main/base_formSpr.html'
                            },
                        },    
        'spr_nomenklatura': {
                            'class_object_create':create_spr,
                            'class_object_update':update_spr,
                             'form_list': {
                                'classForm': None,
                                'template':'main/list_default.html'
                            },
                            'form_el': {
                                'classForm': spr_nomenklaturaForm,
                                'template': 'main/base_formSpr.html'
                            },
                            'form_gr': {
                                'classForm': spr_nomenklaturaForm_gr,
                                'template': 'main/base_formSpr.html'
                            },
                        },    
        'spr_variantoplaty': {
                            'class_object_create':create_spr,
                            'class_object_update':update_spr,
                             'form_list': {
                                'classForm': None,
                                'template':'main/list_default.html'
                            },
                            'form_el': {
                                'classForm': spr_variantoplatyForm,
                                'template': 'main/base_formSpr.html'
                            },
                        },    
        'spr_statiyzatrat': {
                            'class_object_create':create_spr,
                            'class_object_update':update_spr,
                             'form_list': {
                                'classForm': None,
                                'template':'main/list_default.html'
                            },
                            'form_el': {
                                'classForm': spr_statiyzatratForm,
                                'template': 'main/base_formSpr.html'
                            },
                        },      
        'spr_priznakdelete': {
                            'class_object_create':create_spr,
                            'class_object_update':update_spr,
                             'form_list': {
                                'classForm': None,
                                'template':'main/list_default.html'
                            },
                            'form_el': {
                                'classForm': spr_priznakdeleteForm,
                                'template': 'main/base_formSpr.html'
                            },
                        },      
        'spr_pictures': {
                            'class_object_create':create_spr,
                            'class_object_update':update_spr,
                             'form_list': {
                                'classForm': None,
                                'template':'main/list_default.html'
                            },
                            'form_el': {
                                'classForm': spr_picturesForm,
                                'template': 'main/base_formSpr.html'
                            },
                        },    
        'spr_otdely': {
                            'class_object_create':create_spr,
                            'class_object_update':update_spr,
                             'form_list': {
                                'classForm': None,
                                'template':'main/list_default.html'
                            },
                            'form_el': {
                                'classForm': spr_otdelyForm,
                                'template': 'main/base_formSpr.html'
                            },
                        },        
        'spr_stavkands': {
                            'class_object_create':create_spr,
                            'class_object_update':update_spr,
                             'form_list': {
                                'classForm': None,
                                'template':'main/list_default.html'
                            },
                            'form_el': {
                                'classForm': spr_stavkandsForm,
                                'template': 'main/base_formSpr.html'
                            },
                        },  
        'spr_categories': {
                            'class_object_create':create_spr,
                            'class_object_update':update_spr,
                             'form_list': {
                                'classForm': None,
                                'template':'main/list_default.html'
                            },
                            'form_el': {
                                'classForm': spr_categoriesForm,
                                'template': 'main/base_formSpr.html'
                            },
                        },  
        'spr_grprint': {
                            'class_object_create':create_spr,
                            'class_object_update':update_spr,
                             'form_list': {
                                'classForm': None,
                                'template':'main/list_default.html'
                            },
                            'form_el': {
                                'classForm': spr_grprintForm,
                                'template': 'main/base_formSpr.html'
                            },
                        },       
        'spr_menu': {
                            'class_object_create':create_spr,
                            'class_object_update':update_spr,
                             'form_list': {
                                'classForm': None,
                                'template':'main/list_default.html'
                            },
                            'form_el': {
                                'classForm': spr_menuForm,
                                'template': 'main/base_formSpr.html'
                            },
                            'form_gr': {
                                'classForm': spr_menuForm_gr,
                                'template': 'main/base_formSpr.html'
                            },                            
                        },     
        'spr_conditions': {
                            'class_object_create':create_spr,
                            'class_object_update':update_spr,
                             'form_list': {
                                'classForm': None,
                                'template':'main/list_default.html'
                            },
                            'form_el': {
                                'classForm': spr_conditionsForm,
                                'template': 'main/base_formSpr.html'
                            },
                        },   
        'spr_modificators': {
                            'class_object_create':create_spr,
                            'class_object_update':update_spr,
                             'form_list': {
                                'classForm': None,
                                'template':'main/list_default.html'
                            },
                            'form_el': {
                                'classForm': spr_modificatorsForm,
                                'template': 'main/base_formSpr.html'
                            },
                            'form_gr': {
                                'classForm': spr_modificatorsForm_gr,
                                'template': 'main/base_formSpr.html'
                            },                            
                        },                                                                                                                                                                                                                                                                                                                                                               
    }  

    temp = {
        'class_object_create': create_spr,
        'class_object_update': update_spr,
        'classForm': None,
        'template': 'main/list_default.html' 
    }

    classForm = None
    template = 'main/list_default.html' 

    try: 
        M = CT_MODEL_CLASS[nameSpr]
        temp['class_object_create'] = M['class_object_create'] 
        temp['class_object_update'] = M['class_object_update'] 
    except:
        pass 

    if (param):
        try: 
            temp['classForm'] = M[param['type']]['classForm'] 
            temp['template'] = M[param['type']]['template'] 
        except:
            pass 

    return temp                          


'''Дефолтные параметры справочника'''
class default_spr:
    def dispatch(self, *args, **kwargs):
        self.model = apps.get_model('main', kwargs['nameTabl'])

        p_group = False
        if (self.request.GET):
            if ('group' in self.request.GET):     
                p_group = str2bool(self.request.GET['group'])  

        elif (self.request.POST):
            if ('group' in self.request.POST):     
                p_group = str2bool(self.request.POST['group'])  

        temp = template(self.model.__name__, {'type': 'form_gr' if (p_group) else 'form_el'})
        self.form_class = temp['classForm']
        self.template_name = temp['template']

        return super().dispatch(*args, **kwargs)

    def get_success_url(self):
        if ('close' in self.request.POST):
            url_pattern = '/tabl/{nametabl}/?owner={owner_id}&parent={parent_id}'
        else:
            url_pattern = '/tabl/{nametabl}/{id}'            

        try:
            owner = self.object.owner.pk
        except:
            owner = None
        try:
            parent = self.object.parent.pk
        except:
            parent = None

        url = url_pattern.format(id = self.object.id, nametabl = self.model.__name__, owner_id = owner if (owner) else '', parent_id = parent if (parent) else '')
        return url

    def def_get_form_kwargs(self):
        kwargs = super(self.__class__, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        kwargs.update({'owner_old': self.request.GET['owner'] if ('owner' in self.request.GET) else ''})
        kwargs.update({'parent_old': self.request.GET['parent'] if ('parent' in self.request.GET) else ''})
        return kwargs

    def def_get_initial(self):
        initial = super(self.__class__, self).get_initial()
        if (self.request.GET):
            if ('parent' in self.request.GET):  
                if (self.request.GET['parent'] != ''):
                    initial['parent'] = self.model.objects.get(pk=self.request.GET['parent'])
            if ('owner' in self.request.GET):  
                if (self.request.GET['owner'] != ''):
                    mod = apps.get_model('main', self.model._meta.get_field('owner').target_field.model.__name__)
                    initial['owner'] = mod.objects.get(pk=self.request.GET['owner'])
        return initial

    def get_context_data(self, **kwargs):
        if (self.object != None):
            try:
                p_group = self.object.group 
            except:
                p_group = False

            temp = template(self.model.__name__, {'type': 'form_gr' if (p_group) else 'form_el'})
            self.form_class = temp['classForm']
            self.template_name = temp['template']

        context = super().get_context_data(**kwargs) 
        context['caption']= self.model._meta.verbose_name
        context['nameTabl']= self.model.__name__
        context['id_element']= 'add' if (self.object == None) else self.object.pk
        return context

    def form_valid(self, form):
        form.instance.reg_global_id = self.request.user.reg_global.pk
        try:
            return super().form_valid(form)      
        except Exception as e:
            form.add_error('__all__', e)
            return super().form_invalid(form)  


'''Дефолтные класс создание элемента'''
class create_spr(default_spr,CreateView):
    def get_initial(self):
        return self.def_get_initial()   
    def get_form_kwargs(self):
        return self.def_get_form_kwargs()  


'''Дефолтные класс редактирования элемента'''
class update_spr(default_spr,UpdateView):
    def get_form_kwargs(self):
        return self.def_get_form_kwargs()              


'''Список справочника'''  
class def_list(ListView): 
    def dispatch(self, *args, **kwargs):
        self.model = apps.get_model('main', kwargs['nameTabl'])

        temp = template(self.model.__name__, {'type': 'form_list'})
        self.form_class = temp['classForm']
        self.template_name = temp['template']

        return super().dispatch(*args, **kwargs)
    
    def get_queryset(self):
        self.p_global = get_param(self.model,'reg_global')
        self.p_owner = get_param(self.model,'owner')
        self.p_parent = get_param(self.model,'parent')
        self.parent_list = []

        if (self.p_owner):
            _owner = apps.get_model('main', self.model._meta.get_field('owner').target_field.model.__name__)
            if (get_param(_owner,'reg_global')):
                self.owner = apps.get_model('main', self.model._meta.get_field('owner').target_field.model.__name__).objects.filter(reg_global=self.request.user.reg_global)            
            else:
                self.owner = apps.get_model('main', self.model._meta.get_field('owner').target_field.model.__name__).objects.all()            

            self.owner_name = self.model._meta.get_field('owner').target_field.model._meta.verbose_name
            self.owner_class = self.model._meta.get_field('owner').target_field.model.__name__ 

            self.owner_id = '' 
            if ('owner' in self.request.GET):
                if (self.request.GET['owner']):
                    self.owner_id = self.request.GET['owner']

            if (self.owner_id == ''): 
                if (self.owner.count() != 0):
                    self.owner_id = str(self.owner[0].pk)

            if (self.owner_id == ''):
                filter= Q(owner__isnull=True) 
            else:
                filter= Q(owner_id=self.owner_id);

        else:
            filter = Q(reg_global=self.request.user.reg_global)            

        if (self.p_parent):
            f = Q(parent__isnull=True)  
            if ('parent' in self.request.GET):
                if (self.request.GET['parent']):
                    obj = self.model.objects.get(pk=self.request.GET['parent'])
                    f = Q(parent_id=obj.id);
                    list_parent(obj,self.parent_list) 
            filter = filter & f

        sort = list()

        if (get_param(self.model,'group')):
            sort.append('-group') 

        if (get_param(self.model,'group')):            
            sort.append('code')       
        else:
            sort.append('pk')       

        return self.model.objects.filter(filter).order_by(*sort)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nameTabl'] = self.model.__name__
        context['name_spr'] = self.model._meta.verbose_name_plural
        context['p_group'] = get_param(self.model,'group')
        context['m_column'] = self.model.visible_colum_list(self.model)  
        context['parent_list'] = self.parent_list
        if (self.p_owner):
            context['owner_name'] = self.owner_name
            context['owner_class'] = self.owner_class
            context['owner'] = self.owner
            context['owner_id'] = self.owner_id

        return context       


'''Ссылка на создание нового элемента'''
def def_create_spr (request, *args, **kwargs):
    return template(kwargs['nameTabl'])['class_object_create'].as_view()(request, *args, **kwargs)


'''ссылка на редактирование элемента'''
def def_update_spr (request, *args, **kwargs):
    if ('delete' in request.POST):
        return smenaStatusDel(request, *args, **kwargs)

    if ('copy' in request.POST):
        return copyElement(request, *args, **kwargs)

    return template(kwargs['nameTabl'])['class_object_update'].as_view()(request, *args, **kwargs)    


'''Процедура смены признака удаления'''
def smenaStatusDel(request, *args, **kwargs):
    Spr = apps.get_model('main', kwargs['nameTabl'])
    obj = Spr.objects.get(pk=kwargs['pk'])
    obj.deleted = not obj.deleted
    obj.save();

    group = obj.group if (get_param(Spr,'group')) else False

    return JsonResponse({'deleted': obj.deleted, 'group':group}, status=200)
    

'''Копирование элемента'''
def copyElement(request, *args, **kwargs):
    model = apps.get_model('main', kwargs['nameTabl'])
    obj = model.objects.get(pk=kwargs['pk'])
    obj.pk = None
    obj.code =''

    try:
        p_group = obj.group 
    except:
        p_group = False

    temp = template(kwargs['nameTabl'], {'type': 'form_gr' if (p_group) else 'form_el'})
    form_class = temp['classForm']
    template_name = temp['template']

    context = {}
    context['form'] = form_class(instance=obj, user=request.user)
    context['caption']= model._meta.verbose_name
    context['nameTabl']= model.__name__
    context['id_element']= 'add'

    return render(request, template_name, context)


def index(request):
    MENU = [
        {
            'id':'spr', 
            'name':'Справочники',
            'data': [
                {'id':'spr_company','name':'Структура компаний'},
                {'id':'spr_object','name':'Подразделения'},
                {'id':'spr_typemenu','name':'Типы меню'},
                {'id':'spr_zaly','name':'Залы'},
                {'id':'spr_fizlitso','name':'Физические лица'},
                {'id':'spr_role','name':'Права доступа'},
                {'id':'spr_doljnosty','name':'Должности персонала'},
                {'id':'spr_units','name':'Классификатор единиц измерения'},
                {'id':'spr_nomenklatura','name':'Номенклатура'},
                {'id':'spr_variantoplaty','name':'Способы оплаты'},
                {'id':'spr_statiyzatrat','name':'Статьи затрат'},
                {'id':'spr_priznakdelete','name':'Признаки удаления'},
                {'id':'spr_pictures','name':'Картинки on-line заказов'},
                {'id':'spr_otdely','name':'Отделы'},
                {'id':'spr_stavkands','name':'Ставки НДС'},
                {'id':'spr_categories','name':'Категории'},
                {'id':'spr_grprint','name':'Группы печати'},
                {'id':'spr_menu','name':'Меню'},
                {'id':'spr_conditions','name':'Условия примнения скидок\наценок'},
                {'id':'spr_modificators','name':'Модификаторы'},
            ]
        }
    ]    
    return render(request, 'main/index.html', {'MENU':MENU})


    
class create_spr_object(default_spr,CreateView):
    UsersFormSet = inlineformset_factory(spr_object, spr_object_users, form = spr_object_usersForm_el, fk_name='owner', fields = '__all__',extra=0) 
    def get_initial(self):
        return self.def_get_initial()   

    def get_form_kwargs(self):
        return self.def_get_form_kwargs()

    def form_valid(self, form, formset):
        form.instance.reg_global_id = self.request.user.reg_global.pk
        self.object= form.save()

        formset.instance = self.object
        formset.save()

        try:
            return redirect(self.get_success_url())   
        except Exception as e:
            form.add_error('__all__', e)
            return super().form_invalid(form)  

    def form_invalid(self, form, formset):            
        return self.render_to_response(self.get_context_data(form=form,formset=formset))

    def get(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        formset = self.UsersFormSet(form_kwargs={'user': request.user}) 
        return self.render_to_response(self.get_context_data(form=form,formset=formset))

    def post(self, request, *args, **kw):
        self.object = None
        form = self.get_form()

        formset = self.UsersFormSet(self.request.POST, form_kwargs={'user': request.user}) 
        if all([form.is_valid(), formset.is_valid()]):
            return self.form_valid(form, formset)
        else:
            return self.form_invalid(form, formset)


class update_spr_object(default_spr,UpdateView):
    UsersFormSet = inlineformset_factory(spr_object, spr_object_users, form = spr_object_usersForm_el, fk_name='owner', fields = '__all__',extra=0) 
    def get_form_kwargs(self):
        return self.def_get_form_kwargs()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context['formset']=self.UsersFormSet(instance = self.object,form_kwargs={'user': self.request.user}) 
        return context

    def form_valid(self, form):
        try:
            formset = self.UsersFormSet(self.request.POST, instance=self.object, form_kwargs={'user': self.request.user})
            if (formset.is_valid()):
                formset.save()
            else:
                return self.render_to_response(self.get_context_data(form=form, formset=formset))

            return super().form_valid(form)      
        except Exception as e:
            form.add_error('__all__', e)
            return super().form_invalid(form)          
