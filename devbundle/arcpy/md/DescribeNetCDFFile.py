# Generated documentation for module arcpy.md


class DescribeNetCDFFile(object):
    """
    Describes the nature and content of an input netCDF dataset. It lists all the variables along with their dimensions and attributes.
    """

    @property
    def description(self) -> str:
        return """

        DescribeNetCDFFile_md(in_netCDF_file, {out_file})

        Describes the nature and content of an input netCDF dataset. It lists
        all the variables along with their dimensions and attributes.

     INPUTS:
      in_netCDF_file (File):
          The input netCDF file that will be described.

     OUTPUTS:
      out_file {File}:
          The name of the output description markdown file that will contain
          summary information about the input netCDF file. Specify the file name
          with the .md extension.

        """