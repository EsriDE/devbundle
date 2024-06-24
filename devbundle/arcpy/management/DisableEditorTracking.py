# Generated documentation for module arcpy.management


class DisableEditorTracking(object):
    """
    Disables editor tracking on a feature class, table, feature dataset, or mosaic dataset.
    """

    @property
    def description(self) -> str:
        return """

        DisableEditorTracking_management(in_dataset, {creator}, {creation_date}, {last_editor}, {last_edit_date})

        Disables editor tracking on a feature class, table, feature dataset,
        or mosaic dataset.

     INPUTS:
      in_dataset (Dataset / Topology / Network Dataset):
          The feature class, table, feature dataset, or mosaic dataset in which
          editor tracking will be disabled.
      creator {Boolean}:
          Specifies whether editor tracking for the creator field will be
          disabled.DISABLE_CREATOR-Editor tracking for the creator field will be
          disabled. This is the default.NO_DISABLE_CREATOR-Editor tracking for
          the creator field will not be
          disabled.
      creation_date {Boolean}:
          Specifies whether editor tracking for the creation date field will be
          disabled.DISABLE_CREATION_DATE-Editor tracking for the creation date
          field will
          be disabled. This is the default.NO_DISABLE_CREATION_DATE-Editor
          tracking for the creation date field
          will not be disabled.
      last_editor {Boolean}:
          Specifies whether editor tracking for the last editor field will be
          disabled.DISABLE_LAST_EDITOR-Editor tracking for the last editor field
          will be
          disabled. This is the default.NO_DISABLE_LAST_EDITOR-Editor tracking
          for the last editor field will
          not be disabled.
      last_edit_date {Boolean}:
          Specifies whether editor tracking for the last edit date field will be
          disabled.DISABLE_LAST_EDIT_DATE-Editor tracking for the last edit date
          field
          will be disabled. This is the default.NO_DISABLE_LAST_EDIT_DATE-Editor
          tracking for the last edit date field
          will not be disabled.

        """