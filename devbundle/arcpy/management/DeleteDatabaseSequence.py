# Generated documentation for module arcpy.management


class DeleteDatabaseSequence(object):
    """
    Deletes a database sequence from a geodatabase.
    """

    @property
    def description(self) -> str:
        return """

        DeleteDatabaseSequence_management(in_workspace, seq_name)

        Deletes a database sequence from a geodatabase.

     INPUTS:
      in_workspace (Workspace):
          The full path to the location of the file geodatabase from
          which you want to delete a sequence or the database connection file
          (.sde) to connect to the enterprise geodatabase from which you want to
          delete a sequence. The user specified in the database connection must
          have the following permissions in the database:        Db2-DBADM
          authorityOracle-Must be the sequence owner or have the DROP
          ANY SEQUENCE system
          privilegePostgreSQL-Must be the sequence ownerSAP HANA-Must be a
          standard userSQL Server-ALTER OR CONTROL permission on the database
          schema where
          the sequence is stored
      seq_name (String):
          The name of the database sequence you want to delete. Once deleted,
          the sequence cannot be used to generate sequence IDs when called from
          existing custom applications or expressions.

        """