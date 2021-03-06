from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound,\
HttpResponseNotAllowed, HttpResponseBadRequest, HttpResponseRedirect
from models import Url
from django.views.decorators.csrf import csrf_exempt


def getUrls(urlList):
    urls = ""
    for url in urlList:
        urls += "<pre>" + url.longUrl + "\t\t" + str(url.id) + "<br/>"
    return urls + "<br/>"


def processPost(url):
    if url == "":
        return HttpResponseBadRequest("ERROR: EMPTY POST")
    elif not url.startswith("http://") and not url.startswith("https://"):
        url = "http://" + url
    try:
        newUrl = Url.objects.get(longUrl=url)
    except Url.DoesNotExist:
        newUrl = Url(longUrl=url)
        newUrl.save()
    response = "<p>url real: <a href=" + url + ">" + url + "</a></p>"
    response += "<p>url acortada: <a href=" + str(newUrl.id) + ">" +\
                str(newUrl.id) + "</a></p>"
    return HttpResponse(response)


@csrf_exempt
def processHome(request):
    if request.method == "GET":
        urlList = Url.objects.all()
        urls = getUrls(urlList)
        form = "<form action='' method='POST'>URL para acortar: <input type=\
                'text' name='url'><input type='submit' value='Enviar'></form>"
        return HttpResponse(urls + form)
    elif request.method == "POST":
        url = request.POST.get("url")
        response = processPost(url)
        return response
    else:
        return HttpResponseNotAllowed("Only GET and POST are allowed")


def redirect(request, id):
    try:
        url = Url.objects.get(id=id)
    except Url.DoesNotExist:
        return HttpResponseNotFound(str(id) + " not found")
    return HttpResponseRedirect(url.longUrl)
