# Generated documentation for module arcpy.management


class SynchronizeChanges(object):
    """
    Synchronizes updates between two replica geodatabases in a specified direction.
    """

    @property
    def description(self) -> str:
        return """

        SynchronizeChanges_management(geodatabase_1, in_replica, geodatabase_2, in_direction, conflict_policy, conflict_definition, reconcile)

        Synchronizes updates between two replica geodatabases in a specified
        direction.

     INPUTS:
      geodatabase_1 (Workspace / GeoDataServer):
          The geodatabase hosting the replica to synchronize. The geodatabase
          can be local or remote.
      in_replica (String):
          A valid replica with a parent contained in one input geodatabase and a
          child in the other input geodatabase.
      geodatabase_2 (Workspace / GeoDataServer):
          The geodatabase hosting the relative replica. The geodatabase can be
          local or remote.
      in_direction (String):
          Specifies the direction in which the changes will be synchronized:
          from geodatabase 1 to geodatabase 2, from geodatabase 2 to geodatabase
          1, or in both directions. For check-out/check-in replicas or one-way
          replicas, there is only one appropriate direction. If the replica is
          two-way, all of the choices are available.BOTH_DIRECTIONS-Changes will
          be synchronized in both directions. This
          is the default.FROM_GEODATABASE2_TO_1-Changes will be synchronized
          from geodatabase 2
          to geodatabase 1.FROM_GEODATABASE1_TO_2-Changes will be synchronized
          from geodatabase 1
          to geodatabase 2.
      conflict_policy (String):
          Specifies how conflicts will be resolved when they are
          encountered.MANUAL-Conflicts will be resolved manually in the
          versioning reconcile
          environment.IN_FAVOR_OF_GDB1-Conflicts will be resolved in favor of
          geodatabase 1.
          This is the default.IN_FAVOR_OF_GDB2-Conflicts will be resolved in
          favor of geodatabase 2.
      conflict_definition (String):
          Specifies how conflicts will be defined.BY_OBJECT-Changes to the same
          row or feature in the parent and child
          versions will conflict during reconcile. This is the
          default.BY_ATTRIBUTE-Only changes to the same attribute (column) of
          the same
          row or feature in the parent and child versions will be flagged as a
          conflict during reconcile. Changes to different attributes will not be
          considered a conflict during reconcile.
      reconcile (Boolean):
          Specifies whether to automatically reconcile once data changes are
          sent to the parent replica if there are no conflicts present. This
          option is only available for check-out/check-in
          replicas.DO_NOT_RECONCILE-Do not reconcile with the parent version.
          This is the
          default.RECONCILE-Reconcile with the parent version.

        """