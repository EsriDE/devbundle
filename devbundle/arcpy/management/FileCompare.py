# Generated documentation for module arcpy.management


class FileCompare(object):
    """
    Compares two files and returns the comparison results..
    """

    @property
    def description(self) -> str:
        return """

        FileCompare_management(in_base_file, in_test_file, {file_type}, {continue_compare}, {out_compare_file})

        Compares two files and returns the comparison results..

     INPUTS:
      in_base_file (File):
          Theis compared with the. Therefers to a file that you have
          declared valid. This base file has the correct content and
          information. Input Base FileInput Test FileInput Base File
      in_test_file (File):
          Theis compared against the. Therefers to a file that you have
          made changes to by editing or compiling new information. Input
          Test FileInput Base FileInput Test File
      file_type {String}:
          The type of files being compared.ASCII-Compare using ASCII characters.
          This is the
          default.BINARY-Perform a binary compare.
      continue_compare {Boolean}:
          Indicates whether to compare all properties after encountering the
          first mismatch.NO_CONTINUE_COMPARE-Stops after encountering the first
          mismatch. This
          is the default.CONTINUE_COMPARE-Compares other properties after
          encountering the
          first mismatch.

     OUTPUTS:
      out_compare_file {File}:
          This file will contain all similarities and differences
          between theand the. This file is a comma-delimited text file which can
          be viewed and used as a table in ArcGIS. Input Base FileInput
          Test File

        """