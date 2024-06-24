# Generated documentation for module arcpy.td


class LoadTerritoryRecords(object):
    """
    Adds records (features) or updates existing records for the specified level.
    """

    @property
    def description(self) -> str:
        return """

        LoadTerritoryRecords_td(in_territory_solution, level, in_data, {id_field}, {name_field}, {field_map;field_map...}, {append_data})

        Adds records (features) or updates existing records for the specified
        level.

     INPUTS:
      in_territory_solution (Group Layer / Feature Dataset / String):
          The name of the input territory solution.
      level (String):
          The name of the level to which the data will be loaded.
      in_data (Table View):
          The layer or records to be loaded.
      id_field {Field}:
          The field containing the ID values to be loaded into the level.
      name_field {Field}:
          The field containing the name values to be loaded into the level.
      field_map {Value Table}:
          The values for the territory properties.parent_territory_id-The ID of
          the parent territory.locked_state-The
          territory can't be modified.center_locked-Center points can't be
          modified and will remain in their
          fixed locations.
      append_data {Boolean}:
          Specifies whether the records being loaded will be appended or
          replaced.APPEND-The records being loaded to the specified level will
          be
          appended.REPLACE-The records being loaded to the specified level will
          be
          replaced. This is the default.

        """