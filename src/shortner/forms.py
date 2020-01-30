from django import forms
from .validator import validate_dot_com, validator_url
class SubmitUrlForm(forms.Form):
    url = forms.CharField(label = '',
                          validators=[validator_url],
                          widget= forms.TextInput(
                              attrs ={"placeholder":"Long URL",
                                      "class":"form-control"
                                      }
                          )
                        )