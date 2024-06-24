# Generated documentation for module arcpy.management


class PackageResult(object):
    """
    Packages one or more geoprocessing results, including all tools and input and output datasets, into a single compressed file (.gpkx).
    """

    @property
    def description(self) -> str:
        return """

        PackageResult_management(in_result;in_result..., output_file, {convert_data}, {convert_arcsde_data}, {extent}, {apply_extent_to_arcsde}, {schema_only}, {arcgisruntime}, {additional_files;additional_files...}, {summary}, {tags}, {version;version...}, {select_related_rows})

        Packages one or more geoprocessing results, including all tools and
        input and output datasets, into a single compressed file (.gpkx).

     INPUTS:
      in_result (String / File):
          The result that will be packaged.The input can be either a result from
          the history of the current
          project or a Result object's resultID property when the tool is being
          used in a Python script.
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
          Specifies whether all records for input and output datasets or only
          the schema of input and output datasets will be consolidated or
          packaged.ALL-All records for input and output datasets will be
          consolidated or
          packaged. This is the default.SCHEMA_ONLY-Only the schema of input
          and output datasets will be
          consolidated or packaged.
      arcgisruntime {Boolean}:
          Specifies whether the package will support ArcGIS Maps SDKs. To
          support ArcGIS Maps SDKs, all data sources will be converted to a file
          geodatabase.DESKTOP-The output package will not support ArcGIS Maps
          SDKs. This is
          the default.RUNTIME-The output package will support ArcGIS Maps SDKs.
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
      version {String}:
          Specifies the version of the geodatabases that will be created
          in the resulting package. Specifying a version allows packages to be
          shared with earlier versions of ArcGIS and supports backward
          compatibility. A package saved to an earlier version may lose
          properties that are
          only available in the later version.ALL-The package will contain
          geodatabases and maps compatible with
          all versions (ArcGIS Pro 2.1 and later).CURRENT-The package will
          contain geodatabases and maps compatible
          with the version of the current release.2.2-The package will contain
          geodatabases and maps compatible with
          version 2.2.2.3-The package will contain geodatabases and maps
          compatible with
          version 2.3.2.4-The package will contain geodatabases and maps
          compatible with
          version 2.4.2.5-The package will contain geodatabases and maps
          compatible with
          version 2.5.2.6-The package will contain geodatabases and maps
          compatible with
          version 2.6.2.7-The package will contain geodatabases and maps
          compatible with
          version 2.7.2.8-The package will contain geodatabases and maps
          compatible with
          version 2.8.2.9-The package will contain geodatabases and maps
          compatible with
          version 2.9.3.0-The package will contain geodatabases and maps
          compatible with
          version 3.0.3.1-The package will contain geodatabases and maps
          compatible with
          version 3.1.3.2-The package will contain geodatabases and maps
          compatible with
          version 3.2.3.3-The package will contain geodatabases and maps
          compatible with
          version 3.3.
      select_related_rows {Boolean}:
          Specifies whether the specified extent will be applied to related data
          sources.KEEP_ONLY_RELATED_ROWS-Only related data corresponding to
          records
          within the specified extent will be
          consolidated.KEEP_ALL_RELATED_ROWS-Related data sources will be
          consolidated in
          their entirety. This is the default.

     OUTPUTS:
      output_file (File):
          The name and location of the output package file (.gpkx).

        """