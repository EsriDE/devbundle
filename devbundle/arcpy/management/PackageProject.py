# Generated documentation for module arcpy.management


class PackageProject(object):
    """
    Consolidates and packages a project file (.aprx) of referenced maps and data to a packaged project file (.ppkx).
    """

    @property
    def description(self) -> str:
        return """

        PackageProject_management(in_project, output_file, {sharing_internal}, {package_as_template}, {extent}, {apply_extent_to_arcsde}, {additional_files;additional_files...}, {summary}, {tags}, {version;version...}, {include_toolboxes}, {include_history_items}, {read_only}, {select_related_rows}, {preserve_sqlite})

        Consolidates and packages a project file (.aprx) of referenced maps
        and data to a packaged project file (.ppkx).

     INPUTS:
      in_project (File):
          The project (.aprx file) to be packaged.
      sharing_internal {Boolean}:
          Specifies whether the project will be consolidated for your internal
          environment or will move all data elements so it can be shared
          externally.INTERNAL-Enterprise data sources, such as enterprise
          geodatabases and
          data from a UNC path, will not be copied to the local folder. This is
          the default.EXTERNAL-Data formats will be copied and preserved when
          possible.
      package_as_template {Boolean}:
          Specifies whether a project template or a project package will be
          created. Project templates can include maps, layouts, connections to
          databases and servers, and so on. A project template can be used to
          standardize a series of maps for different projects and to ensure that
          the correct layers are immediately available for everyone to use in
          their maps.PROJECT_PACKAGE-A project package will be created. This is
          the
          default.PROJECT_TEMPLATE-A project template will be created
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
          default.ENTERPRISE_ONLY-The specified extent will be applied to
          enterprise
          geodatabase layers only.
      additional_files {File}:
          The additional files that will be added to a package. Additional
          files, such as .doc, .txt, .pdf, and so on, are used to provide more
          information about the contents and purpose of the package.
      summary {String}:
          The summary information that will be added to the properties of the
          package.
      tags {String}:
          The tags that will be added to the properties of the package. Separate
          multiple tags with a comma or semicolon.
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
      include_toolboxes {Boolean}:
          Specifies whether project toolboxes will be consolidated and included
          in the output package. All projects require a default toolbox, and the
          default toolbox will be included regardless of this
          setting.TOOLBOXES-Project toolboxes will be included in the output
          package.
          This is the default.NO_TOOLBOXES-Project toolboxes will not be
          included in the output
          package.
      include_history_items {String}:
          Specifies whether geoprocessing history items will be consolidated and
          included in the output package. Included history items will
          consolidate the data required to reprocess the history
          item.HISTORY_ITEMS-History items will be included in the output
          package.
          This is the default.NO_HISTORY_ITEMS-History items will not be
          included in the output
          package.VALID_HISTORY_ITEMS_ONLY-Only valid history items will be
          included in
          the output package. History items are invalid if any of the original
          input layers or tools cannot be found.
      read_only {Boolean}:
          Specifies whether the project will be read-only. Read-only projects
          cannot be modified or saved.READ_ONLY-The project will be read-
          only.READ_WRITE-The project will be
          writable. This is the default.
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
          The output project package (.ppkx file).

        """