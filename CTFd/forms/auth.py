from wtforms import PasswordField, StringField, SelectField, BooleanField
from wtforms.fields.html5 import EmailField
from wtforms.validators import InputRequired

from CTFd.forms import BaseForm
from CTFd.forms.fields import SubmitField
from CTFd.forms.users import (
    attach_custom_user_fields,
    attach_registration_code_field,
    build_custom_user_fields,
    build_registration_code_field,
)

services = [
"DG/DG",
"SG/SG",
"SG/MJ",
"SG/SAFCG",
"SG/SAM",
"SG/SILOG",
"DP/DP",
"DP/PEPS",
"DP/SPRI",
"DP/SPP",
"DP/SDPU",
"DP/DR",
"DSI/DSI",
"DSI/SOI",
"DSI/SDM",
"DSI/SIMV",
"ENSG/ENSG",
"ENSG/SE",
"ENSG/SMG",
"DOT/DOT",
"DOT/SIS",
"DOT/SGM",
"DOT/SISFE",
"DOT/SIA",
"DOT/SV3D",
"DOT/SVRP",
"DOT/DT-CE",
"DOT/DT-NOM",
"DOT/DT-GO",
"DOT/DT-SE",
"DOT/DT-SO",
"DRH/DRH",
"DRH/SREF",
"DRH/SPER",
"DRH/SASP",
"DIRCOM/DIRCOM",
"AC/AC",
]

sites= ['Saint Mandé',
        'Marne-La-Vallée',
        'Lyon',
        'Lille',
        'Nantes',
        'Hérouville-Saint-Clair',
        'Caen',
        'Aix-En-Provence',
        'Champigneulles',
        'Saint-Médard-En-Jalles',
        'Ramonville-St-Agne',
        'Tillé',
        'Nogent-Sur-Vernisson',
        'Villefranche-Sur-Cher',
        'Autre']


def RegistrationForm(*args, **kwargs):
    class _RegistrationForm(BaseForm):
        name = StringField(
            "Nom", validators=[InputRequired()], render_kw={"autofocus": True}
        )
        surname = StringField("Prénom", validators=[InputRequired()])
        gender = SelectField(u'Genre', choices=[('H'), ('F'), ('')])
        email = EmailField("Email", validators=[InputRequired()])
        password = PasswordField("Mot de passe", validators=[InputRequired()])
        site = SelectField(u'Site', choices=sites)
        service = SelectField(u'Service', choices=services)
        cellphone = StringField("Téléphone")
        as_member = BooleanField("Membre AS")
        submit = SubmitField("Inscription")

        @property
        def extra(self):
            return build_custom_user_fields(
                self, include_entries=False, blacklisted_items=()
            ) + build_registration_code_field(self)

    attach_custom_user_fields(_RegistrationForm)
    attach_registration_code_field(_RegistrationForm)

    return _RegistrationForm(*args, **kwargs)


class LoginForm(BaseForm):
    email = StringField(
        "Email",
        validators=[InputRequired()],
        render_kw={"autofocus": True},
    )
    password = PasswordField("Mot de passe", validators=[InputRequired()])
    submit = SubmitField("Connexion")


class ConfirmForm(BaseForm):
    submit = SubmitField("Réenvoyer la confirmation par email")


class ResetPasswordRequestForm(BaseForm):
    email = EmailField(
        "Email", validators=[InputRequired()], render_kw={"autofocus": True}
    )
    submit = SubmitField("Confirmer")


class ResetPasswordForm(BaseForm):
    password = PasswordField(
        "Mot de passe", validators=[InputRequired()], render_kw={"autofocus": True}
    )
    submit = SubmitField("Confirmer")
