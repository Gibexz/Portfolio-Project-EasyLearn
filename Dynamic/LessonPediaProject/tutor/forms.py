from django import forms
from django_countries.fields import countries
from django_flatpickr.widgets import DatePickerInput
from .models import Tutor, Day, TimeSlot


class TutorScheduleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Change the default label for empty option in dropdowns
        self.fields['day'].empty_label = 'Select Day'
        self.fields['from_hour'].empty_label = 'Select Time'
        self.fields['to_hour'].empty_label = 'Select Time'

        self.fields['day'].widget.attrs['class'] = 'day_field'
        self.fields['day'].widget.attrs['id'] = 'dayField'

        self.fields['from_hour'].widget.attrs['class'] = 'from_hour'
        self.fields['from_hour'].widget.attrs['id'] = 'fromHour'

        self.fields['to_hour'].widget.attrs['class'] = 'to_hour'
        self.fields['to_hour'].widget.attrs['id'] = 'toHour'

    class Meta:
        model = TimeSlot
        fields = ['day', 'from_hour', 'to_hour']


class TutorUpdateForm(forms.ModelForm):
    """Tutor update form"""
    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()

        return instance
    institution_type = forms.ChoiceField(
        choices=[
        ('--select one--', '--select one--'),
        ('University', 'University'),
        ('Polytechnic', 'Polytechnic'),
        ('College Of Education', 'College Of Education'),
        ('Vocational', 'Vocational'),
        ('Others', 'Others'),

        ],
        widget=forms.Select(attrs={
            'class': 'no_outline',
            'id': 'institution_type',
        })
    )

    institution = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'id': 'institution',
            'placeholder': 'top-most institution attended',
        })
    )

    discipline = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'id': 'dis',
            'placeholder': 'What\'s your discipline?',
        })
    )

    highest_qualification = forms.ChoiceField(
        choices=[
            ('--select one--', '--select one--'),
            ('Phd', 'Phd'),
            ('Msc', "Msc"),
            ('BED', 'BED'),
            ('BSC', 'BSC'),
            ('BENG', 'BENG'),
            ('HND', 'HND'),
            ('OND', 'OND'),
            ('NCE', 'NCE'),
            ('SSCE', 'SSCE'),
            ('Others', 'Others')
        ],
        widget=forms.Select(attrs={
            'id': 'qual',
        })
    )

    result = forms.ChoiceField(
        choices=[
            ('', '-- Select One --'),
            ('First Class', 'First Class'),
            ('Distinction', 'Distinction'),
            ('Second Class Upper', 'Second Class Upper'),
            ('Upper credit', 'Upper credit'),
            ('Second Class Lower', 'Second Class Lower'),
            ('Lower credit', 'Lower credit'),
            ('Others', 'Others'),
        ],
        widget=forms.Select(attrs={
            'class': 'no_outline',
            'id': 'degree_class',
        })
    )

    employment_status = forms.ChoiceField(
        choices=[
            ('', '--select one--',),
            ('Employed', 'Employed'),
            ('Self Employed', 'Self Employed'),
            ('Unemployed', 'Unemployed'),
        ],
        widget=forms.Select(attrs={
            'class': 'no_outline',
            'id': 'empStat',
        })
    )

    employment_type = forms.ChoiceField(
        choices=[
        ('--select one--', '--select one--'),
        ('Full Time', 'Full Time'),
        ('Part Time', 'Part Time'),
        ('Freelance', 'Freelance'),
        ('Others', 'Others'),
        ],
        required=False,
        widget=forms.Select(attrs={
            'class': 'no_outline',
            'id': 'employmentStat',
        })
    )
#     date_of_birth = forms.DateField(
#     widget=DatePickerInput(
#         attrs={
#             'class': 'no_outline',
#             'id': 'dob',
#             'placeholder': 'Format: (MM/DD/YYYY)',
#         }
#     )
# )

    nationality = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'nationality',
        })
    )


    # nationality = forms.CharField(
    #     widget=forms.CharField(choices=countries),
    #     required=True
    # )



    # state_of_residence = forms.ChoiceField(
    #     choices=[
    #         ('', '- Select -'),
    #         ('Abia', 'Abia'), ('Adamawa', 'Adamawa'), ('AkwaIbom', 'AkwaIbom'),
    #         ('Anambra', 'Anambra'), ('Bauchi', 'Bauchi'), ('Bayelsa', 'Bayelsa'),
    #         ('Benue', 'Benue'), ('Borno', 'Borno'), ('Cross River', 'Cross River'),
    #         ('Delta', 'Delta'), ('Ebonyi', 'Ebonyi'), ('Edo', 'Edo'),
    #         ('Ekiti', 'Ekiti'), ('Enugu', 'Enugu'), ('FCT', 'FCT'),
    #         ('Gombe', 'Gombe'), ('Imo', 'Imo'), ('Jigawa', 'Jigawa'),
    #         ('Kaduna', 'Kaduna'), ('Kano', 'Kano'), ('Katsina', 'Katsina'),
    #         ('Kebbi', 'Kebbi'), ('Kogi', 'Kogi'), ('Kwara', 'Kwara'),
    #         ('Lagos', 'Lagos'), ('Nasarawa', 'Nasarawa'), ('Niger', 'Niger'),
    #         ('Ogun', 'Ogun'), ('Ondo', 'Ondo'), ('Osun', 'Osun'),
    #         ('Oyo', 'Oyo'), ('Plateau', 'Plateau'), ('Rivers', 'Rivers'),
    #         ('Sokoto', 'Sokoto'), ('Taraba', 'Taraba'), ('Yobe', 'Yobe'),
    #         ('Zamfara', 'Zamafara'),
    #     ],
    #     widget=forms.Select(attrs={
    #         'class': 'select-option no_outline',
    #         'id': 'state',
    #         'onchange': 'toggleLGA(this);',
    #     })
    # )

    # state_of_residence = forms.CharField(
    #     widget=forms.TextInput(attrs={
    #         'class': 'state_of_residence',
    #         'id': 'state',
    #     })
    # )

    highest_qualification_cert = forms.FileField(
        required=False,
        widget=forms.FileInput(attrs={
            'id': 'cert',
            'placeholder': 'upload certificate',
            'class': 'file_button'
        })
    )

    cv_id = forms.FileField(
        required=False,
        widget=forms.FileInput(attrs={
            'id': 'cv',
            'placeholder': 'upload cv',
            'class': 'file_button'
        })
    )

    profile_picture = forms.ImageField(
        widget=forms.FileInput(attrs={
            'id': 'pic',
            'placeholder': 'upload profile picture',
            'class': 'file_button'
        })
    )

    gender = forms.ChoiceField(
        choices=[
            ('', '- Select -'),
            ('Male', 'Male'),
            ('Female', 'Female'),
        ],
        widget=forms.Select(attrs={
            'id': 'gender2',
            'class': 'no_outline',
        })
    )
    open_to_work = forms.ChoiceField(
        choices=Tutor.open_to_work_choice,
        widget=forms.Select(attrs={
            'id': 'open_to_work',
            'class': 'no_outline',
        })
    )


    class Meta:
        model = Tutor
        fields = [
                'first_name', 'last_name', 'others', 'phone_number', 'highest_qualification',
                'area_of_specialization', 'discipline', 'employment_status','employment_type','nationality',
                'state_of_residence', 'institution_type', 'institution', 'result',
                'residential_address', 'cv_id', 'highest_qualification_cert', 'profile_picture', 'gender', 'open_to_work'

            ]
        widgets = {
            'first_name': forms.TextInput(attrs={
                'name': 'first_name',
                'placeholder': 'enter first name',
                'id': 'first_name',
                'autocomplete': 'on'

            }),
            'last_name': forms.TextInput(attrs={
                'name': 'last_name',
                'placeholder': 'enter last name',
                'id': 'last_name',
                'autocomplete': 'on',
            }),
            'others': forms.TextInput(attrs={
                'name': 'others',
                'placeholder': 'enter other names',
                'required': False,
                'id': 'others',
                'autocomplete': 'on',
            }),
            'phone_number': forms.TextInput(attrs={
                'name': 'phone_number',
                'placeholder': '+234xxxxxxxxxx',
                'id': 'phone_number'
            }),

            'area_of_specialization': forms.TextInput(attrs={
                'name': 'area_of_specialization',
                'placeholder': 'enter area of specialization',
                'id': 'area_of_specialization',
                'required': False,
                'autocomplete': 'on',
            }),
            'residential_address': forms.TextInput(attrs={
                'name': 'residential_address',
                'placeholder': 'enter residential address',
                'id': 'residential_address',
                'autocomplete': 'on',
            }),
            'state_of_residence': forms.TextInput(attrs={
                'name': 'state_of_residence',
                'placeholder': 'enter state of residence',
                'id': 'state',
                'autocomplete': 'on',
            })
        }

