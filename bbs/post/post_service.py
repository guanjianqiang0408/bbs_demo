from post.models import Comment


def build_topic_base_info(topic):
    return {
        "id": topic.id,
        "title": topic.title,
        "user": topic.user.username,
        "create_time": topic.createtime.strftime("%Y-%m-%d %H:%M:%S")
    }


def build_comment_info(comment):
    return {
        "id": comment.id,
        "content": comment.content,
        "up": comment.up,
        "down": comment.down,
        "create_time": comment.createtime.strftime("%Y-%m-%d %H:%M:%S"),
        "last_modified": comment.last_modified.strftime("%Y-%m-%d %H:%M:%S")
    }


def build_topic_detail_info(topic):
    comments = Comment.objects.filter(topic=topic)
    return {
        "id": topic.id,
        "title": topic.title,
        "content": topic.content,
        "user": topic.user.username,
        "create_time": topic.createtime.strftime("%Y-%m-%d %H:%M:%S"),
        "last_modified": topic.last_modified.strftime("%Y-%m-%d %H:%M:%S"),
        "comments": [build_comment_info(comment) for comment in comments]
    }


def add_comment_to_topic(topic, content):
    return Comment.objects.create(topic=topic, content=content)
