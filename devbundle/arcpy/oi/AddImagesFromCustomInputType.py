# Generated documentation for module arcpy.oi


class AddImagesFromCustomInputType(object):
    """
    Adds images to an oriented imagery dataset from the input data defined by a custom input type.
    """

    @property
    def description(self) -> str:
        return """

        AddImagesFromCustomInputType_oi(in_oriented_imagery_dataset, input_type, in_type_folder, in_data;in_data..., {auxiliary_parameters;auxiliary_parameters...})

        Adds images to an oriented imagery dataset from the input data defined
        by a custom input type.

     INPUTS:
      in_oriented_imagery_dataset (Oriented Imagery Layer):
          The path and name of the oriented imagery dataset where the images
          will be added.
      input_type (String):
          The name of the custom input type.If the custom input type folder is
          not in
          [InstallDirectory]\Resources\OrientedImagery\CustomInputTypes, specify
          the parameter value as Folder and provide the folder path in the
          in_type_folder parameter.
      in_type_folder (Folder):
          The path to the custom input type folder. The folder must contain a
          Python module with the same name as the folder and the required public
          functions.
      in_data (Value Table):
          The name and the path or value of the input data. The selected custom
          input type determines the available options.
      auxiliary_parameters {Value Table}:
          The names and values of any auxiliary parameters defined in the input
          type schema.

        """