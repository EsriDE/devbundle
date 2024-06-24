# Generated documentation for module arcpy.indoors


class GenerateUnitOpenings(object):
    """
    Creates unit openings as line features that model the location and physical extent of an entrance.
    """

    @property
    def description(self) -> str:
        return """

        GenerateUnitOpenings_indoors(in_unit_features, in_detail_features, door_detail_expression, wall_detail_expression, target_openings, {wall_thickness_tolerance}, {delete_existing_openings})

        Creates unit openings as line features that model the location and
        physical extent of an entrance.

     INPUTS:
      in_unit_features (Feature Layer):
          The input polygon features representing unit footprints for one or
          more facilities. In the Indoors model, this is the Units layer. The
          tool only processes the levels that contain the selected features.
      in_detail_features (Feature Layer):
          The input polyline features representing the architectural detail
          polylines.
      door_detail_expression (SQL Expression):
          An SQL expression used to identify which detail polylines represent
          doors.
      wall_detail_expression (SQL Expression):
          An SQL expression used to identify which detail polylines represent
          walls.
      target_openings (Feature Layer):
          The existing polyline feature class or feature layer to which
          generated polylines will be written. In the Indoors model this is the
          Details layer.
      wall_thickness_tolerance {Linear Unit}:
          The distance that will be searched inward and outward from the edge of
          a unit feature to find a door feature. The default unit of measurement
          is feet. The default value is 2 feet but can range from 0 to 6 feet.
      delete_existing_openings {Boolean}:
          Specifies whether existing opening features with afield value
          of Opening will be deleted before creating new opening features. If
          deleted, existing openings will be replaced with new openings if they
          are at the same location. USE_TYPEDELETE_EXISTING-Existing
          openings will be
          deleted.KEEP_EXISTING-Existing openings will not be deleted. This is
          the
          default.

        """