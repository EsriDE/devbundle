# Generated documentation for module arcpy.conversion


class TableToSAS(object):
    """
    Converts a table to a SAS dataset.
    """

    @property
    def description(self) -> str:
        return """

        TableToSAS_conversion(in_table, out_sas_dataset, {replace_sas_dataset}, {use_domain_and_subtype_description}, {use_cas_connection}, {hostname}, {port}, {username}, {password}, {custom_cfg_file}, {authinfo_file})

        Converts a table to a SAS dataset.

     INPUTS:
      in_table (Table View):
          The input table.
      replace_sas_dataset {Boolean}:
          Specifies whether an existing SAS dataset will be overwritten in the
          output.OVERWRITE-The output SAS dataset can overwrite an existing
          dataset.NO_OVERWRITE-The output SAS dataset cannot overwrite an
          existing
          dataset.. This is the default.
      use_domain_and_subtype_description {Boolean}:
          Specifies whether domain and subtype descriptions will be included in
          the output SAS dataset.USE_DOMAIN-Domain and subtype descriptions will
          be included in the
          output SAS dataset.NO_DOMAIN-Domain and subtype descriptions will not
          be included in the
          output SAS dataset. This is the default.
      use_cas_connection {Boolean}:
          Specifies whether the output SAS dataset will be uploaded to CAS or
          saved in a local SAS library.USE_CAS-The output SAS dataset will be
          uploaded to CAS.LOCAL_SAS-The
          output SAS dataset will be saved in a local SAS library.
          This is the default.
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
      out_sas_dataset (String):
          The output SAS dataset. Provide the dataset in the form libref.table
          in which libref is the name of a SAS library and table is the name of
          the SAS table.

        """