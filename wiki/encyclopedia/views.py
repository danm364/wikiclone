from django.shortcuts import render
from django.http import HttpResponse

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
#how do i make sure im passing the correct variable?
def entry(request, title):
    page_title = title
    if util.get_entry(page_title) == None:
        return HttpResponse("Requested Page Was Not Found")
    
    else: 
        return render(request, "encyclopedia/entry.html", {
       "entry": util.get_entry(page_title),
       "page_title": page_title
    })
    
def search(request):
    print(request.GET)
    print(request.GET['q'])
    # How do we pass the value in our search bar as a variable to
    page_title = request.GET['q']
    # if the entry is not available we need to search all entries to see if 
    # any entries have our search as a substring
    # than return all entries that include our substring as a list on a page
    if util.get_entry(page_title) == None:
        entries = util.list_entries()
        new_list = []
        print(entries)
        for item in entries:
            if page_title in item.lower():
                new_list.append(item)

        return render(request, "encyclopedia/search_page.html", {
            "entries": new_list
        })
    # if the entry is available bring us directly to entry page via our search button
    else: 
        return render(request, "encyclopedia/entry.html", {
       "entry": util.get_entry(page_title),
       "page_title": page_title
    })

