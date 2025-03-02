from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'FirstName': forms.TextInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded'}),
            'LastName': forms.TextInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded'}),
            'Email': forms.EmailInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded'}),
            'DateOfBirth': forms.DateInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded', 'type': 'date'}),
            'Course': forms.TextInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded'}),
            'EnrollmentDate': forms.DateInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded', 'type': 'date'}),
        }