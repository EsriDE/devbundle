# Generated documentation for module arcpy.management


class CreateDatabaseConnection(object):
    """
    Creates a file that ArcGIS uses to connect to a database or an enterprise geodatabase.
    """

    @property
    def description(self) -> str:
        return """

        CreateDatabaseConnection_management(out_folder_path, out_name, database_platform, {instance}, {account_authentication}, {username}, {password}, {save_user_pass}, {database}, {schema}, {version_type}, {version}, {date}, {auth_type}, {project_id}, {default_dataset}, {refresh_token}, {key_file}, {role}, {warehouse}, {advanced_options})

        Creates a file that ArcGIS uses to connect to a database or an
        enterprise geodatabase.

     INPUTS:
      out_folder_path (Folder):
          The folder path where the database connection file (.sde) will be
          stored.
      out_name (String):
          The name of the database connection file. The output file will have
          the .sde extension.
      database_platform (String):
          Specifies the database management system platform to which the
          connection will be made. The following are valid options:BIGQUERY-The
          connection will be made to Google BigQuery.DAMENG-The
          connection will be made to Dameng.DB2-The connection will be made to
          IBM Db2 for Linux, UNIX, or
          Windows.ORACLE-The connection will be made to Oracle, Amazon
          Relational
          Database Service (RDS) for Oracle, or Autonomous Transaction
          Processing.POSTGRESQL-The connection will be made to PostgreSQL,
          Amazon Aurora
          (PostgreSQL-compatible edition), Amazon Relational Database Service
          (RDS) for PostgreSQL, Google Cloud SQL for PostgreSQL, Microsoft Azure
          Database for PostgreSQL, or Microsoft Azure Cosmos DB for
          PostgreSQL.REDSHIFT-The connection will be made to Amazon Redshift.SAP
          HANA-The connection will be made to SAP HANA or SAP HANA
          Cloud.SNOWFLAKE-The connection will be made to
          Snowflake.SQL_SERVER-The connection will be made to Microsoft SQL
          Server,
          Microsoft Azure SQL Database, Microsoft Azure SQL Managed Instance,
          Amazon Relational Database Service (RDS) for SQL Server, or Google
          Cloud SQL for SQL Server.TERADATA-The connection will be made to
          Teradata Vantage.
      instance {String}:
          The database server or instance to which the connection will be
          made.The value you specify for the database_platform parameter
          indicates
          the type of database or cloud data warehouse to which the connection
          will be made. The information you provide for the instance parameter
          will vary, depending on the platform you specified.See below for
          information about what to provide for each platform.Dameng-The name of
          the server where the Dameng database is
          installedDb2-The name of the cataloged Db2 databaseOracle-Either the
          TNS name or the Oracle Easy Connection string to
          connect to the Oracle database or database servicePostgreSQL-The name
          of the server where PostgreSQL is installed or the
          name of the PostgreSQL database service instanceRedshift-The URL for
          the Redshift serverSAP HANA-The Open Database Connectivity (ODBC) data
          source name for
          the SAP HANA database or database serviceSnowflake-The URL of the
          Snowflake serverSQL Server-The name of the SQL Server database
          instance or the name of
          the database service instanceTeradata-The ODBC data source name for
          the Teradata database
      account_authentication {Boolean}:
          Specifies the type of authentication that will be used.
          DATABASE_AUTH-                  Database authentication will
          be used. An internal database
          username and a password will be used to connect to the database. You
          aren't required to provide your username and password to create a
          connection; however, if you don't, you will be prompted to enter them
          when a connection is established. If the connection file you
          are creating will provide ArcGIS services
          with access to the database or geodatabase, or if you want to use the
          Catalog search to locate data accessed through this connection file,
          you must include a username and
          password.OPERATING_SYSTEM_AUTH-Operating system authentication will be
          used.
          You do not need to provide a username and password. The connection
          will be made with the username and password that were used to log in
          to the operating system. If the login used for the operating system is
          not a valid database login, the connection will fail.
      username {String}:
          The database username that will be used for database authentication.
      password {Encrypted String}:
          The database user password that will be used for database
          authentication.
      save_user_pass {Boolean}:
          Specifies whether the username and password will be
          saved.SAVE_USERNAME-The username and password will be saved in the
          connection file. This is the default. If the connection file you are
          creating will provide ArcGIS services with access to the database,
          geodatabase, or cloud data warehouse, or if you want to use the
          Catalog search to locate data accessed through this connection file,
          you must save the username and password.DO_NOT_SAVE_USERNAME-The
          username and password will not be saved in
          the connection file. Every time you attempt to connect using the file,
          you will be prompted for the username and password.
      database {String}:
          The name of the database to which the connection will be made. This
          parameter applies to PostgreSQL, Redshift, Snowflake, and SQL Server
          platforms.
      schema {String}:
          The user schema geodatabase to which the connection will be made. This
          option only applies to Oracle databases that contain at least one
          user-schema geodatabase. The default value for this parameter is to
          use the sde schema geodatabase.
      version_type {String}:
          Specifies the type of version to which the connection will be made.
          TRANSACTIONAL-The connection will be made to a traditional
          transactional version. This option does not apply to
          geodatabases in SAP HANA.HISTORICAL-The connection will be made to an
          historical marker.POINT_IN_TIME-The connection will be made to a
          specific point in time.
          If POINT_IN_TIME is used, the version parameter will be
          ignored.BRANCH-The connection will be made to the default branch
          version.If TRANSACTIONAL or HISTORICAL is used, the date parameter
          will be
          ignored. If HISTORICAL is used and a name is not provided for the
          version parameter, the default transactional version will be used. If
          POINT_IN_TIME is used and a date is not provided for the date
          parameter, the default transactional version will be used.
      version {String}:
          The geodatabase transactional version or historical marker to which
          the connection will be made. The default option uses the default
          transactional version.If you choose a branch version type, the
          connection is always to the
          default branch version.
      date {Date}:
          The value representing the date and time that will be used to connect
          to the database when working with archive-enabled data. Dates
          can be entered in the following formats:        6/9/2011
          4:20:15 PM6/9/2011 16:20:156/9/20114:20:15 PM16:20:15If a time is
          entered without a date, the default date of December 30,
          1899, will be used.If a date is entered without a time, the default
          time of 12:00:00 AM
          will be used.
      auth_type {String}:
          Specifies the advanced authentication type that will be used when
          connecting to a cloud data warehouse, Microsoft Azure SQL Database, or
          Azure SQL Managed
          Instance.AZURE_ACTIVE_DIRECTORY_UNIVERSAL_WITH_MFA-The Microsoft Entra
          multifactor authentication (MFA) username authentication type will be
          used, but not the password. When you connect, a code is sent to you in
          a text message, email, or MFA device, or it can use a fingerprint scan
          for authentication. This second part of the authentication process
          varies depending on how your network and authentication protocols are
          configured. This option is supported for Azure SQL Database and Azure
          SQL Managed Instance only.AZURE_ACTIVE_DIRECTORY_PASSWORD-The
          Microsoft Entra Password
          authentication type, which requires username and password parameter
          values, will be used. Usernames can be a maximum of 30 characters.
          This option is supported for Azure SQL Database and Azure SQL Managed
          Instance
          only.AZURE_ACTIVE_DIRECTORY_INTEGRATEDSERVICE_AUTHENTICATION-The
          Microsoft
          Entra Integrated authentication type will be used. You do not need to
          provide a username and password. The connection will be made with the
          username and password that were used to log in to the operation
          system. This option is supported for Azure SQL Database and Azure SQL
          Managed Instance only.SERVICE_AUTHENTICATION-The service
          authentication type when connecting
          to Google BigQuery will be used. See Google BigQuery documentation
          about authentication for information.STANDARD-The standard
          authentication type when connecting to Amazon
          Redshift will be used. See the Amazon Redshift ODBC Data Connector
          Installation and Configuration Guide for information about standard
          authentication.USER-An authentication method that requires a username
          and password
          when connecting to Snowflake will be used.USER_AUTHENTICATION-The user
          authentication type when connecting to
          Google BigQuery will be used. See Google BigQuery documentation about
          authentication for information.
      project_id {String}:
          The project ID for the Google BigQuery connection.
      default_dataset {String}:
          The default dataset for the Google BigQuery connection.
      refresh_token {Encrypted String}:
          The refresh token value.This parameter is only applicable for Google
          BigQuery connections when
          the advanced authentication type is user authentication.
      key_file {File}:
          The key file value.This parameter is only applicable for Google
          BigQuery connections when
          the advanced authentication type is server authentication.
      role {String}:
          The role value for a cloud data warehouse connection.This parameter is
          only applicable for connections to Snowflake.
      warehouse {String}:
          The warehouse value for the connection.This parameter is only
          applicable for connections to Snowflake.
      advanced_options {String}:
          The advanced options for the connection. This is optional connection
          information that is specific to the cloud data warehouse platform
          (Google BigQuery, Amazon Redshift, or Snowflake) to which you connect.
          Provide advanced options using Option=<value> separated by semicolons.
          For example, option1=value1;option2=value2;. Consult the cloud data
          warehouse documentation for information about optional connection
          options.

        """