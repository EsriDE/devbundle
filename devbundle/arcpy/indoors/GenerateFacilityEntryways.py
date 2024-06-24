# Generated documentation for module arcpy.indoors


class GenerateFacilityEntryways(object):
    """
    Creates or updates points representing a facility's entry or exit locations.
    """

    @property
    def description(self) -> str:
        return """

        GenerateFacilityEntryways_indoors(in_level_features, in_unit_features, in_door_features, target_entryways, {buffer_size}, {entryway_use_type}, {exterior_unit_exp}, {delete_existing_entryways}, {level_id_field}, {use_type_field})

        Creates or updates points representing a facility's entry or exit
        locations.

     INPUTS:
      in_level_features (Feature Layer):
          The input polygon features representing a level or levels in one or
          more facilities. In the Indoors model, this is the Levels layer. Only
          the levels represented by these features will be processed.
      in_unit_features (Feature Layer):
          The input polygon features representing building spaces. In the
          Indoors model, this is the Units layer. The tool will use these
          features when identifying exterior edges of a facility.
      in_door_features (Feature Layer):
          The input polyline features representing doors. In the Indoors
          model, this is a subset of features from the Details layer. The tool
          will use these features when identifying entryways along the exterior
          of a facility. The layer must have one or more door features
          selected for the tool to
          run. Use the Select Layer By Attribute tool to make a selection.
      target_entryways (Feature Layer):
          The feature class or feature layer to which generated entryway points
          will be written.
      buffer_size {Double}:
          The distance, in meters, the tool will search inward and outward from
          a facility's exterior edge to identify potential entryways. The value
          must be greater than 0 and less than 10. The default value is 0.5.
      entryway_use_type {String}:
          The value that will be used to calculate thefield for new
          entryway points. The default value is Entry. USE_TYPE
      exterior_unit_exp {SQL Expression}:
          An SQL expression used to define whichvalues represent a
          facility's exterior spaces, such as patios or fire escapes. Spaces
          matching this expression will be treated as exterior features during
          entryway generation. Input Unit Features
      delete_existing_entryways {Boolean}:
          Specifies whether existing entryway features with afield value
          matching the entryway_use_type parameter value will be deleted before
          creating new entryway points. When deleting existing entryways, the
          tool only identifies entryways on levels included in the
          in_level_features parameter. USE_TYPEDELETE_FEATURES-Existing
          features will be
          deleted.NO_DELETE_FEATURES-Existing features will not be deleted. This
          is the
          default.
      level_id_field {Field}:
          The field that will be updated with the associated level ID
          for the new entryway features. If the in_level_features parameter
          value is a floor-aware layer, this parameter will default to the
          layer's configuredvalue. Otherwise, the parameter will default to
          thefield. If the defined field does not exist in the target_entryways
          feature layer, a field with the supplied name will be created and
          populated with the level ID field values. Floor FieldLEVEL_ID
      use_type_field {Field}:
          The field that will be updated with the entryway_use_type
          value for the new entryway features. The default is thefield. If the
          defined field does not exist in the target_entryways feature layer, a
          field with the supplied name will be created and populated with the
          entryway_use_type value. USE_TYPE

        """