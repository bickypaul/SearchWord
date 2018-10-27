from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .searchProgram import search, sort_results #relative import
import json

#renders the search page.
def search_view(request):
    return render(request, 'search.html', {})

#Returns the autocomplete results while the user types in a letter.
def search_autocomplete(request):
    if request.is_ajax():
        query = request.GET.get('term','')
        results = sort_results(search(query.lower()), query.lower())
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)

# Returns a jsonresponse having the search results(25 words) containing the searched word(partial)
def getSearchResults(request):
    if request.method == 'GET':
        query = request.GET.get('term') # for example: query = 'hello'
        searchResult = sort_results(search(query.lower()), query.lower())
        if len(searchResult) == 0:
            return JsonResponse({'Search_Result': "Word not found."})
        else:
            return JsonResponse({'Search_Result': searchResult})


