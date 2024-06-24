# Generated documentation for module arcpy.management


class ExtractDataFromGeodatabase(object):
    """
    Extracts a subset of data from one geodatabase to another geodatabase or an .xml file.
    """

    @property
    def description(self) -> str:
        return """

        ExtractDataFromGeodatabase_management(in_data;in_data..., {extract_type}, {out_type}, {out_geodatabase}, {out_xml}, {out_folder_path}, {out_name}, {expand_feature_classes_and_tables}, {reuse_schema}, {get_related_data}, {extract_using_geometry_features}, {geometry_filter_type}, {all_records_for_tables})

        Extracts a subset of data from one geodatabase to another geodatabase
        or an .xml file.

     INPUTS:
      in_data (Table View / Dataset):
          The data that will be extracted.
      extract_type {String}:
          Specifies whether the schema and rows of the data or only the schema
          will be extracted.DATA-The schema and rows will be extracted. This is
          the
          default.SCHEMA_ONLY-Only the schema will be extracted.
      out_type {String}:
          Specifies the output type the data will be extracted
          to.GEODATABASE-The data will be extracted to an existing geodatabase.
          This is the default.XML_FILE-The data will be extracted to an XML
          workspace document.NEW_FILE_GEODATABASE-The data will be extracted to
          a new file
          geodatabase. Specify the location and name of the new file geodatabase
          using the out_folder_path and out_name parameters.
      out_geodatabase {Workspace}:
          The geodatabase that will contain the extracted data when the out_type
          parameter is set to GEODATABASE.
      out_folder_path {Folder}:
          The location of the file geodatabase that will be created for the
          extracted data. This parameter is required when the out_type parameter
          is set to NEW_FILE_GEODATABASE.
      out_name {String}:
          The name of the file geodatabase that will be created for the
          extracted data. This parameter is required when the out_type parameter
          is set to NEW_FILE_GEODATABASE.
      expand_feature_classes_and_tables {String}:
          Specifies whether expanded feature classes and tables-such as those in
          networks, topologies, or relationship classes-will be
          added.USE_DEFAULTS-The expanded feature classes and tables related to
          the
          feature classes and tables in the input datasets will be added. The
          default for feature classes is to extract all features intersecting
          the spatial filter. If no spatial filter has been provided, all
          features will be included. The default for tables is to extract the
          schema only. This is the default.ADD_WITH_SCHEMA_ONLY-Only the schema
          for the expanded feature classes
          and tables will be added.ALL_ROWS-All rows for expanded feature
          classes and tables will be
          added.DO_NOT_ADD-No expanded feature classes or tables will be added.
      reuse_schema {String}:
          Specifies whether a geodatabase that contains the schema of the data
          to be extracted will be reused. Reusing the schema reduces the amount
          of time required to extract the data.DO_NOT_REUSE-The schema will not
          be reused. This is the
          default.REUSE-The schema will be reused.
      get_related_data {String}:
          Specifies whether rows related to rows existing in the data will be
          extracted. For example, a feature (f1) is inside the geometry filter
          and a related feature (f2) from another class is outside the filter.
          Feature f2 will be included in the extracted data if you choose to get
          related data.DO_NOT_GET_RELATED-Related data will not be
          extracted.GET_RELATED-Related data will be extracted. This is the
          default.
      extract_using_geometry_features {Feature Layer}:
          The features that will be used to define the area to extract.
      geometry_filter_type {String}:
          Specifies the spatial relationship between the
          extract_using_geometry_features and in_data parameter values and how
          that relationship will be filtered. The spatial relationship is
          applied to data in an extent defined by the area of interest (AOI)
          specified in the extract_using_geometry_features
          parameter.INTERSECTS-Features in the in_data parameter value that
          intersect
          features in the extract_using_geometry_features parameter value will
          be extracted.CONTAINS-Features in the in_data parameter value that are
          contained by
          the selected feature in the extract_using_geometry_features parameter
          value will be extracted.
      all_records_for_tables {Boolean}:
          Specifies whether all records or only the schema will be extracted for
          tables that do not have filters applied (such as selections or
          definition queries).Tables with applied filters will be
          honored.ALL_RECORDS_FOR_TABLES-All records will be extracted to the
          geodatabase. This option will override the
          expand_feature_classes_and_tables parameter
          value.SCHEMA_ONLY_FOR_TABLES-Only the schema will be extracted to the
          geodatabase. This is the default.

     OUTPUTS:
      out_xml {File}:
          The name and location of the .xml file that will be created when the
          out_type parameter is set to XML_FILE.

        """