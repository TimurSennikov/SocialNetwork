import secrets
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from django.utils.html import strip_tags


class AccountVerificationEmail(EmailMultiAlternatives):
    subject_template = "Code entering: {code}"
    html_template = "templates/emails/verification_email.html"

    def __init__(self, to_email, code=None, **kwargs):
        self.code = code or self._generate_code()
        subject = self.subject_template.format(code=self.code)

        context = {
            "code": self.code,
            "user_email": to_email,
        }

        html_content = render_to_string(self.html_template, context)
        text_content = strip_tags(html_content)

        super().__init__(
            subject=subject,
            body=text_content,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[to_email],
            **kwargs
        )

        self.attach_alternative(html_content, "text/html")

    @staticmethod
    def _generate_code():
        """Generate cryptographically secure 6-digit code (000001 to 999999)."""
        return str(secrets.randbelow(999999) + 1).zfill(6)

    def get_code(self):
        return self.code