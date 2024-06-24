# Generated documentation for module arcpy.topographic


class ExtractDataByFeature(object):
    """
    Extracts features from multiple input feature classes into a target database.
    """

    @property
    def description(self) -> str:
        return """

        ExtractDataByFeature_topographic(in_datasets;in_datasets..., target_gdb, {reuse_schema}, {filter_feature}, {filter_type}, {checkout_replica}, {replica_name}, {expand_feature_classes_and_tables}, {get_related_data}, {excluded_rel_classes;excluded_rel_classes...}, {where_clause})

        Extracts features from multiple input feature classes into a target
        database.

     INPUTS:
      in_datasets (Value Table):
          A value table of rows that contain a dataset to extract and a filter
          option for that dataset. Specifying a filter option allows you to
          control how rows are replicated in each dataset. The following are the
          filter options:Dataset-The schema of the dataset will be extracted to
          the child
          workspace. Rows option-Specifies whether all rows, only the
          schema, or
          features that match filter criteria will be extracted.
          ALL_ROWS-All rows of the dataset will be extracted to the child
          workspace.SCHEMA_ONLY-Only the schema of the dataset will be extracted
          to the
          child workspace.USE_FILTERS-If a feature layer is specified for the
          filter_feature
          parameter, features that either intersect or are contained by features
          in the filter_feature parameter value will be extracted.
      target_gdb (Workspace / GeoDataServer):
          The workspace into which data will be extracted.
      reuse_schema {Boolean}:
          Specifies whether the schema of the data that will be extracted will
          be reused. This reduces the amount of time required to extract the
          data. This parameter is only supported for file geodatabases.REUSE-The
          schema will be reused.DO_NOT_REUSE-The schema will not be
          reused. This is the default.
      filter_feature {Layer}:
          A feature layer with one selected feature that will be used to limit
          the extent of the extracted data.
      filter_type {String}:
          Specifies the spatial relationship between the filter_feature and
          in_datasets parameter values and how that relationship will be
          filtered. The spatial relationship is applied to data in an extent
          defined by the area of interest (AOI) specified in the filter_feature
          parameter.INTERSECTS-Features in the in_datasets parameter value that
          intersect
          features in the filter_feature parameter value will be
          extracted.CONTAINS-Features in the in_datasets parameter value that
          are
          contained by the selected feature in the filter_feature parameter
          value will be extracted.CLIP-Features in the in_datasets parameter
          value that intersect
          features in the filter_feature parameter value will be extracted, the
          features will be split at the AOI boundary, and only the features
          within the AOI will be kept.
      checkout_replica {Boolean}:
          Specifies whether the replica will be checked out, replicated, edited,
          and checked back in one time.CHECKOUT_REPLICA-The replica will be
          checked
          out.DO_NOT_CHECKOUT_REPLICA-The replica will not be checked out. This
          is
          the default.
      replica_name {String}:
          The name of the replica that will be checked out.
      expand_feature_classes_and_tables {String}:
          Specifies whether expanded feature classes and tables-such as those in
          networks, topologies, or relationship classes-will be
          added.USE_DEFAULTS-The expanded feature classes and tables related to
          the
          feature classes and tables in the replica will be added. The default
          for feature classes is to replicate all features intersecting the
          spatial filter. If no spatial filter has been provided, all features
          are included. The default for tables is to replicate only the
          schema.ADD_WITH_SCHEMA_ONLY-Only the schema for the expanded feature
          classes
          and tables will be added.ALL_ROWS-All rows for expanded feature
          classes and tables will be
          added.DO_NOT_ADD-No expanded feature classes and tables will be added.
          This
          is the default.
      get_related_data {Boolean}:
          Specifies whether rows related to existing rows in the replica will be
          replicated. For example, consider a feature (f1) inside the
          replication filter and a related feature (f2) from another class
          outside the filter. Feature f2 will be included in the replica if you
          choose to get related data.DO_NOT_GET_RELATED-Related data will not be
          replicated. This is the
          default.GET_RELATED-Related data will be replicated.
      excluded_rel_classes {Relationship Class}:
          The relationship classes with the relationships to exclude from
          extraction. The relationship classes will still be included if both
          datasets that participate are present, but the related objects are not
          extracted.
      where_clause {SQL Expression}:
          An SQL expression that is used to further refine results from the AOI
          extraction.

        """