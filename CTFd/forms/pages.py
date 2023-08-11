from wtforms import (
    BooleanField,
    HiddenField,
    MultipleFileField,
    SelectField,
    StringField,
    TextAreaField,
)
from wtforms.validators import InputRequired

from CTFd.forms import BaseForm


class PageEditForm(BaseForm):
    title = StringField(
        "Titre", description="This is the title shown on the navigation bar"
    )
    route = StringField(
        "Route",
        description="This is the URL route that your page will be at (e.g. /page). You can also enter links to link to that page.",
    )
    draft = BooleanField("Brouillon")
    hidden = BooleanField("Caché")
    auth_required = BooleanField("Authentication Nécessaire")
    content = TextAreaField("Contenu")
    format = SelectField(
        "Format",
        choices=[("markdown", "Markdown"), ("html", "HTML")],
        default="markdown",
        validators=[InputRequired()],
        description="The markup format used to render the page",
    )


class PageFilesUploadForm(BaseForm):
    file = MultipleFileField(
        "Upload Files",
        description="Attach multiple files using Control+Click or Cmd+Click.",
        validators=[InputRequired()],
    )
    type = HiddenField("Page Type", default="page", validators=[InputRequired()])
