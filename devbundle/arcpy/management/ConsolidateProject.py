# Generated documentation for module arcpy.management


class ConsolidateProject(object):
    """
    Consolidates a project (an .aprx file) and referenced maps and data into a specified output folder.
    """

    @property
    def description(self) -> str:
        return """

        ConsolidateProject_management(in_project, output_folder, {sharing_internal}, {extent}, {apply_extent_to_enterprise_geo}, {package_as_template}, {preserve_sqlite}, {version}, {select_related_rows})

        Consolidates a project (an .aprx file) and referenced maps and data
        into a specified output folder.

     INPUTS:
      in_project (File):
          The project (.aprx file) to be consolidated.
      sharing_internal {Boolean}:
          Specifies whether the project and all data will be consolidated into
          the output folder so it can be shared externally. INTERNAL-
          The project and its data sources
          will not be consolidated
          into the output folder. This is the default. This parameter
          applies to enterprise geodatabase data sources,
          including enterprise geodatabases and folders referenced through a UNC
          path.EXTERNAL-The project and its data sources will be consolidated
          (copied) into the output folder when possible.
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
      apply_extent_to_enterprise_geo {Boolean}:
          Specifies whether the extent parameter value will be applied to all
          layers or to enterprise geodatabase layers only.ALL-The extent will
          be applied to all layers. This is the
          default.ENTERPRISE_ONLY-The extent will be applied to enterprise
          geodatabase
          layers only.
      package_as_template {Boolean}:
          Specifies whether the project will be consolidated as a template or a
          regular project. Templates can include maps, layouts, connections to
          databases and servers, and so on. A project template allows you to
          standardize a series of maps for use in a project and ensure that the
          correct layers are immediately available for use.PROJECT_PACKAGE-The
          project will be consolidated as a project into a
          folder. This is the default.PROJECT_TEMPLATE-The project will be
          consolidated as a template into a
          folder
      preserve_sqlite {Boolean}:
          Specifies whether mobile geodatabases will be preserved or
          converted to file geodatabases. This parameter applies only to
          mobile geodatabases (.geodatabase) used
          primarily for offline workflows in ArcGIS Runtime apps. SQLite
          databases with .sqlite or .gpkg file extensions will be converted to
          file geodatabases.CONVERT_SQLITE-Mobile geodatabases will be converted
          to file
          geodatabases. This is the default.PRESERVE_SQLITE-Mobile geodatabases
          will be preserved.
      version {String}:
          Specifies the ArcGIS Pro version that the consolidated project will be
          saved as. Saving to an earlier version will ensure tool backward
          compatibility. If you attempt to consolidate a toolbox to an earlier
          version and capabilities that are only available in the newer version
          are included, an error will occur. You must remove tools that are
          incompatible with the earlier version, or specify a compatible
          version.CURRENT-The consolidated folder will contain geodatabases and
          maps
          compatible with the version of the current release.2.2-The
          consolidated folder will contain geodatabases and maps
          compatible with version 2.2.2.3-The consolidated folder will contain
          geodatabases and maps
          compatible with version 2.3.2.4-The consolidated folder will contain
          geodatabases and maps
          compatible with version 2.4.2.5-The consolidated folder will contain
          geodatabases and maps
          compatible with version 2.5.2.6-The consolidated folder will contain
          geodatabases and maps
          compatible with version 2.6.2.7-The consolidated folder will contain
          geodatabases and maps
          compatible with version 2.7.2.8-The consolidated folder will contain
          geodatabases and maps
          compatible with version 2.8.2.9-The consolidated folder will contain
          geodatabases and maps
          compatible with version 2.9.3.0-The consolidated folder will contain
          geodatabases and maps
          compatible with version 3.0.3.1-The consolidated folder will contain
          geodatabases and maps
          compatible with version 3.1.3.2-The consolidated folder will contain
          geodatabases and maps
          compatible with version 3.2.3.3-The consolidated folder will contain
          geodatabases and maps
          compatible with version 3.2.
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
          The output folder that will contain the consolidated project and data.
          If the specified folder does not exist, a folder will be created.

        """