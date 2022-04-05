from django.core.paginator import Paginator
ob=['Aneesh','vicky','chitti']
p=Paginator(ob,3)

print(p.count)
print(p.num_pages)