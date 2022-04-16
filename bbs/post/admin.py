from django.contrib import admin
from post.models import Topic, Comment
# Register your models here.

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    # 动作（批量上线或下线）
    actions = ['topic_online', 'topic_offline']

    def topic_online(self, request, queryset):
        row_update = queryset.update(is_online=True)
        self.message_user(request, "{} is online".format(row_update))
    
    topic_online.short_description = "上线所选的 {}".format(Topic._meta.verbose_name)

    def topic_offline(self, request, queryset):
        row_update = queryset.update(is_online=False)
        self.message_user(request, "{} is offline".format(row_update))

    topic_offline.short_description = "下线所选的 {}".format(Topic._meta.verbose_name)

    # 展示模型，不仅可以展示模型属性，也可以根据函数返回内容进行展示
    list_display = ['topic_title', 'topic_content', 'topic_is_online', 'topic_user', 'topic_createtime']

    def topic_is_online(self, obj):
        return '是' if obj.is_online else '否'
    topic_is_online.short_description = '话题是否在线'

    def topic_content(self, obj):
        return obj.content[:30]
    topic_content.short_description = '话题内容'

    def topic_title(self, obj):
        return obj.title
    topic_title.short_description = '话题标题'

    def topic_user(self, obj):
        return obj.user
    topic_user.short_description = '作者'

    def topic_createtime(self, obj):
        return obj.createtime
    topic_createtime.short_description = '创建时间'
    # 搜素列
    search_fields = ['title', 'user__username']
    # 过滤列
    list_filter = ['title', 'user__username']
    # 排序列
    ordering = ['id']
    # 分页展示
    list_per_page = 1
    list_max_show_all = 2
    # 详情列展示
    fields = [('user', 'title'), 'content', 'is_online']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['comment_content', 'comment_topic', 'comment_up', 'comment_down', 'comment_createtime']

    def comment_content(self, obj):
        return obj.content
    comment_content.short_description = '评论内容'

    def comment_topic(self, obj):
        return obj.topic.title
    comment_topic.short_description = '话题标题'

    def comment_up(self, obj):
        return obj.up
    comment_up.short_description = '支持'

    def comment_down(self, obj):
        return obj.down
    comment_down.short_description = '反对'

    def comment_createtime(self, obj):
        return obj.createtime
    comment_createtime.short_description = '创建时间'
    search_fields = ['content', 'topic']
    list_filter = ['content', 'topic']
    fields = ['topic', 'content',('up', 'down')]
