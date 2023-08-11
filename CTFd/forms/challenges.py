from wtforms import MultipleFileField, SelectField, StringField
from wtforms.validators import InputRequired

from CTFd.forms import BaseForm
from CTFd.forms.fields import SubmitField


class ChallengeSearchForm(BaseForm):
    field = SelectField(
        "Champ de recherche",
        choices=[
            ("name", "Name"),
            ("id", "ID"),
            ("category", "Category"),
            ("type", "Type"),
        ],
        default="name",
        validators=[InputRequired()],
    )
    q = StringField("Parameter", validators=[InputRequired()])
    submit = SubmitField("Chercher")


class ChallengeFilesUploadForm(BaseForm):
    file = MultipleFileField(
        "Upload Files",
        description="Attach multiple files using Control+Click or Cmd+Click.",
        validators=[InputRequired()],
    )
    submit = SubmitField("Upload")
