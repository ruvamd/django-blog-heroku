from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext, loader
from blogging.models import Post
from django.views.generic import ListView
from django.views.generic import DetailView
from django.utils import timezone


class PostListView(ListView):
    # model = Post
    queryset = Post.objects.exclude(published_date__exact=None).order_by(
        "-published_date"
    )
    template_name = "blogging/list.html"
    # def get_queryset(self):
    #     queryset = Post.objects.order_by('-publication_date')
    #     return queryset

    # queryset =Post.objects.filter(pub_date__lte=timezone.now())
    # context_object_name ='post_list'

    # def get_queryset(self):
    #     """
    #     Excludes any questions that aren't published yet.
    #     """
    #     return Post.objects.filter(pub_date__lte=timezone.now())


class PostDetailView(DetailView):
    # model = Post
    # queryset = Post.objects.all()
    # context_object_name='post'
    queryset = Post.objects.exclude(published_date__exact=None)
    template_name = "blogging/detail.html"
    # def get_queryset(self):
    #     queryset = Post.objects.exclude(published_date__exact=None)
    #     return queryset


# def stub_view(request, *args, **kwargs):
#     body = "Stub View\n\n"
#     if args:
#         body += "Args:\n"
#         body += "\n".join(["\t%s" % a for a in args])
#     if kwargs:
#         body += "Kwargs:\n"
#         body += "\n".join(["\t%s: %s" % i for i in kwargs.items()])
#     return HttpResponse(body, content_type="text/plain")

# first old
# def list_view(request):
#     published = Post.objects.exclude(published_date__exact=None)
#     posts = published.order_by('-published_date')
#     template = loader.get_template('blogging/list.html')
#     context = {'posts': posts}
#     body = template.render(context)
#     return HttpResponse(body, content_type="text/html")

# second old
# def list_view(request):
#     published = Post.objects.exclude(published_date__exact=None)
#     posts = published.order_by('-published_date')
#     context = {'posts': posts}
#     return render(request, 'blogging/list.html', context)


# old
# def detail_view(request, post_id):
#     published = Post.objects.exclude(published_date__exact=None)
#     try:
#         post = published.get(pk=post_id)
#     except Post.DoesNotExist:
#         raise Http404
#     context = {'post': post}
#     return render(request, 'blogging/detail.html', context)
