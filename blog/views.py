from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from . import models, forms, base
from django.conf import settings


class PostDetailView(DetailView):
    model = models.Post
    template_name = 'post-detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = forms.CommentForm()
        return context

    def get_object(self, queryset=None):
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        day = self.kwargs.get('day')
        slug = self.kwargs.get('slug')
        return get_object_or_404(models.Post,
                                 slug=slug,
                                 post_date__year=year,
                                 post_date__month=month,
                                 post_date__day=day
                                 )

    def post(self, request, **kwargs):
        form = forms.CommentForm(request.POST)
        form.instance.post = models.Post.objects.get(slug=self.kwargs['slug'])
        if form.is_valid():
            form.save()
        return redirect('detail', self.kwargs['year'], self.kwargs['month'], self.kwargs['day'], self.kwargs['slug'])

class AboutListView(ListView):
    model = models.About
    template_name = 'about.html'
    context_object_name = 'abouts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for about in context['abouts']:
            parts = about.my_skills_and_experiences.split('.')
            if len(parts) > 3:
                about.my_skills_part1 = '.'.join(parts[:3]) + '.'
                about.my_skills_part2 = '.'.join(parts[3:])
            else:
                about.my_skills_part1 = about.my_skills_and_experiences
                about.my_skills_part2 = ''
        return context


class EmailListView(ListView):
    model = models.EmailSite
    template_name = 'contact.html'
    context_object_name = 'emails'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = forms.CommentForm()
        return context

    def post(self, request, **kwargs):
        form = forms.EmailForm(request.POST)
        if form.is_valid():
            form.save()
            cd = form.cleaned_data
            message = f"{cd['comment']}\n Ushbu habar: {cd['name']}"
            send_mail(
                    'Test habar',
                    message,
                    cd['email'],
                    [settings.EMAIL_HOST_USER],
                    fail_silently=False,
                )
            return redirect('contact')
        else:
            return HttpResponse('Form is invalid')


class SearchView(base.PostList, ListView):
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return models.Post.objects.filter(title__icontains=query)
        return models.Post.objects.none()

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['q'] = self.request.GET.get('q')
        return context


class PostListView(base.PostList, ListView):
    context_object_name = 'posts'

class IndexListView(base.PostList, ListView):
    context_object_name = 'posts'

class PrivacyPolicyDetailView(base.PolicyList, ListView):
    context_object_name = 'policies'

class TermsConditionsListView(base.PolicyList, ListView):
    context_object_name = 'terms'



