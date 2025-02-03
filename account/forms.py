from django import forms
from django.contrib.auth.models import User

# Create your forms here.


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email", "password"]

    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(
        widget=forms.PasswordInput, label="Confirm Password"
    )

    # validate user input
    def clean(self):
        cleaned_data = super().clean()
        # checks if the "password" field matches the "password_confirm" field.
        if cleaned_data.get("password") != cleaned_data.get("password_confirm"):
            self.add_error("password_confirm", "Passwords do not match")
        return cleaned_data
