from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from ..forms import AddLinkForm
from ..services import get_links_by_user


@login_required
def shortener_view(request):
    template_name = 'shortener/shortener.html'

    links = get_links_by_user(request.user)
    paginator = Paginator(links, 7)
    page_number = int(request.GET.get('page', 1))
    links_page = paginator.get_page(page_number)

    context = {
        'form': AddLinkForm(),
        'links_page': links_page,
    }

    if request.method == 'GET':

        return render(request, template_name, context)

    elif request.method == 'POST':
        form = AddLinkForm(request.POST)

        if form.is_valid():
            shortened_object = form.save(commit=False)
            shortened_object.user = request.user
            shortened_object.save()

            return redirect('shortener')

        context['errors'] = form.errors

        return render(request, template_name, context)
