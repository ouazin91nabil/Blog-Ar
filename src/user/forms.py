from django import forms
from django.contrib.auth.models import User


class UserCreationForm(forms.ModelForm):
    username = forms.CharField(label='إسم المستخدم', max_length=30, help_text='إسم المستخدم يجب ألا يحتوي على مسافات')
    email = forms.EmailField(label='البريد الإلكتروني')
    first_name = forms.CharField(label='الإسم الأول', max_length=100)
    last_name = forms.CharField(label='الإسم الأخير', max_length=100)
    password1 = forms.CharField(label='كلمة المرور', widget=forms.PasswordInput(), min_length=8)
    password2 = forms.CharField(label='تأكيد كلمة المرور', widget=forms.PasswordInput(), min_length=8)
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name',
                  'last_name', 'password1', 'password2')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('كلمة المرور غير متطابقة')
        return cd['password2']

    def clean_username(self):
        cd = self.cleaned_data
        if User.objects.filter(username=cd['username']).exists():
            raise forms.ValidationError('يوجد مستخدم مسجل بهذا اإسم')
        return cd['username']


class LoginForm(forms.ModelForm):
    username = forms.CharField(label='إسم المستخدم', max_length=30, help_text='يرجى عدم وضع فراغات في إسم المستخدم.')
    password = forms.CharField(label='كلمة المرور', widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'password')

