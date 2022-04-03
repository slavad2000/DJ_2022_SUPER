
'''Проверка на ИСТИНУ'''
def str2bool(v):
  return v.lower() in ("yes", "true", "t", "1", "on")


'''Проверяем наличие реквизита в моделе'''
def get_param(model,param):
    try: _param = True if (model._meta.get_field(param)) else False
    except: _param = False
    return _param 


'''Получение иерархии групп'''
def list_parent (item,list):
    if (item):
        list.insert(0,item)
        list_parent(item.parent,list)


