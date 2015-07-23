from django import forms
from django.contrib.auth.models import User
from ox_web.models import UserProfile, Blog, Job
from django.utils import timezone

class JobForm(forms.ModelForm):
  author = forms.CharField(max_length=100, widget=forms.HiddenInput(), required=False)
  created_at = forms.DateTimeField(widget=forms.HiddenInput(), required=False)
  data_path = forms.CharField(max_length=200, widget=forms.HiddenInput(), required=False)
  output_path = forms.CharField(max_length=200, widget=forms.HiddenInput(), required=False)
  
  class Meta:
    model = Job
    fields = ('author', 'created_at', 'data_path', 'output_path',)

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
  sim_type = forms.CharField(initial='MD')
  backend = forms.CharField(initial='CPU')
  backend_precision = forms.CharField(initial='double')
  interaction_type = forms.CharField(initial='NBLOCK')
  
  steps = forms.IntegerField(initial='10000')
  newtonian_steps = forms.IntegerField(initial='103')
  diff_coeff = forms.DecimalField(initial='2.50')
  thermostat = forms.CharField(initial='john')
  salt_concentration = forms.DecimalField(initial='0.5')
  base_angle_range = forms.IntegerField(initial='360')
  strand_orthogonality_range = forms.IntegerField(initial='360')

  t = forms.CharField(initial='298 K')
  dt = forms.DecimalField(initial='0.005')
  verlet_skin = forms.DecimalField(initial='0.05')

  topology = forms.CharField(required=False)
  conf_file = forms.CharField(required=False)
  lastconf_file = forms.CharField(required=False)
  trajectory_file = forms.CharField(required=False)
  refresh_vel = forms.IntegerField(initial='1')
  log_file = forms.CharField(required=False)
  no_stdout_energy = forms.IntegerField(initial='1')
  restart_step_counter = forms.IntegerField(initial='1')
  energy_file = forms.CharField(required=False)
  print_conf_interval = forms.IntegerField(initial='100')
  print_energy_every = forms.IntegerField(initial='100')
  time_scale = forms.CharField(initial='linear')
