from ..models import Link


def get_links_by_user(user):
    links = Link.objects.filter(user=user).values('full_link', 'short_link', 'clicks', 'created_at')
    return links


def get_link_by_short_link(short_link):
    return Link.objects.get(short_link=short_link)
