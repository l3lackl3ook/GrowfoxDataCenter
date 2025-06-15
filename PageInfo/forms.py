from django import forms
from .models import PageGroup

class PageURLForm(forms.Form):
<<<<<<< HEAD
    url = forms.URLField(
        label="Page URL",
        widget=forms.URLInput(attrs={
            'class': 'form-control form-control-lg',  # ใส่ขนาด input ใหญ่เหมือนหน้า add_page
=======
    PLATFORM_CHOICES = [
        ('facebook', 'Facebook'),
        ('tiktok', 'TikTok'),
        ('instagram', 'Instagram'),
        ('lemon8', 'Lemon8'),
        ('youtube', 'Youtube'),
    ]
    platform = forms.ChoiceField(
        choices=PLATFORM_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-control form-control-lg',
        }),
        required=True,  # บังคับเลือก platform
        label="Platform"
    )
    url = forms.URLField(
        label="Page URL",
        widget=forms.URLInput(attrs={
            'class': 'form-control form-control-lg',
>>>>>>> bee78e8f8b34bfc8e75e08ac77a3a7df56667643
            'placeholder': 'Input URL Page'
        })
    )

class PageGroupForm(forms.ModelForm):
    class Meta:
        model = PageGroup
        fields = ['group_name']
        widgets = {
            'group_name': forms.TextInput(attrs={
<<<<<<< HEAD
                'class': 'form-control form-control-lg',  # เพิ่ม form-control-lg เพื่อให้ input ใหญ่เหมือน add_page
                'placeholder': 'Input Group Name'
            }),
        }

=======
                'class': 'form-control form-control-lg',
                'placeholder': 'Input Group Name'
            }),
        }
>>>>>>> bee78e8f8b34bfc8e75e08ac77a3a7df56667643
