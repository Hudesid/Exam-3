from . import models


class PostList():
    model = models.Post
    template_name = 'list.html'


class PolicyList():
    model = models.PrivacyPolicy
    template_name = 'privacy-policy.html'
