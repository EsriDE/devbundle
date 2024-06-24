# Generated documentation for module arcpy.ba


class CreateTargetGroup(object):
    """
    Creates a new target group. A target group is a container for targets that you create, name, and populate with segments from a locally installed Business Analyst dataset.
    """

    @property
    def description(self) -> str:
        return """

        CreateTargetGroup_ba(target_group, input_type;input_type...)

        Creates a new target group. A target group is a container for targets
        that you create, name, and populate with segments from a locally
        installed Business Analyst dataset.

     INPUTS:
      input_type (Value Table):
          Specifies a list of the targets to be added to the new target
          group.name-The name of the target.segments-The segments to be added to
          the
          target.color-The color associated with the segment.

     OUTPUTS:
      target_group (File):
          The name for the output target group file.

        """