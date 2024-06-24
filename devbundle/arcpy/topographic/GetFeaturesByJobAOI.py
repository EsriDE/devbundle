# Generated documentation for module arcpy.topographic


class GetFeaturesByJobAOI(object):
    """
    Extracts features from a source geodatabase to a target geodatabase based on the Filter Feature Layer parameter value (or job AOI).
    """

    @property
    def description(self) -> str:
        return """

        GetFeaturesByJobAOI_topographic(job_id, source_database, target_database, extract_operation, {filter_feature}, {filter_type}, {replica_type}, {database_path})

        Extracts features from a source geodatabase to a target geodatabase
        based on the Filter Feature Layer parameter value (or job AOI).

     INPUTS:
      job_id (Long):
          The job ID of the Workflow Manager (Classic) job that will be updated.
          The default area over which features will be extracted or replicated
          is also determined.
      source_database (Workspace):
          The path to the source database containing features to extract.
      target_database (Workspace):
          The database from which features will be extracted.
      extract_operation (String):
          Specifies whether the data will be copied to the target database or
          replicated to the target database.EXTRACT_DATA-A copy of the features
          will be extracted to the target
          database. This is the default.REPLICATE_DATA-The features will be
          extracted as a replica.
      filter_feature {Feature Layer}:
          A feature layer with one selected feature that will be used to limit
          the extent of the data that will be extracted. If no filter feature is
          specified, the job AOI will be used.
      filter_type {String}:
          Specifies the spatial relationship between the source_database and
          filter_feature parameter values. This parameter is only used if the
          extract_operation parameter is set to EXTRACT_DATA.INTERSECTS-Features
          from the source_database parameter value that
          intersect features in the filter_feature parameter value will be
          extracted. This is the default.CONTAINS-Features from the
          source_database parameter value that are
          contained in the selected feature in the filter_feature parameter
          value will be extracted.CLIP-Features from the source_database
          parameter value that intersect
          features in the filter_feature parameter value will be extracted.
          Features are then split at the AOI boundary and only those within the
          AOI boundary will be kept.
      replica_type {String}:
          Specifies the type of replica that will be created. This parameter is
          only used if the extract_operation parameter is set to
          REPLICATE_DATA.TWO_WAY_REPLICA-Changes will be sent between child and
          parent replicas
          in both directions.ONE_WAY_REPLICA-Changes will be sent from the
          parent replica to the
          child replica only.CHECK_OUT-Data will be replicated, edited, and
          checked back in one
          time. This is the default.ONE_WAY_CHILD_TO_PARENT_REPLICA-Changes will
          be sent from the child
          replica to the parent replica only.
      database_path {File}:
          The Workflow Manager (Classic) database connection file (.jtc) that
          contains the job information. If no connection file is specified, the
          current default Workflow Manager (Classic) database will be used.

        """