# Generated documentation for module arcpy.management


class RebuildIndexes(object):
    """
    Rebuild existing attribute or spatial indexes in enterprise geodatabases. Indexes can also be rebuilt on states and state_lineage geodatabase system tables and the delta tables of datasets that are registered to participate in traditional versioning. Out-of-date indexes can lead to poor query performance.
    """

    @property
    def description(self) -> str:
        return """

        RebuildIndexes_management(input_database, include_system, {in_datasets;in_datasets...}, {delta_only})

        Rebuild existing attribute or spatial indexes in enterprise
        geodatabases. Indexes can also be rebuilt on states and state_lineage
        geodatabase system tables and the delta tables of datasets that are
        registered to participate in traditional versioning. Out-of-date
        indexes can lead to poor query performance.

     INPUTS:
      input_database (Workspace):
          The connection (.sde file) to the database or geodatabase that
          contains the data for which you want to rebuild indexes.
      include_system (Boolean):
          Indicates whether indexes will be rebuilt on the states and state
          lineages tables.NO_SYSTEM-Indexes will not be rebuilt on the states
          and state
          lineages table. This is the default.SYSTEM-Indexes will be rebuilt on
          the states and state lineages
          tables.
      in_datasets {String}:
          Names of the datasets that will have their indexes rebuilt. Dataset
          names use paths relative to the input_database; full paths are not
          accepted as input.
      delta_only {Boolean}:
          Indicates how the indexes will be rebuilt on the selected datasets.
          This option has no effect if in_datasets is empty.This option only
          applies to geodatabases. If the input workspace is a
          database, this option will be ignored.ALL-Indexes will be rebuilt on
          all indexes for the selected datasets.
          This includes spatial indexes as well as user-created attribute
          indexes and any geodatabase-maintained indexes for the
          dataset.ONLY_DELTAS-Indexes will only be rebuilt for the delta tables
          of the
          selected datasets. This option can be used for cases where the
          business tables for the selected datasets are not updated often and
          there is a high volume of edits in the delta tables. This is the
          default.

        """