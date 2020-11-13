from django.forms import ModelForm

from company.models import Company


class EditForm(ModelForm):

    class Meta:
        model = Company
        fields = ('name', 'owner')

    def save(self, commit=True):
        # if self.is_valid():

        company = super().save(commit=False)

        import ipdb; ipdb.set_trace()
