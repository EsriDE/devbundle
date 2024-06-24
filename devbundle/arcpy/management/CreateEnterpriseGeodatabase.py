# Generated documentation for module arcpy.management


class CreateEnterpriseGeodatabase(object):
    """
    Creates a database, storage locations, and a database user to act as the geodatabase administrator and owner of the geodatabase. Functionality varies depending on the database management system used. The tool grants the geodatabase administrator the privileges required to create a geodatabase; it then creates a geodatabase in the database.
    """

    @property
    def description(self) -> str:
        return """

        CreateEnterpriseGeodatabase_management(database_platform, instance_name, {database_name}, {account_authentication}, {database_admin}, {database_admin_password}, {sde_schema}, {gdb_admin_name}, {gdb_admin_password}, {tablespace_name}, authorization_file, {spatial_type})

        Creates a database, storage locations, and a database user to act as
        the geodatabase administrator and owner of the geodatabase.
        Functionality varies depending on the database management system used.
        The tool grants the geodatabase administrator the privileges required
        to create a geodatabase; it then creates a geodatabase in the
        database.

     INPUTS:
      database_platform (String):
          Specifies the type of database management system to which a connection
          to create a geodatabase will be made.Oracle-Connection to an Oracle
          instance will be
          made.PostgreSQL-Connection to a PostgreSQL database cluster will be
          made.SQL_Server-Connection to a Microsoft SQL Server instance will be
          made.
      instance_name (String):
          The name of the instance.For SQL Server, provide the SQL Server
          instance name. Case-sensitive
          or binary collation SQL Server instances are not supported.For Oracle,
          provide either the TNS name or the Oracle Easy Connection
          string.For PostgreSQL, provide the name of the server where PostgreSQL
          is
          installed.
      database_name {String}:
          The name of the database.This parameter is valid for PostgreSQL and
          SQL Server. You can provide
          either the name of an existing, preconfigured database or a name for a
          database that the tool will create.If the tool creates the database in
          SQL Server, the file sizes will be
          either the same as defined for the SQL Server model database or 500 MB
          for the .mdf file and 125 MB for the .ldf file, whichever is greater.
          Both the .mdf and .ldf files are created in the default SQL Server
          location on the database server. Do not name the database sde.If the
          tool creates the database in PostgreSQL, it uses the template1
          database as the template for the database. If you need to use a
          different template-for example, you require a template that is enabled
          for PostGIS-you must create the database before running this tool and
          provide the name of the existing database. Always use lowercase
          characters for the database name. If you use uppercase letters, the
          tool will convert them to lowercase.
      account_authentication {Boolean}:
          Specifies the type of authentication that will be used for the
          database connection. OPERATING_SYSTEM_AUTH-Operating system
          authentication will be
          used. The login information that you provide for the computer where
          you run the tool is the login that will be used to authenticate the
          database connection. If the database management system is not
          configured to allow operating
          system authentication, authentication will fail.
          DATABASE_AUTH-Database authentication will be used. You must
          provide a valid database username and password for authentication in
          the database. This is the default. If the database management
          system is not configured to allow database
          authentication, authentication will fail.
      database_admin {String}:
          The database administrator user for database authentication. For
          Oracle, use the sys user. For PostgreSQL, specify a user with
          superuser status. For SQL Server, specify any member of the sysadmin
          fixed server role.
      database_admin_password {Encrypted String}:
          The database administrator password for database authentication.
      sde_schema {Boolean}:
          This parameter is only relevant to SQL Server and specifies whether
          the geodatabase will be created in the schema of a user named sde or
          in the dbo schema in the database. If creating a dbo-schema
          geodatabase, connect as a user who is dbo in the SQL Server
          instance.SDE_SCHEMA-The geodatabase repository is owned by and will be
          stored
          in the schema of a user named sde. This is the default.DBO_SCHEMA-The
          geodatabase repository will be stored in the dbo schema
          in the database.
      gdb_admin_name {String}:
          The name of the geodatabase administrator user.If you are using
          PostgreSQL, this value must be sde. If the sde login
          role does not exist, this tool will create it and grant it superuser
          status in the database cluster. If the sde login role exists, this
          tool will grant it superuser status if it does not already have it.
          The tool also creates an sde schema in the database and grants usage
          on the schema to public.If you are using Oracle, the value is sde. If
          the sde user does not
          exist in the Oracle database, the tool will create it and grant it the
          privileges required to create and upgrade a geodatabase and disconnect
          users from the database. The tool also grants privileges to allow data
          imports using Oracle Data Pump. If the sde user exists, the tool will
          grant these same privileges to the existing user.If you are using SQL
          Server and specified an sde-schema geodatabase,
          this value must be sde. The tool will create an sde login, database
          user, and schema and grant it privileges to create a geodatabase and
          remove connections from the SQL Server instance. If you specified a
          dbo schema, do not provide a value for this parameter.
      gdb_admin_password {Encrypted String}:
          The password for the geodatabase administrator user. If the
          geodatabase administrator user exists in the database management
          system, the password you provide must match the existing password. If
          the geodatabase administrator user does not exist, provide a valid
          database password for the new user. The password must meet the
          password policy enforced by the database.The password is an encrypted
          string.
      tablespace_name {String}:
          The name of the tablespace. This parameter is only valid for
          Oracle and PostgreSQL
          database management system types. For Oracle, do one of the following:
          Provide the name of an existing tablespace. This tablespace will be
          used as the default tablespace for the geodatabase administrator
          user.Provide a valid name for a new tablespace. The tool will create a
          400
          MB tablespace in the Oracle default storage location and set it as the
          geodatabase administrator's default tablespace.Leave the tablespace
          blank. The tool will create a 400 MB tablespace
          named SDE_TBS in the Oracle default storage location. The SDE_TBS
          tablespace will be set as the geodatabase administrator's default
          tablespace.This tool does not create a tablespace in PostgreSQL. You
          must either
          provide the name of an existing tablespace to be used as the
          database's default tablespace or leave this parameter blank. If you
          leave the parameter blank, the tool will create a database in the
          pg_default tablespace.
      authorization_file (File):
          The keycodes file that was created when ArcGIS Server was authorized.
          If you have not done so, authorize ArcGIS Server to create this file.
          This file is in the <drive>\Program
          Files\ESRI\License<release#>\sysgen folder on Windows or the
          /arcgis/server/framework/runtime/.wine/drive_c/Program
          Files/ESRI/License<release#>/sysgen directory on Linux. The
          /.wine directory is a hidden directory.You may need to copy the
          keycodes file from the ArcGIS Server machine
          to a location that is accessible to the tool.
      spatial_type {String}:
          Specifies the spatial type that will be used. This is only applicable
          to PostgreSQL databases.ST_GEOMETRY-The ST_Geometry spatial type will
          be used. This is the
          default.POSTGIS-The PostGIS spatial type will be used.

        """