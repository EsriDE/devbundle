# Generated documentation for module arcpy.td


class AddTerritorySeedPoints(object):
    """
    Creates a point feature that is used to determine the starting point for creating territories.
    """

    @property
    def description(self) -> str:
        return """

        AddTerritorySeedPoints_td(in_territory_solution, level, in_seed_points, {field_map;field_map...}, {append_data})

        Creates a point feature that is used to determine the starting point
        for creating territories.

     INPUTS:
      in_territory_solution (Group Layer / Feature Dataset / String):
          The Territory Design solution dataset.
      level (String):
          The target territory level for which the seed points feature will be
          created.
      in_seed_points (Feature Layer):
          The points feature layer that represents seed points for territories.
      field_map {Value Table}:
          Specifies the attributes and fields that will be used for the seed
          point properties.Name-The name for a seed point featureID-The ID for a
          seed point
          featureType-The seed point typeThe field value associated with the
          Type attribute can only be
          Required or Candidate.
      append_data {Boolean}:
          Specifies whether the data will be appended or replaced.APPEND-The
          data will be appended.REPLACE-The data will be replaced.
          This is the default.

        """