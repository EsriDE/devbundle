# Generated documentation for module arcpy.management


class TransferFiles(object):
    """
    Transfers files between a file system and a cloud storage workspace.
    """

    @property
    def description(self) -> str:
        return """

        TransferFiles_management(input_paths;input_paths..., output_folder, {file_filter})

        Transfers files between a file system and a cloud storage workspace.

     INPUTS:
      input_paths (Raster Dataset / File / Folder):
          The list of input files or folders that will be copied to the output
          folder. The path can be a file system path or cloud storage path where
          the .acs file can be used.
      output_folder (Folder):
          The output folder path where the files will be copied.
      file_filter {String}:
          A file pattern filter that will limit the number of files that need to
          be copied, such as .tif, .crf, and similar image file types.

        """