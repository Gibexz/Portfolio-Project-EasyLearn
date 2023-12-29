from django import forms
from django_countries.fields import countries
from django_flatpickr.widgets import DatePickerInput
from .models import Tutor

class TutorUpdateForm(forms.ModelForm):
    """Tutor update form"""
    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()

        return instance
    institution_type = forms.ChoiceField(
        choices=[
            ('', '-- Select One --'),
            ('university', 'University'),
            ('polytechnic', 'Polytechnic'),
            ('COE', 'College Of Education'),
            ('vocational', 'Vocational'),
            ('others', 'Others'),
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
            ('', '-- Select One --'),
            ('Phd', 'Phd'),
            ('Msc', 'Msc'),
            ('Bsc', 'Bsc'),
            ('Beng', 'Beng'),
            ('Hnd', 'Hnd'),
            ('ND', 'ND'),
            ('NCE', 'NCE'),
            ('Waec', 'Waec'),
            ('Others', 'Others')
        ],
        widget=forms.Select(attrs={
            'class': 'no_outline',
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
        ('full_time', 'Full Time'),
        ('part_time', 'Part Time'),
        ('freelance', 'Freelance'),
        ('others', 'Others'),
        ],
        widget=forms.Select(attrs={
            'class': 'no_outline',
            'id': 'employmentStat',
        })
    )
    date_of_birth = forms.DateField(
    widget=DatePickerInput(
        attrs={
            'class': 'no_outline',
            'id': 'dob',
            'placeholder': 'Format: (dd/mm/yyyy)',
        }
    )
)


    nationality = forms.CharField(
        widget=forms.Select(choices=countries),
        required=True
    )


    
    state_of_residence = forms.ChoiceField(
        choices=[
            ('', '- Select -'),
            ('Abia', 'Abia'), ('Adamawa', 'Adamawa'), ('AkwaIbom', 'AkwaIbom'),
            ('Anambra', 'Anambra'), ('Bauchi', 'Bauchi'), ('Bayelsa', 'Bayelsa'),
            ('Benue', 'Benue'), ('Borno', 'Borno'), ('Cross River', 'Cross River'),
            ('Delta', 'Delta'), ('Ebonyi', 'Ebonyi'), ('Edo', 'Edo'),
            ('Ekiti', 'Ekiti'), ('Enugu', 'Enugu'), ('FCT', 'FCT'),
            ('Gombe', 'Gombe'), ('Imo', 'Imo'), ('Jigawa', 'Jigawa'),
            ('Kaduna', 'Kaduna'), ('Kano', 'Kano'), ('Katsina', 'Katsina'),
            ('Kebbi', 'Kebbi'), ('Kogi', 'Kogi'), ('Kwara', 'Kwara'),
            ('Lagos', 'Lagos'), ('Nasarawa', 'Nasarawa'), ('Niger', 'Niger'),
            ('Ogun', 'Ogun'), ('Ondo', 'Ondo'), ('Osun', 'Osun'),
            ('Oyo', 'Oyo'), ('Plateau', 'Plateau'), ('Rivers', 'Rivers'),
            ('Sokoto', 'Sokoto'), ('Taraba', 'Taraba'), ('Yobe', 'Yobe'),
            ('Zamfara', 'Zamafara'),
        ],
        widget=forms.Select(attrs={
            'class': 'select-option no_outline',
            'id': 'state',
            'onchange': 'toggleLGA(this);',
        })
    )

    
    certificate = forms.FileField(
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
        required=False,
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
            'id': 'gender',
            'class': 'no_outline',
        })


    )

    class Meta:
        model = Tutor
        fields = [
                'first_name', 'last_name', 'others', 'phone_number', 'highest_qualification', 
                'area_of_specialization', 'discipline', 'employment_status','employment_type','nationality',
                'state_of_residence', 'institution_type', 'institution', 'result', 
                'residential_address', 'cv_id', 'certificate', 'profile_picture', 'gender',
                'date_of_birth',
                
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
        }
                
