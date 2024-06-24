# Generated documentation for module arcpy.management


class ReconcileVersions(object):
    """
    Reconciles a version or multiple versions with a target version.
    """

    @property
    def description(self) -> str:
        return """

        ReconcileVersions_management(input_database, reconcile_mode, {target_version}, {edit_versions;edit_versions...}, {acquire_locks}, {abort_if_conflicts}, {conflict_definition}, {conflict_resolution}, {with_post}, {with_delete}, {out_log}, {proceed_if_conflicts_not_reviewed}, {reconcile_checkout_versions})

        Reconciles a version or multiple versions with a target version.

     INPUTS:
      input_database (Workspace):
          The enterprise geodatabase that contains the versions to be
          reconciled. The default is to use the geoprocessing workspace
          environment.For branch versioning, this will be the feature service
          URL (that is,
          https://mysite.mydomain/server/rest/services/ElectricNetwork/FeatureSe
          rver).
      reconcile_mode (String):
          Specifies the versions that will be reconciled when the tool is run.If
          the input is a branch workspace, the only valid option for this
          parameter is to reconcile all versions.ALL_VERSIONS-Edit versions will
          be reconciled with the target version.
          This is the default.BLOCKING_VERSIONS-Versions that are blocking the
          target version from
          compressing will be reconciled. This option uses the recommended
          reconcile order.
      target_version {String}:
          The name of any version in the direct ancestry of the edit version,
          such as the parent version or the default version.It typically
          contains edits from other versions that you want included
          in the edit version.If the input is a branch workspace, the only valid
          option for this
          parameter is to reconcile with the default version.
      edit_versions {String}:
          The name of the edit version or versions to be reconciled with the
          selected target version. This can be an individual version name or a
          list of version names.
      acquire_locks {Boolean}:
          Specifies whether feature locks will be acquired.LOCK_ACQUIRED-Locks
          will be acquired during the reconcile process. Use
          this option when the intention is to post edits. It ensures that the
          target version is not modified in the time between the reconcile and
          post operations. This is the default.NO_LOCK_ACQUIRED-Locks will not
          be acquired during the reconcile
          process. This allows multiple users to reconcile in parallel. Use this
          option when the edit version will not be posted to the target version
          because there is a possibility that the target version may be modified
          in the time between the reconcile and post operations.
      abort_if_conflicts {Boolean}:
          Specifies whether the reconcile process will be aborted if conflicts
          are found between the target version and the edit version during the
          reconcile process.NO_ABORT-The reconcile will not be aborted if
          conflicts are found.
          This is the default.ABORT_CONFLICTS-The reconcile will be aborted if
          conflicts are found.
      conflict_definition {String}:
          Specifies whether the conditions required for a conflict to occur will
          be defined by object (row) or by attribute
          (column).BY_OBJECT-Conflicts will be defined by object. Any changes to
          the same
          row or feature in the parent and child versions will conflict during
          reconcile. This is the default.BY_ATTRIBUTE-Conflicts will be defined
          by attribute. Only changes to
          the same attribute (column) of the same row or feature in the parent
          and child versions will be flagged as a conflict during reconcile.
          Changes to different attributes will not be considered a conflict
          during reconcile.
      conflict_resolution {String}:
          Specifies the resolution that will be used if a conflict is
          detected.If the input is a branch workspace, the default is to favor
          the edit
          version.FAVOR_TARGET_VERSION-All conflicts will be resolved in favor
          of the
          target version. This is the default for traditional
          versioning.FAVOR_EDIT_VERSION-All conflicts will be resolved in favor
          of the edit
          version. This is the default for branch versioning.
      with_post {Boolean}:
          Specifies whether the current edit session will be posted to the
          reconciled target version.NO_POST-The current edit version will not be
          posted to the target
          version after the reconcile. This is the default.POST-The current edit
          version will be posted to the target version
          after the reconcile.
      with_delete {Boolean}:
          Specifies whether the reconciled edit version will be deleted after
          posting. This parameter only applies if the with_post parameter is set
          to POST.DELETE_VERSION-The current edit version that was reconciled
          will be
          deleted after being posted to the target version.KEEP_VERSION-The
          current edit version that was reconciled will not be
          deleted. This is the default.
      proceed_if_conflicts_not_reviewed {Boolean}:
          Specifies whether the reconcile will proceed if existing unreviewed
          conflicts are detected before the reconcile process starts. If you
          proceed, existing conflicts from previous sessions will be lost when
          the tool runs. This parameter is only applicable to branch
          versioning.PROCEED-The reconcile process will proceed if existing
          unreviewed
          conflicts are detected. This is the default.NOT_PROCEED-The reconcile
          process will not proceed if existing
          unreviewed conflicts are detected.
      reconcile_checkout_versions {Boolean}:
          Specifies whether the reconcile process will include checkout replica
          versions. If you are creating a checkout replica as part of a
          geodatabase replication workflow, an associated version is created in
          the geodatabase. This option allows you to include or remove these
          types of versions from the list of versions to be reconciled. This
          parameter is not applicable for branch versioning.RECONCILE-The
          reconcile process will include checkout replica
          versions. This is the default.DO_NOT_RECONCILE-The reconcile process
          will not include checkout
          replica versions.

     OUTPUTS:
      out_log {File}:
          The name and location where the log file will be written. The log file
          is an ASCII file containing the contents of the geoprocessing
          messages.

        """