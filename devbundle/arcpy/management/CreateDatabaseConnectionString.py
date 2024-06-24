# Generated documentation for module arcpy.management


class CreateDatabaseConnectionString(object):
    """
    Creates a connection string that geoprocessing tools can use to connect to a database or an enterprise geodatabase.
    """

    @property
    def description(self) -> str:
        return """

        CreateDatabaseConnectionString_management(database_platform, instance, {account_authentication}, {username}, {password}, {database}, {object_name}, {data_type}, {feature_dataset}, {schema}, {version_type}, {version}, {date})

        Creates a connection string that geoprocessing tools can use to
        connect to a database or an enterprise geodatabase.

     INPUTS:
      database_platform (String):
          Specifies the database platform to which the connection will be
          made.SQL_SERVER-Connect to Microsoft SQL Server or Microsoft Azure SQL
          Database.ORACLE-Connect to Oracle.DB2-Connect to IBM DB2 for Linux,
          UNIX, or Windows.POSTGRESQL-Connect to PostgreSQL.TERADATA-Connect to
          Teradata Data Warehouse Appliance.SAP HANA-Connect to SAP
          HANA.DAMENG-Connect to Dameng.
      instance (String):
          The database server or instance to which the connection will be made.
          This parameter value depends on theparameter value chosen.
          Database Platform
      account_authentication {Boolean}:
          Specifies the type of authentication that will be used.
          DATABASE_AUTH-                  Database authentication will
          be used. An internal database
          user name and password are used to connect to the database. You aren't
          required to type your user name and password to create a connection;
          however, if you don't, you will be prompted to enter them when a
          connection is established. This is the default. If the
          connection file you are creating will provide ArcGIS services
          with access to the database or geodatabase, or if you want to use the
          Catalog search to locate data accessed through this connection file,
          you must type a user name and password.OPERATING_SYSTEM_AUTH-Operating
          system authentication will be used.
          You do not need to type a user name and password. The connection will
          be made with the user name and password that were used to log in to
          the operating system. If the login used for the operating system is
          not a valid geodatabase login, the connection will fail.
      username {String}:
          The database user name that will be used when using database
          authentication.
      password {Encrypted String}:
          The database user password that will be used when using database
          authentication.
      database {String}:
          The name of the database to which you will connect. This parameter
          only applies to PostgreSQL and SQL Server platforms.
      object_name {String}:
          The name of the dataset or object in the database to which the
          connection string will point. This connection string can be used as a
          path to the specified dataset.
      data_type {String}:
          The type of dataset or object referred to in the dataset object name.
          If there are multiple objects with the same name in the database, you
          may need to specify the data type of the object for which you want to
          make a connection string.
      feature_dataset {String}:
          The name of the feature dataset containing the dataset or object for
          which you want to make a connection string. If the dataset is not in a
          feature dataset (for example, if it's at the root of the database), do
          not specify a target feature dataset.
      schema {String}:
          The user schema geodatabase to which you will connect. This option
          only applies to Oracle databases that contain at least one user-schema
          geodatabase. The default value for this parameter is to use the sde
          schema (master) geodatabase.
      version_type {String}:
          Specifies the type of version to which you will connect. This
          parameter only applies when connecting to a geodatabase.
          TRANSACTIONAL-Connect to a transactional version. Ifis
          selected, theparameter will be populated with a list of transactional
          versions, and theparameter will be inactive. This is the Default.
          TransactionalThe following version will be usedDate and Time
          HISTORICAL-Connect to an historical marker. Ifis selected,
          theparameter will be populated with a list of historical markers, and
          theparameter will be inactive. HistoricalThe following version
          will be usedDate and Time         POINT_IN_TIME-Connect to a specific
          point in time. Ifis
          selected, theparameter will be inactive, and theparameter will become
          active. Point in timeThe following version will be usedDate
          and TimeBRANCH-Connect to the default branch version. Ifis
          selected and a name is not provided, the default
          transactional version is used. Ifis selected and a date is not
          provided in theparameter, the default transactional version is used.
          HistoricalPoint in timeDate and Time
      version {String}:
          The geodatabase transactional version or historical marker to connect
          to. The default option uses the default transactional version.If you
          choose a branch version type, the connection is always to the
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

        """