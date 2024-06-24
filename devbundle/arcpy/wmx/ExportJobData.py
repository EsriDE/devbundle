# Generated documentation for module arcpy.wmx


class ExportJobData(object):
    """
    This tool will export the Workflow Manager (Classic) repository to a .jxl file in the specified folder location. The .jxl file will contain all the configuration information for the repository as well as information about all the jobs. The .jxl file can be imported into another Workflow Manager (Classic) repository using the Import Job Data tool.
    """

    @property
    def description(self) -> str:
        return """

        ExportJobData_wmx(Input_Folder, {Input_DatabasePath}, {Input_Repository_Name}, {Input_Export_Since}, {Input_Export_Until})

        This tool will export the Workflow Manager (Classic) repository to a
        .jxl file in the specified folder location. The .jxl file will contain
        all the configuration information for the repository as well as
        information about all the jobs. The .jxl file can be imported into
        another Workflow Manager (Classic) repository using the Import Job
        Data tool.

     INPUTS:
      Input_Folder (Folder):
          The location of the JXL file output from the tool. This folder can be
          on a local or a network drive.
      Input_DatabasePath {File}:
          The Workflow Manager (Classic) connection file for the database to be
          exported. If no connection file is specified, the current default
          Workflow Manager (Classic) database in the project is used.
      Input_Repository_Name {String}:
          The name of the Workflow Manager (Classic) repository that contains
          the configuration to be shared. If repository name is not specified,
          the current default Workflow Manager (Classic) repository name is
          used.
      Input_Export_Since {Date}:
          By specifying a date, the JXL exported will only contain changes that
          occurred between the specified time and the current date. The input
          should be in UTC time format.
      Input_Export_Until {Date}:
          By specifying a date, the JXL exported will only contain
          changes that occurred betweenand the specified time. The input should
          be in UTC time format. Export Since

        """