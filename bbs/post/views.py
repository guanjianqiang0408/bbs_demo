from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from post.models import Topic, Comment
from post.post_service import build_topic_base_info, build_topic_detail_info, add_comment_to_topic
from post.forms import TopicSearchForm

# Create your views here.
def index(request):
    """
    using django templates
    """
    return render(request, 'hello_world.html', context={"data": "hello world"})


def topic_list_view(request):
    topics = Topic.objects.all()
    result = JsonResponse({
        "count": topics.count(),
        "info": [build_topic_base_info(topic) for topic in topics]
    })
    return result


def topic_detail_view(request, topic_id):
    try:
        result = build_topic_detail_info(Topic.objects.get(pk=topic_id))
    except Topic.DoesNotExist:
        pass
    return JsonResponse(result)


def add_comment_to_topic_view(request):
    topic_id = request.POST.get('id', 0)
    content = request.POST.get("content", "")
    topic = None
    try:
        topic = Topic.objects.get(pk=topic_id)
    except Topic.DoesNotExist:
        pass
    if topic and content:
        return JsonResponse({"id": add_comment_to_topic(topic, content).id})
    return JsonResponse({})


def search_topic(request):
    form = TopicSearchForm(request.GET)
    if form.is_valid():
        title = form.cleaned_data.get("title")
        topic = Topic.objects.filter(title__contains=title)
        return render(request, 'topic_list.html', context={"topic": topic})
    else:
        return render(request, 'search_topic.html', context={"form": form})


def search_topic_form(request):
    return render(request, 'search_topic.html', context={'form': TopicSearchForm()})
