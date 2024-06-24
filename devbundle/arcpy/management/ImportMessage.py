# Generated documentation for module arcpy.management


class ImportMessage(object):
    """
    Imports changes from a delta file into a replica geodatabase or imports an acknowledgment message into a replica geodatabase.
    """

    @property
    def description(self) -> str:
        return """

        ImportMessage_management(in_geodatabase, source_delta_file, {output_acknowledgement_file}, {conflict_policy}, {conflict_definition}, {reconcile_with_parent_version})

        Imports changes from a delta file into a replica geodatabase or
        imports an acknowledgment message into a replica geodatabase.

     INPUTS:
      in_geodatabase (Workspace / GeoDataServer):
          The replica geodatabase that will receive the imported message. The
          geodatabase can be local or remote.
      source_delta_file (Workspace / File):
          The file from which the message will be imported.
      conflict_policy {String}:
          Specifies how conflicts will be resolved when they are encountered
          while importing a data change message.MANUAL-Conflicts must be
          manually resolved in the versioning reconcile
          environment.IN_FAVOR_OF_DATABASE-Conflicts will be automatically
          resolved in favor
          of the database receiving the
          changes.IN_FAVOR_OF_IMPORTED_CHANGES-Conflicts will be automatically
          resolved
          in favor of the imported changes.
      conflict_definition {String}:
          Specifies whether the conditions required for a conflict to occur will
          be detected by object (row) or by attribute
          (column).BY_OBJECT-Conflicts will be detected by
          row.BY_ATTRIBUTE-Conflicts
          will be detected by column.
      reconcile_with_parent_version {Boolean}:
          Specifies whether data changes will be automatically reconciled once
          they are sent to the parent replica if no conflicts are present. This
          parameter is only enabled for check-out/check-in
          replicas.DO_NOT_RECONCILE-Changes will not be reconciled with the
          parent
          version. This is the default.RECONCILE-Changes will be reconciled with
          the parent version.

     OUTPUTS:
      output_acknowledgement_file {File}:
          The file that will contain the acknowledgement message. When importing
          data changes, you can also export a message to acknowledge the import
          of a data change message. This parameter is only supported for a data
          change message.

        """