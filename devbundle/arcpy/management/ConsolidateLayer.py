# Generated documentation for module arcpy.management


class ConsolidateLayer(object):
    """
    Consolidates one or more layers by copying all referenced data sources into a single folder.
    """

    @property
    def description(self) -> str:
        return """

        ConsolidateLayer_management(in_layer;in_layer..., output_folder, {convert_data}, {convert_arcsde_data}, {extent}, {apply_extent_to_arcsde}, {schema_only}, {select_related_rows}, {preserve_sqlite}, {exclude_network_dataset})

        Consolidates one or more layers by copying all referenced data sources
        into a single folder.

     INPUTS:
      in_layer (Layer):
          The input layers that will be consolidated.
      convert_data {Boolean}:
          Specifies whether input layers will be converted to a file geodatabase
          or preserved in their original format.CONVERT-Data will be converted
          to a file geodatabase. This option
          does not apply to enterprise geodatabase data sources. To convert
          enterprise geodatabase data, set the convert_arcsde_data parameter to
          CONVERT_ARCSDE.PRESERVE-Data formats will be preserved when possible.
          This is the
          default.
      convert_arcsde_data {Boolean}:
          Specifies whether input enterprise geodatabase layers will be
          converted to a file geodatabase or preserved in their original
          format.CONVERT_ARCSDE-Enterprise geodatabase data will be converted
          to a
          file geodatabase and will be included in the consolidated folder or
          package. This is the default.PRESERVE_ARCSDE-Enterprise geodatabase
          data will be preserved and
          will be referenced in the consolidated folder or package.
      extent {Extent}:
          Specifies the extent that will be used to select or clip
          features.MAXOF-The maximum extent of all inputs will be used.MINOF-The
          minimum
          area common to all inputs will be used.DISPLAY-The extent is equal to
          the visible display.Layer name-The extent of the specified layer will
          be used.Extent object-The extent of the specified object will be
          used.Space delimited string of coordinates-The extent of the specified
          string will be used. Coordinates are expressed in the order of x-min,
          y-min, x-max, y-max.
      apply_extent_to_arcsde {Boolean}:
          Specifies whether the specified extent will be applied to all layers
          or to enterprise geodatabase layers only.ALL-The specified extent
          will be applied to all layers. This is the
          default.ARCSDE_ONLY-The specified extent will be applied to enterprise
          geodatabase layers only.
      schema_only {Boolean}:
          Specifies whether only the schema of the input layers will be
          consolidated or packaged.ALL-All features and records will be
          consolidated or packaged. This
          is the default.SCHEMA_ONLY-Only the schema of the input layers will
          be consolidated
          or packaged.
      select_related_rows {Boolean}:
          Specifies whether the specified extent will be applied to related data
          sources.KEEP_ONLY_RELATED_ROWS-Only related data corresponding to
          records
          within the specified extent will be
          consolidated.KEEP_ALL_RELATED_ROWS-Related data sources will be
          consolidated in
          their entirety. This is the default.
      preserve_sqlite {Boolean}:
          Specifies whether mobile geodatabase data will be preserved in the
          output or written to file geodatabase format. If the input data is a
          mobile geodatabase network dataset, the output will be a mobile
          geodatabase.This parameter overrides the convert_data parameter when
          the input
          data is a mobile geodatabase.CONVERT_SQLITE-Mobile geodatabase data
          will be converted to file
          geodatabase format. This is the default.PRESERVE_SQLITE-Mobile
          geodatabase data will be preserved in the
          output. The geodatabase will be included in its entirety.
      exclude_network_dataset {Boolean}:
          For network analysis layers, specifies whether the network dataset
          will also be consolidated.INCLUDE_NETWORK_DATASET-The network dataset
          will be included and
          consolidated. This is the default.EXCLUDE_NETWORK_DATASET-The network
          dataset will not be included.
          Only the network analysis layers will be consolidated.

     OUTPUTS:
      output_folder (Folder):
          The output folder that will contain the layer files and consolidated
          data.If the specified folder does not exist, a new folder will be
          created.

        """