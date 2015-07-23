from django import forms
from django.contrib.auth.models import User
from ox_web.models import UserProfile, Blog, Job
from django.utils import timezone

class JobForm(forms.ModelForm):
  author = forms.CharField(max_length=100, widget=forms.HiddenInput(), required=False)
  created_at = forms.DateTimeField(widget=forms.HiddenInput(), required=False)
  
  class Meta:
    model = Job
    fields = ('author', 'created_at',)

class UserForm(forms.ModelForm):
  password = forms.CharField(widget=forms.PasswordInput())

  class Meta:
    model = User
    fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
  class Meta:
    model = UserProfile
    fields = ('website',)

class BlogPost(forms.ModelForm):
  title = forms.CharField(max_length=100)
  slug = forms.SlugField(widget=forms.HiddenInput(), max_length=100, required=False)
  body = forms.CharField(widget=forms.Textarea)
  author = forms.CharField(widget=forms.HiddenInput(), required=False)
  posted = forms.DateTimeField(widget=forms.HiddenInput(), required=False)

  class Meta:
    model = Blog
    fields = ('title', 'slug', 'body', 'author', 'posted',)

class InputForm(forms.Form):
  sim_type = forms.CharField(help_text='(MD)')
  backend = forms.CharField(help_text='(CPU)')
  backend_precision = forms.CharField(help_text='(double)')
  interaction_type = forms.CharField(help_text='(NBLOCK)')
  
  steps = forms.IntegerField(help_text='(10000)')
  newtonian_steps = forms.IntegerField(help_text='(103)')
  diff_coeff = forms.DecimalField(help_text='(2.50)')
  thermostat = forms.CharField(help_text='(john)')
  salt_concentration = forms.DecimalField(help_text='(0.5)')
  base_angle_range = forms.IntegerField(help_text='(360)')
  strand_orthogonality_range = forms.IntegerField(help_text='(360)')

  t = forms.CharField(help_text='(298 K)')
  dt = forms.DecimalField(help_text='(0.005)')
  verlet_skin = forms.DecimalField(help_text='(0.05)')

  topology = forms.CharField()
  conf_file = forms.CharField()
  lastconf_file = forms.CharField()
  trajectory_file = forms.CharField()
  refresh_vel = forms.IntegerField(help_text='(1)')
  log_file = forms.CharField()
  no_stdout_energy = forms.IntegerField(help_text='(1)')
  restart_step_counter = forms.IntegerField(help_text='(1)')
  energy_file = forms.CharField()
  print_conf_interval = forms.IntegerField(help_text='(100)')
  print_energy_every = forms.IntegerField(help_text='(100)')
  time_scale = forms.CharField(help_text='(linear)')
