from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from django.utils.html import strip_tags

class AccauntVerificationEmail(EmailMultiAlternatives):
    subject_templates = "Enter code: {code}"
    html_template = "templates/emails/verification_email.html"

    def __init__(self, to_email, code ,**kwargs):
        self.code = code 
        self.subject = self.subject_templates.format(code=code)

        context = {
            "code": code,
            "user_email": to_email,
        }

        html_content = render_to_string(self.html_template, context)

        text_content = strip_tags(html_content)

        super().__init__(
            subject=self.subject,
            body=text_content,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[to_email]
            **kwargs
        )

        self.attach_alternative(html_content, "text/html")
        return  self.__init__