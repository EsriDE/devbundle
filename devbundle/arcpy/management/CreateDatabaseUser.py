# Generated documentation for module arcpy.management


class CreateDatabaseUser(object):
    """
    Creates a database user with privileges sufficient to create data in the database.
    """

    @property
    def description(self) -> str:
        return """

        CreateDatabaseUser_management(input_database, {user_authentication_type}, user_name, {user_password}, {role}, {tablespace_name})

        Creates a database user with privileges sufficient to create data in
        the database.

     INPUTS:
      input_database (Workspace):
          The connection file to an Oracle, PostgreSQL, or SQL Server database
          or an enterprise geodatabase in those databases. Ensure that the
          connection is made as a user with privileges to create users in the
          database. When connecting to Oracle, you must connect as the sys user.
      user_authentication_type {Boolean}:
          Specifies the authentication type for the user. If you specify
          OPERATING_SYSTEM_USER, an operating system login must already exist
          for the user you will create. Operating system users are only
          supported for SQL Server and Oracle databases. DATABASE_USER-A
          database-authenticated user will be created.
          This is the default. If your database management system is not
          configured to allow database
          authentication, do not use this option.
          OPERATING_SYSTEM_USER-An operating system-authenticated user
          will be created. The corresponding login must already exist.
          If your database management system is not configured to allow
          operating system authentication, do not use this option.
      user_name (String):
          The name of the new database user.If you create a database user for an
          operating system login, the
          username must be the same as the login name.
      user_password {Encrypted String}:
          The password for the new user. The password policy of the underlying
          database is enforced.If you create a database user for an operating
          system login, no input
          is required.
      role {String}:
          The name of the existing database role to which the new user will be
          added.
      tablespace_name {String}:
          The name of the tablespace that will be used as the default tablespace
          for the new user in an Oracle database. You can specify a
          preconfigured tablespace, or, if the tablespace does not exist, it
          will be created in the Oracle default storage location with its size
          set to 400 MB. If no tablespace is provided, the user's default
          tablespace will be set to the Oracle default tablespace.

        """