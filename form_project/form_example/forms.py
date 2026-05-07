from django import forms

class ExampleForm(forms.Form):
    """ Form class for input: 
        :text, 
    :password"""
    BOOK_CHOICES = (
        ("1", "Deep Learning with Keras"),
        ("2", "Web Development with Django"),
        ("3", "Brave New World"),
        ("4", "The Great Gatsby"),
    )
    text_input = forms.CharField(help_text="Введите текст")
    password_input = forms.CharField(
        widget=forms.PasswordInput,
        help_text="Введите ваш пароль."
    )
    checkbox_on = forms.BooleanField()
    favorite_book = forms.ChoiceField(choices=BOOK_CHOICES)
    books_you_own = forms.MultipleChoiceField(choices=BOOK_CHOICES)
    text_area = forms.CharField(widget=forms.Textarea)
    integer_input = forms.IntegerField()
    float_input = forms.FloatField()
    decimal_input = forms.DecimalField()
    date_input = forms.DateField(widget=forms.DateInput(
        attrs={"type":"date"}
    ))
    hidden_input = forms.CharField(widget=forms.HiddenInput, initial="Hidden Value")

class ExampleChoiceForm(forms.Form):
    """ Class choice form radio input """
    RADIO_CHOICES = (
        ("Value One", "Value One"),
        ("Value Two", "Value Two"),
        ("Value Three", "Value Three")
    )
    radio_input = forms.ChoiceField(choices=RADIO_CHOICES)
