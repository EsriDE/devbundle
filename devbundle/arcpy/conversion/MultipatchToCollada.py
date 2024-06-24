# Generated documentation for module arcpy.conversion


class MultipatchToCollada(object):
    """
    Converts one or more multipatch features into a collection of COLLADA files (.dae) and referenced texture image files in an output folder.
    """

    @property
    def description(self) -> str:
        return """

        MultipatchToCollada_conversion(in_features, output_folder, {prepend_source}, {field_name}, {collada_version})

        Converts one or more multipatch features into a collection of COLLADA
        files (.dae) and referenced texture image files in an output folder.

     INPUTS:
      in_features (Feature Layer):
          The multipatch features to be exported.
      prepend_source {Boolean}:
          Specifies whether the names of the output COLLADA files will be
          prepended with the name of the source feature
          layer.PREPEND_SOURCE_NAME-The file names will be prepended with the
          name of
          the source feature layer.PREPEND_NONE-The file names will not be
          prepended with the name of the
          source feature layer. This is the default.
      field_name {Field}:
          The feature attribute that will be used as the output COLLADA file
          name for each exported feature. If no field is specified, the
          feature's Object ID will be used.
      collada_version {String}:
          Specifies the COLLADA version to which the files will be
          exported.1.5-Files will be exported to COLLADA version 1.5. Version
          1.5
          supports the inclusion of georeferencing information and enhanced
          rendering capabilities. This is the default.1.4-Files will be exported
          to COLLADA version 1.4. Version 1.4 is the
          widely supported standard used in many design related application
          platforms. Select this version if the COLLADA file will be used on
          systems that do not support version 1.5.

     OUTPUTS:
      output_folder (Folder):
          The destination folder where the output COLLADA files and texture
          image files will be placed.

        """