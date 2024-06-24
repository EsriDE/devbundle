# Generated documentation for module arcpy.management


class ChangePrivileges(object):
    """
    Establishes or changes user access privileges on the input enterprise database datasets, stand-alone feature classes, or tables.
    """

    @property
    def description(self) -> str:
        return """

        ChangePrivileges_management(in_dataset;in_dataset..., user, {View}, {Edit})

        Establishes or changes user access privileges on the input enterprise
        database datasets, stand-alone feature classes, or tables.

     INPUTS:
      in_dataset (Layer / Table View / Dataset / Address Locator):
          The datasets, feature classes, or tables whose access privileges will
          be changed.
      user (String):
          The database username whose privileges will be modified.
      View {String}:
          Specifies the user's view privileges.AS_IS-No changes will be made to
          the user's existing view privileges.
          If the user has view privileges, they will continue to have view
          privileges. If the user doesn't have view privileges, they will
          continue to not have view privileges.GRANT-The user will be allowed to
          view the datasets.REVOKE-The user's view privileges will be removed.
      Edit {String}:
          Specifies the user's edit privileges.AS_IS-No changes will be made to
          the user's existing edit privileges.
          If the user has edit privileges, they will continue to have edit
          privileges. If the user doesn't have edit privileges, they will
          continue to not have edit privileges.GRANT-The user will be allowed to
          edit the input datasets.REVOKE-The user's edit privileges will be
          removed. The user can still
          view the input dataset.

        """