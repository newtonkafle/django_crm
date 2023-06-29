from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .models import Lead, Agent
from .forms import LeadForm, LeadModelForm
from django.views import generic


# CRUD - (Actions) + List

class LandingPageView(generic.TemplateView):
    template_name = "landing.html"


def landing(request):
    return render(request, "landing.html")


class LeadListView(generic.ListView):
    template_name = "leads/lead_lists.html"
    queryset = Lead.objects.all()
    context_object_name = "leads"


def lead_list(request):
    # return HttpResponse("Hello world")
    leads = Lead.objects.all()

    context = {
        "leads": leads
    }
    return render(request, "leads/lead_lists.html", context)


class LeadDetailView(generic.DetailView):
    template_name = "leads/lead_detail.html"
    queryset = Lead.objects.all()
    context_object_name = "lead"


def detail_view(request, pk):
    """Gives the detail veiw of the lead"""
    lead = Lead.objects.get(id=pk)
    context = {
        "lead": lead
    }
    return render(request, "leads/lead_detail.html", context)


class LeadCreateView(generic.CreateView):
    template_name = "leads/lead_create.html"
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:lead-list")


def lead_create(request):
    """ Create the new lead using LeadModelForm """
    form = LeadModelForm()
    if request.method == "POST":
        form = LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/leads/")

    context = {
        "form": form
    }
    return render(request, "leads/lead_create.html", context)


class LeadUpdateView(generic.UpdateView):
    template_name = "leads/lead_update.html"
    queryset = Lead.objects.all()
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:lead-detail")


def lead_update(request, pk):
    """Update the lead with the given id """
    lead = Lead.objects.get(id=pk)
    form = LeadModelForm(instance=lead)
    if request.method == "POST":
        form = LeadModelForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect('/leads/')

    context = {
        "lead": lead,
        "form": form
    }
    return render(request, "leads/lead_update.html", context)


class LeadDeleteView(generic.DeleteView):
    template_name = "leads/lead_delete.html"
    queryset = Lead.objects.all()
    # form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:lead-list")


def lead_delete(request, pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect('/leads/')
