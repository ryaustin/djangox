from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


class HomePageView(TemplateView):
    template_name = "pages/home.html"

class AboutPageView(TemplateView):
    template_name = "pages/about.html"

@login_required
def protected_view(request):
    template_name = "pages/about.html"
    return render(request, template_name=template_name, context={'secret_message': "This message is only visible to logged-in users"})

@login_required
def reservation_list(request):
    """A view that returns a list of reservations"""
    reservation_list = Reservation.objects.all()
    template_name = "pages/reservation_list.html"
    data = {"reservation_list": reservation_list, "company": "Thunder Canyon"}
    return render(request, template_name=template_name, context=data)

