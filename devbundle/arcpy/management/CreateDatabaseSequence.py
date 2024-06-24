# Generated documentation for module arcpy.management


class CreateDatabaseSequence(object):
    """
    Creates a database sequence in a geodatabase. You can use the sequences in custom applications that access the geodatabase.
    """

    @property
    def description(self) -> str:
        return """

        CreateDatabaseSequence_management(in_workspace, seq_name, {seq_start_id}, {seq_inc_value})

        Creates a database sequence in a geodatabase. You can use the
        sequences in custom applications that access the geodatabase.

     INPUTS:
      in_workspace (Workspace):
          The database connection file (.sde) to connect to the enterprise
          geodatabase in which you want to create a sequence or the path to the
          file geodatabase (including the file geodatabase name). For
          database connections, the user specified in the database
          connection will be the owner of the sequence and, therefore, must have
          the following permissions in the database:        Db2-CREATEIN
          privilege on their schemaOracle-CREATE SEQUENCE system
          privilegePostgreSQL-Authority on their schemaSAP HANA-Must be a
          standard userSQL Server-CREATE SEQUENCE privilege and ALTER OR CONTROL
          permission
          on their schema
      seq_name (String):
          The name you want to assign to the database sequence. For enterprise
          geodatabases, the name must meet sequence name requirements for the
          database platform you're using and must be unique in the database. For
          file geodatabases, the name must be unique to the file geodatabase. It
          is important that you remember this name, as it is the name you use in
          your custom applications and expressions to invoke the sequence.
      seq_start_id {Long}:
          The starting number of the sequence. If you do not provide a starting
          number, the sequence starts with 1. If you do provide a starting
          number, it must be greater than 0.
      seq_inc_value {Long}:
          Describes how the sequence numbers will increment. For example, if the
          sequence starts at 10 and the increment value is 5, the next value in
          the sequence is 15, and the next value after that is 20. If you do not
          specify an increment value, sequence values will increment by 1.

        """