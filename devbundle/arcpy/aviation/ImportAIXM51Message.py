# Generated documentation for module arcpy.aviation


class ImportAIXM51Message(object):
    """
    Imports Aeronautical Information Exchange Model (AIXM) version 5.1 data into an aviation geodatabase.
    """

    @property
    def description(self) -> str:
        return """

        ImportAIXM51Message_aviation(in_message_file, target_gdb, {in_tables;in_tables...}, {update_existing_features})

        Imports Aeronautical Information Exchange Model (AIXM) version 5.1
        data into an aviation geodatabase.

     INPUTS:
      in_message_file (File):
          The input AIXM 5.1 message.
      target_gdb (Workspace):
          The ArcGIS Aviation Charting schema workspace where the AIXM message
          will be imported.
      in_tables {String}:
          The names of tables used to restrict the feature types that will be
          imported.
      update_existing_features {Boolean}:
          Specifies whether existing features will be updated or new features
          will be inserted.UPDATE_EXISTING-Existing features will be
          updated.CREATE_NEW-Existing
          features will not be updated; new features will be
          inserted. This is the default.

        """