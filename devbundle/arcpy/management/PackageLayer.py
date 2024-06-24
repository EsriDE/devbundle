# Generated documentation for module arcpy.management


class PackageLayer(object):
    """
    Packages one or more layers and all referenced data sources to create a single compressed .lpkx file.
    """

    @property
    def description(self) -> str:
        return """

        PackageLayer_management(in_layer;in_layer..., output_file, {convert_data}, {convert_arcsde_data}, {extent}, {apply_extent_to_arcsde}, {schema_only}, {version;version...}, {additional_files;additional_files...}, {summary}, {tags}, {select_related_rows}, {preserve_sqlite}, {exclude_network_dataset})

        Packages one or more layers and all referenced data sources to create
        a single compressed .lpkx file.

     INPUTS:
      in_layer (Layer / Table View):
          The layers that will be packaged.
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
      version {String}:
          Specifies the version of the geodatabases that will be created
          in the resulting package. Specifying a version allows packages to be
          shared with earlier versions of ArcGIS and supports backward
          compatibility. A package saved to an earlier version may lose
          properties that are
          only available in the later version.ALL-The package will contain a
          geodatabase and layer file compatible
          with all versions (ArcGIS Pro 1.2 and later).CURRENT-The package will
          contain a geodatabase and layer file
          compatible with the version of the current ArcGIS Pro release.1.2-The
          package will contain a geodatabase and layer file compatible
          with ArcGIS Pro version 1.2 and later.2.x-The package will contain a
          geodatabase and layer file compatible
          with ArcGIS Pro version 2.0 and later.3.x-The package will contain a
          geodatabase and layer file compatible
          with ArcGIS Pro version 3.0 and later.
      additional_files {File}:
          The additional files that will be added to a package. Additional
          files, such as .doc, .txt, .pdf, and so on, are used to provide more
          information about the contents and purpose of the package.
      summary {String}:
          The summary information that will be added to the properties of the
          package.
      tags {String}:
          The tag information that will be added to the properties of the
          package. Multiple tags can be added or separated by a comma or
          semicolon.
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
          will also be packaged.INCLUDE_NETWORK_DATASET-The network dataset will
          be included and
          packaged. This is the default.EXCLUDE_NETWORK_DATASET-The network
          dataset will not be included.
          Only the network analysis layers will be packaged.

     OUTPUTS:
      output_file (File):
          The location and name of the output package file (.lpkx) that will be
          created.

        """