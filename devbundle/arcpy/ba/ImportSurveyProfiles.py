# Generated documentation for module arcpy.ba


class ImportSurveyProfiles(object):
    """
    Imports segmentation profiles consisting of survey variable data.
    """

    @property
    def description(self) -> str:
        return """

        ImportSurveyProfiles_ba(profiles;profiles..., out_folder)

        Imports segmentation profiles consisting of survey variable data.

     INPUTS:
      profiles (String):
          The categories of survey variables that can be selected for importing
          as profiles.
      out_folder (Folder):
          The folder that will contain the imported profiles.

        """