from django.shortcuts import render,reverse,redirect
from django.views import generic
from .forms import MailCreateForm
from django.core.mail import send_mail
# Create your views here.


# Cann't use the builtin create view because it's related to a model 

'''class MailCreateView(generic.CreateView):
    template_name = 'mail/mail_create.html'
    context_object_name = "mail"
    form_class = MailCreateForm
    
    
    def get_success_url(self):
        return reverse('mails:mail_create')
    
    def form_valid(self ,form):
        form = form.save()
        subject = form.subject
        message = form.message
        from_email = self.request.user.email
        receiver_one = form.receiver_one
        receiver_two = form.receiver_two
        cc_myself = form.cc_myself
        
        recipient_list = [receiver_one,receiver_two]
        
        if cc_myself==True:
            recipient_list.append(from_email)
        
        send_mail(
            subject = subject,
            message = message,
            from_email = from_email,
            recipient_list = recipient_list,
        )
        
        return super().form_valid(form)'''


# When there is no model involved only forms we can easily add required fields. 

def MailCreate(request):
    form = MailCreateForm()
    
    if request.method == 'POST':
        form = MailCreateForm(request.POST)
        
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            receiver_one = form.cleaned_data['receiver_one']
            cc_myself = form.cleaned_data['cc_myself']
            
            
            recipient_list = [receiver_one]
            
            if cc_myself == True:
                recipient_list.append(sender)
                
            
            
            send_mail(
                subject = subject,
                message = message,
                from_email = sender,
                recipient_list = recipient_list,
            )
           
            return redirect('mails:mail_create')
        
    context = {'form':form}
    
    
        
    return render(request, 'mail/mail_create.html', context)