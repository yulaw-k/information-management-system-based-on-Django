from django import forms
from .models import PersonInfo, Schedule


class PersonInfoForm(forms.ModelForm):
    class Meta:
        model = PersonInfo
        fields = '__all__'
        labels = {
            'id': ' 学号',
            'name': '姓名',
            'major': '专业',
            'sex': '性别',
            'number': '手机号',
            'age': '年龄',
            'address': '家庭地址',
        }


class ScheduleForm(forms.ModelForm):

    class Meta:
        model = Schedule
        labels = {
            'title': '标题',
            'content': '内容',
            'beginDate': '开始时间',
            'endDate': '结束时间',
        }
        exclude = ['person']
        field_classes = {
            'beginDate': forms.DateField,
            'endDate': forms.DateField
        }
        help_texts = {
            'title': '请输入标题名称'
        }