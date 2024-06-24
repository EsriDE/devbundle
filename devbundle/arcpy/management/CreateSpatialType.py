# Generated documentation for module arcpy.management


class CreateSpatialType(object):
    """
    Adds the ST_Geometry SQL type, subtypes, and functions to an Oracle or a PostgreSQL database. This allows you to use the ST_Geometry SQL type to store geometries in a database that does not contain a geodatabase. You can also use this tool to upgrade the existing ST_Geometry type, subtypes, and functions in an Oracle or a PostgreSQL database.
    """

    @property
    def description(self) -> str:
        return """

        CreateSpatialType_management(input_database, sde_user_password, {tablespace_name}, {st_shape_library_path})

        Adds the ST_Geometry SQL type, subtypes, and functions to an Oracle or
        a PostgreSQL database. This allows you to use the ST_Geometry SQL type
        to store geometries in a database that does not contain a geodatabase.
        You can also use this tool to upgrade the existing ST_Geometry type,
        subtypes, and functions in an Oracle or a PostgreSQL database.

     INPUTS:
      input_database (Workspace):
          The input_database is the database connection file (.sde) that
          connects to the Oracle or PostgreSQL database. You must connect as a
          database administrator user; in Oracle, you must connect as the sys
          user.
      sde_user_password (Encrypted String):
          The password for the sde database user. If the sde user does not exist
          in the database, it will be created and will use the password you
          provide. The password policy of the underlying database will be
          enforced. If the sde user does exist in the database or database
          cluster, this password must match the existing password.
      tablespace_name {String}:
          The name of a tablespace that will be set as the default tablespace
          for the sde user in Oracle. If the tablespace name does not exist, it
          will be created in the Oracle default storage location. If a
          tablespace with the specified name does exist, it will be set as the
          sde user's default.
      st_shape_library_path {File}:
          The location on the Oracle server where the st_shape library resides.

        """