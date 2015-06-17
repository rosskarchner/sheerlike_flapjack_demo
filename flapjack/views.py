from django.shortcuts import render

from sheerlike.query import get_document

# Create your views here.

def blog_detail(request, slug):
    post = get_document(doctype='posts', docid=slug)
    context = dict(post=post)
    return render(request, 'blog/_single.html', context=context)
