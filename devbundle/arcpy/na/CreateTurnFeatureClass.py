# Generated documentation for module arcpy.na


class CreateTurnFeatureClass(object):
    """
    Creates a new turn feature class to store turn features that model turning movements in a network dataset.
    """

    @property
    def description(self) -> str:
        return """

        CreateTurnFeatureClass_na(out_location, out_feature_class_name, {maximum_edges}, {in_network_dataset}, {in_template_feature_class}, {spatial_reference}, {config_keyword}, {spatial_grid_1}, {spatial_grid_2}, {spatial_grid_3}, {has_z})

        Creates a new turn feature class to store turn features that model
        turning movements in a network dataset.

     INPUTS:
      out_location (Workspace / Feature Dataset):
          The file, workgroup, or enterprise geodatabase, or the folder in which
          the output turn feature class will be created. The workspace must
          already exist.
      out_feature_class_name (String):
          The name of the turn feature class to be created.
      maximum_edges {Long}:
          The maximum number of edges that turns in the new turn feature class
          can model. The default value is 5. The maximum value is 50.
      in_network_dataset {Network Dataset Layer}:
          The network dataset in which the turn feature class will participate.
          The resulting turn feature class will be added as a turn source to the
          network dataset. If no network dataset is specified, the turn feature
          class will be created as not participating in a network dataset.
      in_template_feature_class {Feature Layer}:
          The feature class used as a template to define the attribute schema of
          the new turn feature class. If the template feature class has
          the following fields, they
          are not created on the output turn feature class;,,,,,,,,,,,,,,.
          NODE_NODE#JUNCTIONF_EDGET_EDGEF-EDGET-
          EDGEARC1_ARC2_ARC1#ARC2#ARC1-IDARC2-IDAZIMUTHANGLE
      spatial_reference {Spatial Reference}:
          The spatial reference to be applied to the output turn feature class.
          This parameter is ignored if the output location is a geodatabase
          feature dataset, as the output turn feature class will inherit the
          spatial reference of the feature dataset.If you want to import the
          spatial reference from an existing feature
          class, specify its path as the parameter value.
      config_keyword {String}:
          Specifies the configuration keyword that determines the storage
          parameters of the new turn feature class. This parameter is used only
          if the output location is an workgroup or enterprise geodatabase
      spatial_grid_1 {Double}:
          This parameter is not supported. Any value provided will be ignored.
      spatial_grid_2 {Double}:
          This parameter is not supported. Any value provided will be ignored.
      spatial_grid_3 {Double}:
          This parameter is not supported. Any value provided will be ignored.
      has_z {Boolean}:
          ENABLED-The coordinates in the new turn feature class will have
          elevation (Z) values. This value should be used if the input network
          dataset is specified and it supports connectivity based on z
          coordinate values of the network sources.DISABLED-The coordinates in
          the new turn feature class will not have
          elevation (Z) values.

        """