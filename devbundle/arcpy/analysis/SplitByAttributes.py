# Generated documentation for module arcpy.analysis


class SplitByAttributes(object):
    """
    Splits an input dataset by unique attributes.
    """

    @property
    def description(self) -> str:
        return """

        SplitByAttributes_analysis(Input_Table, Target_Workspace, Split_Fields;Split_Fields...)

        Splits an input dataset by unique attributes.

     INPUTS:
      Input_Table (Table View):
          The input feature class or table containing the data that will be
          split into the target workspace.
      Target_Workspace (Workspace / Feature Dataset):
          The existing workspace where the output feature classes or tables will
          be written.
      Split_Fields (Field):
          The fields on which the input will be split into new feature classes
          or tables.

        """