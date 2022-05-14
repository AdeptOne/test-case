from django.http import Http404, HttpResponseRedirect

from ..services import get_link_by_short_link


def redirect_url_view(request, shortened_part):
    try:
        link = get_link_by_short_link(shortened_part)

        link.clicked()

        return HttpResponseRedirect(link.full_link)

    except:
        raise Http404('Извините это сломанная ссылка :(')
