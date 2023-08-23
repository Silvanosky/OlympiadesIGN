from flask import session
from wtforms import PasswordField, SelectField, StringField, SelectMultipleField, BooleanField
from wtforms.fields.html5 import DateField, URLField

from CTFd.forms import BaseForm
from CTFd.forms.fields import SubmitField
from CTFd.forms.users import attach_custom_user_fields, build_custom_user_fields
from CTFd.utils.countries import SELECT_COUNTRIES_LIST
from CTFd.utils.user import get_current_user


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


def SettingsForm(*args, **kwargs):
    class _SettingsForm(BaseForm):
        name = StringField("Nom")
        surname = StringField("Prénom")
        gender = SelectField(u'Genre', choices=[('H'), ('F'), ('')])
        email = StringField("Email")
        password = PasswordField("Mot de passe")
        confirm = PasswordField("Mot de passe actuel")
        service = SelectField(u'Service', choices=services)
        site = SelectField(u'Site', choices=sites)
        cellphone = StringField("Téléphone")
        as_member = BooleanField("Membre AS")
        submit = SubmitField("Confirmer")

        @property
        def extra(self):
            fields_kwargs = _SettingsForm.get_field_kwargs()
            return build_custom_user_fields(
                self,
                include_entries=True,
                fields_kwargs=fields_kwargs,
                field_entries_kwargs={"user_id": session["id"]},
            )

        @staticmethod
        def get_field_kwargs():
            user = get_current_user()
            field_kwargs = {"editable": True}
            if user.filled_all_required_fields is False:
                # Show all fields
                field_kwargs = {}
            return field_kwargs

    field_kwargs = _SettingsForm.get_field_kwargs()
    attach_custom_user_fields(_SettingsForm, **field_kwargs)

    return _SettingsForm(*args, **kwargs)


class TokensForm(BaseForm):
    expiration = DateField("Expiration")
    submit = SubmitField("Generate")
