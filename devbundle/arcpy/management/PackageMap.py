# Generated documentation for module arcpy.management


class PackageMap(object):
    """
    Packages a map and all referenced data sources to create a single compressed .mpkx file.
    """

    @property
    def description(self) -> str:
        return """

        PackageMap_management(in_map;in_map..., output_file, {convert_data}, {convert_arcsde_data}, {extent}, {apply_extent_to_arcsde}, {arcgisruntime}, {reference_all_data}, {version;version...}, {additional_files;additional_files...}, {summary}, {tags}, {select_related_rows}, {preserve_sqlite})

        Packages a map and all referenced data sources to create a single
        compressed .mpkx file.

     INPUTS:
      in_map (Map):
          The map to be packaged. When running this tool in ArcGIS Pro, the
          input can be a map, scene, or basemap.
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
      arcgisruntime {Boolean}:
          Specifies whether the package will support ArcGIS Maps SDKs. To
          support ArcGIS Maps SDKs, all data sources will be converted to a file
          geodatabase, and an .msd file will be created in the output
          package.DESKTOP-The output package will not support ArcGIS Maps SDKs.
          Unless
          otherwise specified, data sources will not be converted to a file
          geodatabase, and an .msd file will not be created.RUNTIME-The output
          package will support ArcGIS Maps SDKs. All data
          sources will be converted to a file geodatabase, and an .msd file will
          be created in the output package.
      reference_all_data {Boolean}:
          Specifies whether a package that references the necessary data will be
          created rather than copying the data. This is helpful when trying to
          package large datasets that are available from a central location in
          an organization.REFERENCED-A package that references the necessary
          data will be
          created rather than copying the data.NOT_REFERENCED-A package that
          contains the necessary data will be
          created. This is the default.
      version {String}:
          Specifies the version of the geodatabases that will be created
          in the resulting package. Specifying a version allows packages to be
          shared with earlier versions of ArcGIS and supports backward
          compatibility. A package saved to an earlier version may lose
          properties that are
          only available in the later version.ALL-The package will contain
          geodatabases and a map compatible with
          all versions (ArcGIS Pro 1.2 and later).CURRENT-The package will
          contain geodatabases and a map compatible
          with the version of the current ArcGIS Pro release.1.2-The package
          will contain geodatabases and a map compatible with
          ArcGIS Pro version 1.2 and later.2.x-The package will contain
          geodatabases and a map compatible with
          ArcGIS Pro version 2.0 and later.3.x-The package will contain
          geodatabases and a map compatible with
          ArcGIS Pro version 3.0 and later.
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
          geodatabase.CONVERT_SQLITE-Mobile geodatabase data will be converted
          to file
          geodatabase format. This is the default.PRESERVE_SQLITE-Mobile
          geodatabase data will be preserved in the
          output. The geodatabase will be included in its entirety.

     OUTPUTS:
      output_file (File):
          The output map package (.mpkx file).

        """