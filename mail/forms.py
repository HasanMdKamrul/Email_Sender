from django import forms



class MailCreateForm(forms.Form): 
    
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    receiver_one = forms.EmailField()
    receiver_two = forms.EmailField(required=False,widget=forms.EmailInput(attrs={'placeholder':'Optional if more than one required'}))
    cc_myself = forms.BooleanField(required=False)
    