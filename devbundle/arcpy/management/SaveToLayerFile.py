# Generated documentation for module arcpy.management


class SaveToLayerFile(object):
    """
    Creates an output layer file (.lyrx) from a map layer. The layer file stores many properties of the input layer such as symbology, labeling, and custom pop-ups.
    """

    @property
    def description(self) -> str:
        return """

        SaveToLayerFile_management(in_layer, out_layer, {is_relative_path}, {version})

        Creates an output layer file (.lyrx) from a map layer. The layer file
        stores many properties of the input layer such as symbology, labeling,
        and custom pop-ups.

     INPUTS:
      in_layer (Layer / Table View):
          The map layer that will be saved to disk as a layer file.
      is_relative_path {Boolean}:
          Specifies whether the output layer file will store a relative path to
          the source data stored on disk or an absolute path.ABSOLUTE-The output
          layer file will store an absolute path to the
          source data stored on disk. This is the default.RELATIVE-The output
          layer file will store a relative path to the
          source data stored on disk. If the output layer file is moved, its
          source path will update to where the source data should be in relation
          to the new path.
      version {String}:
          Specifies the version of the output layer file.CURRENT-The current
          version. This is the default.

     OUTPUTS:
      out_layer (Layer File):
          The output layer file (.lyrx) that will be created.

        """