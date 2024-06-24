# Generated documentation for module arcpy.management


class RegisterAsVersioned(object):
    """
    Registers an enterprise geodatabase dataset as versioned.
    """

    @property
    def description(self) -> str:
        return """

        RegisterAsVersioned_management(in_dataset, {edit_to_base})

        Registers an enterprise geodatabase dataset as versioned.

     INPUTS:
      in_dataset (Table View / Feature Dataset):
          The dataset to be registered as versioned.
      edit_to_base {Boolean}:
          Specifies whether edits made to the default version will be moved to
          the base tables. This parameter is not applicable for branch
          versioning.NO_EDITS_TO_BASE-The dataset will not be versioned with the
          option of
          moving edits to base. This is the default.EDITS_TO_BASE-The dataset
          will be versioned with the option of moving
          edits to base.

        """