from django.shortcuts import render
from gallerie.models import MyPhotoModel
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# Create your views here.


def gallerie(request):
    photos_list = MyPhotoModel.objects.all()
    pagination = Paginator(photos_list, 16)
    page = request.GET.get('page')
    try:
        photos = pagination.page(page)
    except PageNotAnInteger:
        photos = pagination.page(1)
    except EmptyPage:
        photos = pagination.page(pagination.num_pages)

    context = {
        'photos': photos,
        'paginate': True
    }
    
    return render(request, 'gallerie/gallerie.html', context)

