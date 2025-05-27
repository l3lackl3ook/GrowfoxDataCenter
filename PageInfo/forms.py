from django import forms
from .models import PageGroup

class PageURLForm(forms.Form):
    url = forms.URLField(
        label="Page URL",
        widget=forms.URLInput(attrs={
            'class': 'form-control form-control-lg',  # ใส่ขนาด input ใหญ่เหมือนหน้า add_page
            'placeholder': 'Input URL Page'
        })
    )

class PageGroupForm(forms.ModelForm):
    class Meta:
        model = PageGroup
        fields = ['group_name']
        widgets = {
            'group_name': forms.TextInput(attrs={
                'class': 'form-control form-control-lg',  # เพิ่ม form-control-lg เพื่อให้ input ใหญ่เหมือน add_page
                'placeholder': 'Input Group Name'
            }),
        }

