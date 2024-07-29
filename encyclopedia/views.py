from django.shortcuts import render,redirect
from markdown2 import markdown
from . import util
from random import randint

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
    
def entry(request, title):
    content = util.get_entry(title)
    if content == None:
        content = "## Error, Page was not found"
    content = markdown(content)
    return render(request, "encyclopedia/entry.html", 
                  {'content': content, 'title': title})

def search(request):
    info = request.GET.get('q')
    if info in util.list_entries():
        return redirect("entry", title=info)
    return render(request, "encyclopedia/search.html", {
        "entries": util.search_entries(info), 
        "info": info})
    
def create(request):
    if request.method == "POST":
        content = request.POST.get("content")
        title = request.POST.get("title")
        if title in util.list_entries():
            return render(request, "encyclopedia/error.html")
        util.save_entry(title, content)
        return redirect("entry", title=title)
    return render(request, "encyclopedia/create.html")
        
     
def random(request):
    entries = util.list_entries()
    entry = entries[randint(0, len(entries) - 1)]
    return redirect("entry", title=entry)