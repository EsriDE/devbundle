# Generated documentation for module arcpy.aviation


class FAA13(object):
    """
    Creates obstruction identification surfaces (OIS) based on the FAA Advisory Circular AC 150/5300-13B specification.
    """

    @property
    def description(self) -> str:
        return """

        FAA13_aviation(in_features, target_ois_features, high_runway_end_type, {low_runway_end_type}, {high_approach_offset_angle}, {low_approach_offset_angle}, {generate_departure_surfaces}, {generate_clearway_surfaces}, {in_threshold_point_features}, {custom_json_file})

        Creates obstruction identification surfaces (OIS) based on the FAA
        Advisory Circular AC 150/5300-13B specification.

     INPUTS:
      in_features (Feature Layer):
          The input runway dataset. The feature class must be z-enabled and
          contain polylines.
      target_ois_features (Feature Layer):
          The target feature class that will contain the generated OIS.
      high_runway_end_type (String):
          Specifies the classification that will be used for the high end of the
          runway.SMALL_AIRPLANE_APPROACH_SPEEDS_LT_50-This runway classification
          is
          designed for light aircraft with a maximum takeoff weight of less than
          254 pounds and approach speed less than 50 knots. This is a visual
          runway only that can be used during the day or
          night.SMALL_AIRPLANE_APPROACH_SPEEDS_GT_50-This runway classification
          is
          designed for light aircraft with a maximum takeoff weight of less than
          1,320 pounds and approach speed more than 50 knots. This is a visual
          runway only that can be used during the day or
          night.LARGE_AIRPLANE_VISUAL_RUNWAY_DAY_NIGHT-This runway
          classification is
          designed for aircraft with a maximum certified takeoff weight of more
          than 12,500 pounds. The approach end of the runway is expected to
          serve large airplanes as a visual runway available day or night or an
          instrument approach with a minimum greater than one statute mile (1.6
          kilometers) only during the
          day.INSTRUMENT_NP_GT_EQ_3/4_MILE_VISIBILITY-This runway classification
          is
          designed for a nonprecision approach when visibility is greater than
          3/4 of a mile and less than 1 mile. The approach end of the runway
          supports IFR (Instrument Flight Rules) circling procedures providing
          the following lateral guidance: Very High Frequency Omnidirectional
          Range (VOR), Non-Directional Beacon (NDB), Lateral Navigation (LNAV),
          Localizer Performance (LP), Tactical Air Navigation (TACAN), VHF
          Omnidirectional Range Collocated Tactical Air (VORTAC), Airport
          Surveillance Radar (ASR), and Localizer
          (LOC).INSTRUMENT_NP_LT_3/4_MILE_VISIBILITY-This runway
          classification's
          nonprecision approach guidance is provided when visibility is less
          than 3/4 of a mile. The approach end of the runway is expected to
          accommodate instrument approaches with a visibility minimum of less
          than 3/4 of a statue mile (1.2 kilometers) and includes the following
          guidance: Very High Frequency Omnidirectional Range (VOR), Non-
          Directional Beacon (NDB), Lateral Navigation (LNAV), Localizer
          Performance (LP), Tactical Air Navigation (TACAN), VHF Omnidirectional
          Range Collocated Tactical Air (VORTAC), Airport Surveillance Radar
          (ASR), and Localizer (LOC).INSTRUMENT_GT_EQ_3/4_MILE_VISIBILITY-This
          runway classification is
          designed for an instrument approach procedure when visibility is
          greater than 3/4 of a mile and less than 1 mile. The approach end of
          the runway is expected to accommodate instrument approaches with a
          visible minimum of more than 3/4 of a mile but less than 1 statute
          mile (1.2-1.6 kilometers) during the day or
          night.INSTRUMENT_LT_3/4_MILE_VISIBILITY-This runway classification's
          course
          and vertical path guidance are provided when visibility is less than
          3/4 of a mile. The approach end of the runway is expected to
          accommodate instrument approaches with a visibility minimum of less
          than 3/4 of a statute mile (1.2 kilometers) or precision approaches
          (Instrument landing System [ILS] or Global Navigation Satellite System
          [GNSS] Landing System [GLS]) day or night.VERTICAL_GUIDANCE_APPROACH-
          This runway classification uses precision
          guidance systems to support aircraft approach and landing. The
          approach of the runway is expected to accommodate approaches with
          vertical guidance such as a Glide Path Qualification Surface (GPQS).
      low_runway_end_type {String}:
          Specifies the classification that will be used for the low end of the
          runway.SAME_AS_HIGH_RUNWAY_END_CLASSIFICATION-Same as high runway end
          classificationSMALL_AIRPLANE_APPROACH_SPEEDS_LT_50-This runway
          classification is
          designed for light aircraft with a maximum takeoff weight of less than
          254 pounds and approach speed less than 50 knots. This is a visual
          runway only that can be used during the day or
          night.SMALL_AIRPLANE_APPROACH_SPEEDS_GT_50-This runway classification
          is
          designed for light aircraft with a maximum takeoff weight of less than
          1,320 pounds and approach speed more than 50 knots. This is a visual
          runway only that can be used during the day or
          night.LARGE_AIRPLANE_VISUAL_RUNWAY_DAY_NIGHT-This runway
          classification is
          designed for aircraft with a maximum certified takeoff weight of more
          than 12,500 pounds. The approach end of the runway is expected to
          serve large airplanes as a visual runway available day or night or an
          instrument approach with a minimum greater than 1 statute mile (1.6
          kilometers) only during the
          day.INSTRUMENT_NP_GT_EQ_3/4_MILE_VISIBILITY-This runway classification
          is
          designed for a nonprecision approach when visibility is greater than
          3/4 of a mile and less than 1 mile. The approach end of the runway
          supports IFR (Instrument Flight Rules) circling procedures providing
          the following lateral guidance: Very High Frequency Omnidirectional
          Range (VOR), Non-Directional Beacon (NDB), Lateral Navigation (LNAV),
          Localizer Performance (LP), Tactical Air Navigation (TACAN), VHF
          Omnidirectional Range Collocated Tactical Air (VORTAC), Airport
          Surveillance Radar (ASR), and Localizer
          (LOC).INSTRUMENT_NP_LT_3/4_MILE_VISIBILITY-This runway
          classification's
          nonprecision approach guidance is provided when visibility is less
          than 3/4 of a mile. The approach end of the runway is expected to
          accommodate instrument approaches with a visibility minimum of less
          than 3/4 of a statue mile (1.2 kilometers) and includes the following
          guidance: Very High Frequency Omnidirectional Range (VOR), Non-
          Directional Beacon (NDB), Lateral Navigation (LNAV), Localizer
          Performance (LP), Tactical Air Navigation (TACAN), VHF Omnidirectional
          Range Collocated Tactical Air (VORTAC), Airport Surveillance Radar
          (ASR), and Localizer (LOC).INSTRUMENT_GT_EQ_3/4_MILE_VISIBILITY-This
          runway classification is
          designed for an instrument approach procedure when visibility is
          greater than 3/4 of a mile and less than 1 mile. The approach end of
          the runway is expected to accommodate instrument approaches with a
          visibility minimum of more than 3/4 of a mile but less than 1 statute
          mile (1.2-1.6 kilometers) during the day or
          night.INSTRUMENT_LT_3/4_MILE_VISIBILITY-This runway classification's
          course
          and vertical path guidance are provided when visibility is less than
          3/4 of a mile. The approach end of the runway is expected to
          accommodate instrument approaches with a visibility minimum of less
          than 3/4 of a statute mile (1.2 kilometers) or precision approaches
          (Instrument landing System [ILS] or Global Navigation Satellite System
          [GNSS] Landing System [GLS]) day or night.VERTICAL_GUIDANCE_APPROACH-
          This runway classification uses precision
          guidance systems to support aircraft approach and landing. The
          approach of the runway is expected to accommodate approaches with
          vertical guidance such as a Glide Path Qualification Surface (GPQS).
      high_approach_offset_angle {Double}:
          The offset angle for the high-end approach. The angle value is in
          degrees and ranges from -60 to 60. This value will be honored for the
          instrument approach surfaces only.
      low_approach_offset_angle {Double}:
          The offset angle for the low-end approach. The angle value is in
          degrees and ranges from -60 to 60. This value will be honored for the
          instrument approach surfaces only.
      generate_departure_surfaces {String}:
          Specifies whether a departure surface will be generated for departure
          runways.GENERATE_DEPARTURE_SURFACE_AT_BOTH_ENDS-A departure surface
          will be
          generated at both ends of the runway. This is the
          default.GENERATE_DEPARTURE_SURFACE_AT_HIGH_END-A departure surface
          will be
          generated at the high end of the
          runway.GENERATE_DEPARTURE_SURFACE_AT_LOW_END-A departure surface will
          be
          generated at the low end of the
          runway.DO_NOT_GENERATE_DEPARTURE_SURFACE-A departure surface will not
          be
          generated.
      generate_clearway_surfaces {Boolean}:
          Specifies whether a clearway surface will be generated for departure
          runways. Clearway surfaces will only be generated if a value has been
          specified for the generate_departure_surfaces
          parameter.GENERATE_CLEARWAY_SURFACES-A clearway surface will be
          generated.NOT_GENERATE_CLEARWAY_SURFACES-A clearway surface will not
          be
          generated. This is the default.
      in_threshold_point_features {Feature Layer}:
          Provides x-, y-, and z-geometry for displaced threshold features. If
          displaced thresholds are included, surfaces will be constructed based
          on their x-, y-, and z-geometry instead of their corresponding runway
          feature endpoint.
      custom_json_file {File}:
          The import configuration, in JSON format, that will be used to create
          the custom OIS.

        """