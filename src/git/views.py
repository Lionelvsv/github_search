from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic.list import ListView
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from github import Github  as gh


# Create your views here.

def search(request):
    template = loader.get_template('search.html')
    # g = Github("lionelvsv@gmail.com", "thala1188")
    # g = gh()
    # for repo in g.search_users(query='mike').get_page(0):
    #     print(repo.location)
    #     print(repo.url)
   
    context = {
    	    'latest_question_list': 'repo.name',
    	}
    return HttpResponse(template.render(context, request))
    
def searchresponse(request,  *args, **kwargs):
    template = loader.get_template('searchresponse.html')
    g = gh("lionelvsv@gmail.com", "thala1188")
    count = 0
    k = 0
    result = []
    # g = gh()
    if request.method == "GET":
        search =  request.GET['search']
        print(search)
        for repo in g.search_users(query=search)[:10]:
            result.append(repo)
            # print(result)

            
            count += 1
        paginator = Paginator(result, 6) # Show 10 contacts per page
        page = request.GET.get('page')
        contacts = paginator.get_page(page)

        print(paginator)


    
        context = {
        	    'object': contacts,
                'contacts': contacts,
                'search':search,
        	}
        return HttpResponse(template.render(context, request))
    # return HttpResponse((context, request))


