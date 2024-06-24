# Generated documentation for module arcpy.management


class CreateRole(object):
    """
    Creates a database role, allowing you to add users to or remove them from the role.
    """

    @property
    def description(self) -> str:
        return """

        CreateRole_management(input_database, role, {grant_revoke}, {user_name})

        Creates a database role, allowing you to add users to or remove them
        from the role.

     INPUTS:
      input_database (Workspace):
          The connection file to a database or enterprise geodatabase. Connect
          as a database administrator user.
      role (String):
          The name of the database role to create. If it's an existing role,
          type the name for the role you want to add users to or remove them
          from.
      grant_revoke {String}:
          Specifies whether the role will be added to a user or list of users or
          a user or list of users will be removed from the role.GRANT-The role
          will be granted to the specified user or users, making
          them a member of the role. This is the default.REVOKE-The role will be
          revoked from the specified user or users,
          removing them from the role.
      user_name {String}:
          The name of the user whose role membership will change. To specify
          multiple users, type the user names separated by commas (no spaces).

        """