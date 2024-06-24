# Generated documentation for module arcpy.na


class BuildNetwork(object):
    """
    Reconstructs the network connectivity and attribute information of a network dataset. The network dataset must be rebuilt after edits are made to the attributes or the features of a participating source feature class. After the source features are edited, the tool establishes the network connectivity only in the areas that have been edited to speed up the build process; however, when the network attributes are edited, the entire extent of the network dataset is rebuilt. This may be a slow operation on a large network dataset.
    """

    @property
    def description(self) -> str:
        return """

        BuildNetwork_na(in_network_dataset, {force_full_build})

        Reconstructs the network connectivity and attribute information of a
        network dataset. The network dataset must be rebuilt after edits are
        made to the attributes or the features of a participating source
        feature class. After the source features are edited, the tool
        establishes the network connectivity only in the areas that have been
        edited to speed up the build process; however, when the network
        attributes are edited, the entire extent of the network dataset is
        rebuilt. This may be a slow operation on a large network dataset.

     INPUTS:
      in_network_dataset (Network Dataset Layer):
          The network dataset to be built.
      force_full_build {Boolean}:
          Specifies whether the full network will be built or only the parts of
          the network in dirty areas.FORCE_FULL_BUILD-The full network will be
          built.NO_FORCE_FULL_BUILD-Only the parts of the network that have been
          changed since the last build will be built. This is the default.

        """