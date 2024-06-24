# Generated documentation for module arcpy.management


class UnregisterAsVersioned(object):
    """
    Unregisters an enterprise geodatabase dataset as versioned.
    """

    @property
    def description(self) -> str:
        return """

        UnregisterAsVersioned_management(in_dataset, {keep_edit}, {compress_default})

        Unregisters an enterprise geodatabase dataset as versioned.

     INPUTS:
      in_dataset (Table View / Feature Dataset):
          The name of the dataset to be unregistered as versioned.
      keep_edit {Boolean}:
          Specifies whether edits made to the versioned data will be
          maintained.KEEP_EDIT-When there are outstanding edits that could be
          lost, the
          tool will fail. Outstanding edits include edits in the delta tables
          (traditional versioned dataset) and edits in named versions (branch
          versioned dataset). This is the default. For traditional versioned
          datasets, do not use this option when compressing edits from the
          Default version in the compress_default parameter.NO_KEEP_EDIT-When
          there are outstanding edits, the tool will delete
          the edits. For traditional versioned datasets, use this option when
          compressing edits from the Default version in the compress_default
          parameter.
      compress_default {Boolean}:
          Specifies whether edits will be compressed and unused data will be
          removed. This option is ignored if the keep_edit parameter is set to
          KEEP_EDIT.This parameter is only applicable for traditional versioned
          datasets.COMPRESS_DEFAULT-Edits in the Default version will be
          compressed to
          the base table.NO_COMPRESS_DEFAULT-Any edits remaining in the delta
          tables will not
          be compressed. This is the default.

        """