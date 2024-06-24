# Generated documentation for module arcpy.conversion


class SASToTable(object):
    """
    Converts a SAS dataset to a table.
    """

    @property
    def description(self) -> str:
        return """

        SASToTable_conversion(in_sas_dataset, out_table, {use_cas_connection}, {hostname}, {port}, {username}, {password}, {custom_cfg_file}, {authinfo_file})

        Converts a SAS dataset to a table.

     INPUTS:
      in_sas_dataset (String):
          The input SAS dataset. Provide the dataset in the form
          libref.tablename in which libref is the name of a SAS library and
          tablename is the name of the SAS dataset.
      use_cas_connection {Boolean}:
          Specifies whether the input SAS dataset will be downloaded from CAS or
          accessed from a local SAS library.USE_CAS-The input SAS dataset will
          be downloaded from
          CAS.LOCAL_SAS-The input SAS dataset will be accessed from a local SAS
          library. This is the default.
      hostname {String}:
          The URL of the CAS host.
      port {Long}:
          The port of the CAS connection.
      username {String}:
          The username for the CAS connection.
      password {String Hidden}:
          The password for the CAS connection. This password is hidden and not
          accessible after running the tool.
      custom_cfg_file {File}:
          The file specifying custom configurations for the SAS session. The
          file is only required for customized local or remote SAS deployments.
      authinfo_file {File}:
          The file containing authentication information when connecting to CAS.
          The file must contain the username and encoded password for the
          connection. If a file is provided, the username and password
          parameters do not need to be specified.

     OUTPUTS:
      out_table (Table):
          The output table.

        """