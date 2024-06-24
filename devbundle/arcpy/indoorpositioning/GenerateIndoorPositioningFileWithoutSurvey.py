# Generated documentation for module arcpy.indoorpositioning


class GenerateIndoorPositioningFileWithoutSurvey(object):
    """
    Generates a positioning file from beacon and floor plan data by simulating Bluetooth signal propagation through the indoor environment.
    """

    @property
    def description(self) -> str:
        return """

        GenerateIndoorPositioningFileWithoutSurvey_indoorpositioning(target_positioning_table, in_beacon_features, in_ips_area_features, in_wall_features, in_facility_features, in_level_features, {in_ips_transition_features}, {in_comment})

        Generates a positioning file from beacon and floor plan data by
        simulating Bluetooth signal propagation through the indoor
        environment.

     INPUTS:
      target_positioning_table (Table View):
          The table where the generated positioning file will be stored as an
          attachment.
      in_beacon_features (Feature Layer):
          The point features representing the position and settings of Bluetooth
          beacons deployed in the indoor environment.
      in_ips_area_features (Feature Layer):
          The polygon features representing the area where the positioning data
          will be generated.
      in_wall_features (Feature Layer):
          The polygon features representing the physical extent of walls in and
          around the indoor positioning area.
      in_facility_features (Feature Layer):
          The polygon features representing Facilities footprints.
      in_level_features (Feature Layer):
          The polygon features representing Level footprints within the
          facilities.
      in_ips_transition_features {Feature Layer}:
          The line features representing entrance or exit transitions.
      in_comment {String}:
          A text comment that will be associated with the output positioning
          file.

        """