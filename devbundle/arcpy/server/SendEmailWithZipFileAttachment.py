# Generated documentation for module arcpy.server


class SendEmailWithZipFileAttachment(object):
    """
    Emails a file to an email address using an SMTP email server.
    """

    @property
    def description(self) -> str:
        return """

        SendEmailWithZipFileAttachment_server(To, From, Subject, Text, Zip_File, Max_File_Size__MB_, SMTP_Email_Server, {User}, {Password})

        Emails a file to an email address using an SMTP email server.

     INPUTS:
      To (String):
          The email address of the recipient.
      From (String):
          The email address of the sender.
      Subject (String):
          The text in the subject line of the email.
      Text (String):
          The body text of the email.
      Zip_File (File):
          The file to be attached to the email.
      Max_File_Size__MB_ (Long):
          The maximum allowable size of an attachment.If you don't know what to
          use for Max File Size, check the attachment
          size limit of your SMTP mail server and the recipient email provider.
      SMTP_Email_Server (String):
          The SMTP email server that will deliver the email.
      User {String}:
          The user which will log in to the SMTP email server.
      Password {String}:
          The user password used to connect to the SMTP email server (if
          necessary).

        """