from django.core.exceptions import ValidationError

def validar_pdf(value):
    if not value.name.lower().endswith('.pdf'):
        raise ValidationError('El archivo debe ser un documento PDF.')
