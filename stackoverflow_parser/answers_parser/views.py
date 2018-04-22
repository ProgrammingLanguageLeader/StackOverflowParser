from django.shortcuts import render
from django.http import JsonResponse
from django.utils.datastructures import MultiValueDictKeyError

from .parser import fetch_question_page_links


def index(request):
    return render(request, 'index.html')


def search_answers(request):
    try:
        question = request.GET['q']
    except MultiValueDictKeyError:
        question = ''

    question_links = fetch_question_page_links(question)
    questions_data = []
    for question_link in question_links:
        questions_data.append({
            'text': question_link.text,
            'link': 'https://stackoverflow.com%s' %
                    question_link.attrs['href']
        })
    data = {
        'is_taken': True,
        'questions_data': questions_data
    }
    return JsonResponse(data)
