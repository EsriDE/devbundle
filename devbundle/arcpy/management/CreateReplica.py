# Generated documentation for module arcpy.management


class CreateReplica(object):
    """
    Creates a replica in a geodatabase from a specified list of feature classes, layers, datasets, and tables in an enterprise geodatabase.
    """

    @property
    def description(self) -> str:
        return """

        CreateReplica_management(in_data;in_data..., in_type, {out_geodatabase}, out_name, {access_type}, {initial_data_sender}, {expand_feature_classes_and_tables}, {reuse_schema}, {get_related_data}, {geometry_features}, {archiving}, {register_existing_data}, {out_type}, {out_xml}, {all_records_for_tables}, {out_filegdb_folder_path}, {out_filegdb_name})

        Creates a replica in a geodatabase from a specified list of feature
        classes, layers, datasets, and tables in an enterprise geodatabase.

     INPUTS:
      in_data (Table View / Dataset):
          The data to be replicated. This list consists of layers and tables
          referencing versioned, editable data from an enterprise geodatabase.
      in_type (String):
          Specifies the type of replica that will be created.TWO_WAY_REPLICA-
          Changes will be sent between child and parent
          replicas in both directions.ONE_WAY_REPLICA-Changes will be sent from
          the parent replica to the
          child replica only.CHECK_OUT-Data will be replicated, edited, and
          checked back in one
          time.ONE_WAY_CHILD_TO_PARENT_REPLICA-Changes will be sent from the
          child
          replica to the parent replica only.
      out_geodatabase {Workspace / GeoDataServer}:
          The geodatabase that will host the child replica. Geodata services are
          used to represent remote geodatabases. The geodatabase can be an
          enterprise or file geodatabase. For two-way and one-way-child-to-
          parent replicas, the child geodatabase must be an enterprise
          geodatabase. For one-way and checkout replicas, the geodatabase can be
          a file or enterprise geodatabase.This parameter is required if the
          out_type parameter is set to
          GEODATABASE.
      out_name (String):
          The name that identifies the replica.
      access_type {String}:
          Specifies the type of replica access.FULL-Complex types such as
          topologies, are supported and the data must
          be versioned. This is the default.SIMPLE-The data on the child is not
          versioned and must be simple. This
          allows the replica to be interoperable. Nonsimple features in the
          parent (for example, features in topologies) will be converted to
          simple features (for example, point, line, and polygon feature
          classes).
      initial_data_sender {String}:
          Specifies which replica will send changes when in disconnected mode.
          If you are working in a connected mode, this parameter is
          inconsequential. This ensures that the relative replica will not send
          updates until the changes are first received from the initial data
          sender.CHILD_DATA_SENDER-The child replica will be the initial data
          sender.
          This is the default.PARENT_DATA_SENDER-The parent replica will be the
          initial data sender.
      expand_feature_classes_and_tables {String}:
          Specifies whether expanded feature classes and tables-such as those in
          networks, topologies, or relationship classes-will be
          added.USE_DEFAULTS-The expanded feature classes and tables related to
          the
          feature classes and tables in the replica will be added. The default
          for feature classes is to replicate all features intersecting the
          spatial filter. If no spatial filter has been provided, all features
          will be included. The default for tables is to replicate the schema
          only. This is the default.ADD_WITH_SCHEMA_ONLY-Only the schema for the
          expanded feature classes
          and tables will be added.ALL_ROWS-All rows for expanded feature
          classes and tables will be
          added.DO_NOT_ADD-No expanded feature classes or tables will be added.
      reuse_schema {String}:
          Specifies whether a geodatabase that contains the schema of the data
          to be replicated will be reused. This reduces the amount of time
          required to replicate the data. This parameter is only available for
          checkout replicas.DO_NOT_REUSE-Schema will not be reused. This is the
          default.REUSE-Schema will be used.
      get_related_data {String}:
          Specifies whether rows related to rows existing in the replica will be
          replicated. For example, a feature (f1) is inside the replication
          filter and a related feature (f2) from another class is outside the
          filter. Feature f2 will be included in the replica if you choose to
          get related data.DO_NOT_GET_RELATED-Related data will not be
          replicated.GET_RELATED-Related data will be replicated. This is the
          default.
      geometry_features {Feature Layer}:
          The features that will be used to define the area to replicate.
      archiving {Boolean}:
          Specifies whether the archive class will be used to track changes
          instead of the versioning delta tables. This is only available for
          one-way replicas.ARCHIVING-Archiving will be used to track
          changes.DO_NOT_USE_ARCHIVING-Archiving will not be used to track
          changes. This
          is the default.
      register_existing_data {Boolean}:
          Specifies whether existing data in the child geodatabase will be used
          to register the replica datasets. The datasets in the child
          geodatabase must have the same names as the datasets in the parent
          geodatabase.REGISTER_EXISTING_DATA-Existing data in the child
          geodatabase will be
          used to register the replica.DO_NOT_USE_REGISTER_EXISTING_DATA-Data in
          the parent geodatabase will
          be copied to the child geodatabase. This is the default.
      out_type {String}:
          Specifies the output type of the data that will be
          replicated.GEODATABASE-The data will be replicated to an existing
          geodatabase.
          This is the default.XML_FILE-The data will be replicated to an XML
          workspace document.NEW_FILE_GEODATABASE-The data will be replicated to
          a new file
          geodatabase that will be created when the tool is run. Provide the
          location and name of the new file geodatabase in the
          out_filegdb_folder_path parameter. This option is only valid for one-
          way and checkout replicas.
      all_records_for_tables {Boolean}:
          Specifies whether all records or only the schema will be copied to the
          child geodatabase for tables that do not have filters applied (such as
          selections or definition queries).Tables with applied filters will be
          honored.ALL_RECORDS_FOR_TABLES-For tables with no applied filters, all
          records
          will be copied to the child geodatabase. This option will override the
          expand_feature_classes_and_tables parameter
          value.SCHEMA_ONLY_FOR_TABLES-For tables with no applied filters, only
          the
          schema will be copied to the child geodatabase. Tables with applied
          filters will be honored. This is the default.
      out_filegdb_folder_path {Folder}:
          The location of the file geodatabase that will be created to host the
          child replica. This parameter is required if the out_type parameter is
          set to NEW_FILE_GEODATABASE and is only valid for one-way and checkout
          replicas.
      out_filegdb_name {String}:
          The name of the file geodatabase that will be created to host the
          child replica. This parameter is required if the out_type parameter is
          set to NEW_FILE_GEODATABASE and is only valid for one-way and checkout
          replicas.

     OUTPUTS:
      out_xml {File}:
          The name and location of the .xml file that will be created.This
          parameter is required if the out_type parameter is set to
          XML_FILE.

        """