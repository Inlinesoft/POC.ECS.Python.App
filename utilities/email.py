import smtplib
import definitions

class Email:
    """
    Send out emails (with or without attachments) using this class.

    Usage:
    With attachment
    email = Email(server_name)
    email.send_mail(send_from, send_to, subject, text, files)

    Without attachment
    email = Email()
    email.send_mail(send_from, send_to, subject, text)
    """

    # variable
    _user_name = None
    _server = None

    # methods
    def __init__(self):
        """
        This method initialises the local variable
        :return: none
        """

        # Initialize the User name
        self._server = smtplib.SMTP(definitions.EMAIL_PRIMARY_SMTP_ADDRESS, 587)
        self._user_name = definitions.EMAIL_ACCOUNT_USERNAME
        self._password = definitions.EMAIL_ACCOUNT_PASSWORD

        self._server = smtplib.SMTP('smtp.gmail.com')
        self._server.ehlo()
        self._server.starttls()

        self._server.login(self._user_name, self._password)


    def __str__(self):
        """
        This is to return the calss name, which will can be used
            to pass to the logging methods
        :return: A string with class details
        """
        ret_data = f"<<{self.__class__.__name__}>> :: "

        return ret_data

    def set_user_name(self, user_name):
        """
        setter method for user_name
        :param user_name:
        :return:
        """
        self._user_name = user_name

    def get_user_name(self):
        """
        getter method for username
        :param user_name:
        :return:
        """
        return self._user_name

    def set_password(self, password):
        """
        setter method for password
        :param password:
        :return:
        """
        self._password = password

    def get_password(self):
        """
        getter method for password
        :param password:
        :return:
        """
        return self._password

    def set_smtp_server(self, value):
        """
        setter method for server
        :param value:
        :return:
        """
        self._server = value

    def get_smtp_server(self):
        """
        getter method for smtp server
        :return:
        """
        return self._server


    def send_mail_using_smtp(self, send_from, send_to, subject, text, files=None, text_type='text'):
        """
        Send mail sends out email to list of email participants

        :param send_from:
        :param send_to:
        :param subject:
        :param text:
        :param files:
        :param server:
        :return:
        """

        is_email_sent = True

        try:
            body = '\r\n'.join(['To: %s' % send_to,
                                'From: %s' % send_from,
                                'Subject: %s' % subject,
                                '', text])
            self._server.sendmail(send_from, send_to, body)

        except Exception as exp:
            raise (exp)

        return is_email_sent
