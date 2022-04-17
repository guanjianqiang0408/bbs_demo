from django import forms


class TopicSearchForm(forms.Form):
    title = forms.CharField(label="话题标题")
