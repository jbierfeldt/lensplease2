from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.contrib import messages

from registration.backends.default.views import RegistrationView, ActivationView

from photographer.models import PhotographerProfile
from photographer.forms import PhotographerProfileUpdateForm


class PhotographerProfileDetailView(DetailView):
    
    model = PhotographerProfile
    
    def get_object(self, queryset=None):
        obj = PhotographerProfile.objects.get(user__username=self.kwargs['photographer_username'])
        return obj


class PhotographerProfileUpdateView(UpdateView):
    model = PhotographerProfile
    form_class = PhotographerProfileUpdateForm
    template_name_suffix = '_update_form'
    
    def get_object(self, queryset=None):
        obj = PhotographerProfile.objects.get(user__username=self.kwargs['photographer_username'])
        return obj
        

class PhotographerRegistrationView(RegistrationView):

    template_name="photographer/registration_form.html"
        
    def get_success_url(self, request, user):
        """
        Return the name of the URL to redirect to after successful
        user registration.
        
        """
        return ('photographerregistration_complete', (), {})
    
        
class PhotographerActivationView(ActivationView):

    template_name = 'photographer/activate.html'
    
    def form_valid(self, request, form):
        return super(PhotographerActivationView, self).form_valid(request, form)
    
    def get_success_url(self, request, user):
        print messages.success(request, "Your account was successfully created %(user.username)s! Please take a moment to fill out the rest of your profile.", extra_tags='msg')
        return ('photographer_profile_update', (), {"photographer_username": user.username})