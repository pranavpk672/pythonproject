from django import forms


class regform(forms.Form):
    name=forms.CharField(max_length=30)
    email=forms.EmailField()
    password=forms.CharField(max_length=30)
    cpassword=forms.CharField(max_length=30)

    phone = forms.IntegerField()



class logform(forms.Form):
    email=forms.EmailField()
    password=forms.CharField(max_length=30)
