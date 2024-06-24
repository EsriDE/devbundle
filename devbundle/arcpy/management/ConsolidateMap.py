# Generated documentation for module arcpy.management


class ConsolidateMap(object):
    """
    Consolidates a map and all referenced data sources to a specified output folder.
    """

    @property
    def description(self) -> str:
        return """

        ConsolidateMap_management(in_map;in_map..., output_folder, {convert_data}, {convert_arcsde_data}, {extent}, {apply_extent_to_arcsde}, {preserve_sqlite}, {select_related_rows})

        Consolidates a map and all referenced data sources to a specified
        output folder.

     INPUTS:
      in_map (Map):
          The map (.mapx) to be consolidated. When running this tool within the
          ArcGIS Pro application, the input can be a map, scene, or basemap.
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
      preserve_sqlite {Boolean}:
          Specifies whether input mobile geodatabase data will be preserved as
          mobile geodatabase in the output. If the input data is a mobile
          geodatabase network dataset, the output will always be mobile
          geodatabase.PRESERVE_SQLITE-Mobile geodatabase data will be preserved
          as SQLite in
          the consolidated folder.CONVERT_SQLITE-Mobile geodatabase data will be
          converted to file
          geodatabase. This is the default.
      select_related_rows {Boolean}:
          Specifies whether the specified extent will be applied to related data
          sources.KEEP_ONLY_RELATED_ROWS-Only related data corresponding to
          records
          within the specified extent will be
          consolidated.KEEP_ALL_RELATED_ROWS-Related data sources will be
          consolidated in
          their entirety. This is the default.

     OUTPUTS:
      output_folder (Folder):
          The output folder that will contain the consolidated map and data.If
          the specified folder does not exist, a new folder will be created.

        """