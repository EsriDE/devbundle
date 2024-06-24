# Generated documentation for module arcpy.management


class ValidateSceneLayerPackage(object):
    """
    Evaluates a scene layer package (*.slpk or *.i3sREST) in a cloud store to determine its conformity to I3S specifications.
    """

    @property
    def description(self) -> str:
        return """

        ValidateSceneLayerPackage_management({in_slpk}, out_report, {in_folder})

        Evaluates a scene layer package (*.slpk or *.i3sREST) in a cloud store
        to determine its conformity to I3S specifications.

     INPUTS:
      in_slpk {File}:
          The scene layer package (*.slpk) that will be evaluated.
      in_folder {Folder}:
          The scene layer content (*.i3sREST) in a cloud store that will be
          evaluated.

     OUTPUTS:
      out_report (File):
          The output log file that will summarize the results of the evaluation.

        """