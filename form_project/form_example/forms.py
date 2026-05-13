from django import forms
from django.core.exceptions import ValidationError
from .models import Publisher


class ExampleForm(forms.Form):
    """Form class for input:
        :text,
    :password"""

    BOOK_CHOICES = (
        ("1", "Deep Learning with Keras"),
        ("2", "Web Development with Django"),
        ("3", "Brave New World"),
        ("4", "The Great Gatsby"),
    )
    text_input = forms.CharField(help_text="Введите текст здесь")
    password_input = forms.CharField(
        widget=forms.PasswordInput, help_text="Введите ваш пароль."
    )
    checkbox_on = forms.BooleanField()
    favorite_book = forms.ChoiceField(choices=BOOK_CHOICES)
    books_you_own = forms.MultipleChoiceField(choices=BOOK_CHOICES)
    text_area = forms.CharField(widget=forms.Textarea)
    integer_input = forms.IntegerField()
    float_input = forms.FloatField()
    decimal_input = forms.DecimalField()
    date_input = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    hidden_input = forms.CharField(widget=forms.HiddenInput, initial="Hidden Value")


class ExampleChoiceForm(forms.Form):
    """Class choice form radio input"""

    RADIO_CHOICES = (
        ("Value One", "Value One"),
        ("Value Two", "Value Two"),
        ("Value Three", "Value Three"),
    )
    radio_input = forms.ChoiceField(choices=RADIO_CHOICES)


def validate_email_domain(value):
    if value.split("@")[-1].lower() != "example.com":
        raise ValidationError("The email address " "must be on the domain example.com.")


class OrderForm(forms.Form):
    magazine_count = forms.IntegerField(
        min_value=0,
        max_value=80,
        widget=forms.NumberInput(attrs={"placeholder": "Number of Magazines"}),
    )
    book_count = forms.IntegerField(
        min_value=0,
        max_value=50,
        widget=forms.NumberInput(attrs={"placeholder": "Number of Books"}),
    )
    send_confirmation = forms.BooleanField(required=False)
    email = forms.EmailField(
        required=False,
        validators=[validate_email_domain],
        widget=forms.EmailInput(attrs={"placeholder":"Your company email address"})
    )

    def clean(self):
        cleaned_data = super().clean()
        item_total = cleaned_data.get("magazine_count", 0) + cleaned_data.get(
            "book_count", 0
        )
        if item_total > 100:
            self.add_error(None, "The total number of items must be " "100 or less.")
        if cleaned_data["send_confirmation"] and not cleaned_data.get("email"):
            self.add_error(
                "email",
                "Please enter an email address to " "receive the confirmation message.",
            )
        elif cleaned_data.get("email") and not cleaned_data["send_confirmation"]:
            self.add_error(
                "send_confirmation",
                "Please check this if you want to " " receive a confirmation email.",
            )


class ExampleFormField(forms.Form):
    text_field = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Text Placeholder"})
    )
    password_field = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Passowrd Placeholder"})
    )
    email_field = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder": "Email Placeholder"})
    )
    text_area = forms.CharField(
        widget=forms.Textarea(attrs={"placeholder": "Text Area Placeholder"})
    )


class FormTest(forms.Form):
    text_field = forms.CharField()
    email_field = forms.EmailField()

class PublisherForm(forms.ModelForm):
    email_on_save = forms.BooleanField(required=False, help_text="Send notification email on save")
    class Meta:
        model= Publisher
        fields = ("name", "website", "email")
        widgets = {
            "name": forms.TextInput(
                attrs={"placeholder": "The publisher's name."}
            ),
            "website": forms.URLInput(
                attrs={"placeholder": "Your company website address"}
            )
        }
