reset_password = """
Dear {{ user.username }},

To reset your password, click on the following link:

{{ url_for('home.reset_password', token=token, _external=True) }}

If you have not requested a password reset, simply ignore this message.


Sincerely,

The Goose Or Not Team
"""
