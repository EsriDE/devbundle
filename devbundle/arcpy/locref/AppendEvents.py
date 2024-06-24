# Generated documentation for module arcpy.locref


class AppendEvents(object):
    """
    Appends event records from a table, layer, or feature class to an existing ArcGIS Location Referencing event feature class.
    """

    @property
    def description(self) -> str:
        return """

        AppendEvents_locref(in_dataset, in_target_event, field_mapping, {load_type}, {generate_event_ids}, {generate_shapes})

        Appends event records from a table, layer, or feature class to an
        existing ArcGIS Location Referencing event feature class.

     INPUTS:
      in_dataset (Table View):
          The source event records to append.
      in_target_event (Feature Layer):
          The Location Referencing event layer or feature class to which the
          source event records will be appended.
      field_mapping (Field Mappings):
          Controls how the attribute information in fields of the in_dataset
          parameter value is transferred to the in_target_event parameter
          value.Because the in_dataset parameter value is appended to an
          existing
          event that has a predefined schema (field definitions), fields cannot
          be added or removed from the target dataset. While you can set merge
          rules for each output field, the tool ignores those rules.The
          FieldMappings class can be used to define this parameter.
      load_type {String}:
          Specifies how appended events with measure or temporality overlaps
          with identical event IDs as the in_target_event records will be loaded
          into the event feature class.ADD-The in_dataset records will be
          appended to the specified target
          event feature class. No changes are made to the target event
          records.RETIRE_OVERLAPS-The in_dataset records will be appended to the
          specified target event feature class and any records that have the
          same measure or temporality overlaps as the appended events will be
          retired. If the appended event eclipses the specified target event
          feature, the target event record will be deleted. Use this option for
          linear events only.RETIRE_BY_EVENT_ID-The in_dataset records will be
          appended to the
          specified target event feature class and any records that have the
          same event ID and temporality overlaps as the appended events will be
          retired. If the appended event eclipses a target event record that has
          the same event ID, the target event record will be
          deleted.REPLACE_BY_EVENT_ID-The in_dataset records will be appended to
          the
          specified target event feature class, and any records that have the
          same event ID as the appended events will be replaced.
      generate_event_ids {Boolean}:
          Specifies whether event IDs will be generated for in_dataset
          records being appended. Generation of event IDs will only be applied
          to in_dataset records with a Null value for thefield. Event
          IDGENERATE_EVENT_IDS-Event IDs for the in_dataset records being
          appended
          will be generated.NO_GENERATE_EVENT_IDS-Event IDs for the in_dataset
          records being
          appended will not be generated. This is the default.
      generate_shapes {Boolean}:
          Specifies whether the shapes of the records being appended will be
          regenerated. This parameter is only enabled when the in_dataset value
          is a feature layer or feature class.GENERATE_SHAPES-The shapes of the
          input event features will be
          regenerated. This is the default.NO_SHAPES-The shapes of the input
          event features will not be
          regenerated.

        """