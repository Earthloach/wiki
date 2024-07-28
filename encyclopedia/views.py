from django.shortcuts import render
from markdown2 import markdown
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
    
def entry(request, title):
    content = util.get_entry(title.strip())
    if content == None:
        content = "## Error, Page was not found"
    content = markdown(content)
    return render(request, "encyclopedia/entry.html", 
                  {'content': content, 'title': title})
