# Generated documentation for module arcpy.indoorpositioning


class CreateIPSDataModel(object):
    """
    Creates an IPS Data Model containing the following components:
    """

    @property
    def description(self) -> str:
        return """

        CreateIPSDataModel_indoorpositioning(target_workspace, coordinate_system, {setup_indoors_model_for_ips})

        Creates an IPS Data Model containing the following components:

     INPUTS:
      target_workspace (Workspace):
          The file or enterprise geodatabase where the IPS Data Model will be
          created.
      coordinate_system (Coordinate System):
          The spatial reference that will be used for the output IPS Data Model.
          The default is WGS84.
      setup_indoors_model_for_ips {Boolean}:
          Specifies whether an Indoors Information Model containing the feature
          classes-Sites, Facilities, Levels, Pathways. and Floor
          Transitions-will be created and configured.SETUP_INDOORS_MODEL-An
          Indoors Information Model and feature classes
          will be created and configured.NO_SETUP_INDOORS_MODEL-An Indoors
          Information Model and feature
          classes will not be created and configured. This is the default.

        """