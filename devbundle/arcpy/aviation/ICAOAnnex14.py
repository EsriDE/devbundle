# Generated documentation for module arcpy.aviation


class ICAOAnnex14(object):
    """
    Creates obstruction identification surfaces (OIS) based on ICAO Annex 14 specifications. These surfaces define the airspace around aerodromes to be free of obstacles so flight operations can be performed safely. This tool creates surfaces as a polygon or multipatch features.
    """

    @property
    def description(self) -> str:
        return """

        ICAOAnnex14_aviation(in_features, target, runway_type, {highend_clear_way_length}, {lowend_clear_way_length}, {airport_elevation}, {runway_direction}, {include_merged_surface}, {custom_json_file}, {airport_control_point_feature_class})

        Creates obstruction identification surfaces (OIS) based on ICAO Annex
        14 specifications. These surfaces define the airspace around
        aerodromes to be free of obstacles so flight operations can be
        performed safely. This tool creates surfaces as a polygon or
        multipatch features.

     INPUTS:
      in_features (Feature Layer):
          The input runway dataset. The feature class must be z-enabled and
          contain polylines.
      target (Feature Layer):
          The output feature class that will contain the generated OIS.
      runway_type (String):
          Specifies the runway classification for the in_features parameter
          value.NON_INSTRUMENT_CODE_NUMBER_1-A runway intended for the operation
          of
          aircraft using visual approach procedures. Runway strip length is 30
          meters.NON_INSTRUMENT_CODE_NUMBER_2-A runway with a 60-meter strip
          length and
          40-meter strip width that is intended for the operation of aircraft
          using visual approach procedures.NON_INSTRUMENT_CODE_NUMBER_3-A runway
          with a 60-meter strip length and
          75-meter strip width that is intended for the operation of aircraft
          using visual approach procedures.NON_INSTRUMENT_CODE_NUMBER_4-A runway
          with a 60-meter strip length and
          75-meter strip width that is intended for the operation of aircraft
          using visual approach
          procedures.NON_PRECISION_APPROACH_CODE_NUMBER_1-An instrument runway
          served by
          visual aids and a nonvisual aid providing at least directional
          guidance adequate for a straight-in approach. This runway type has a
          60-meter strip length and a 75-meter strip width on either side of the
          runway centerline.NON_PRECISION_APPROACH_CODE_NUMBER_2-An instrument
          runway served by
          visual aids and a nonvisual aid providing at least directional
          guidance adequate for a straight-in approach. This runway type has a
          60-meter strip length and a 75-meter strip width on either side of the
          runway centerline.NON_PRECISION_APPROACH_CODE_NUMBER_3-An instrument
          runway served by
          visual aids and a nonvisual aid providing at least directional
          guidance adequate for a straight-in approach. This runway type has a
          60-meter strip length and a 150-meter strip width on either side of
          the runway centerline.NON_PRECISION_APPROACH_CODE_NUMBER_4-An
          instrument runway served by
          visual aids and a nonvisual aid providing at least directional
          guidance adequate for a straight-in approach. This runway type has a
          60-meter strip length and a 150-meter strip width on either side of
          the runway centerline.PRECISION_APPROACH_CATEGORY_I_CODE_NUMBER_1-An
          instrument runway
          served by an Instrument Landing System (ILS) or a Microwave Landing
          System (MLS) and visual aids intended for operations with a decision
          height not lower than 60 meters (200 feet) and either a visibility not
          less than 800 meters or a runway visual range not less than 550
          meters. This runway type has a 60-meter strip length and a 75-meter
          strip width on either side of the runway
          centerline.PRECISION_APPROACH_CATEGORY_I_CODE_NUMBER_2-An instrument
          runway
          served by ILS and MLS and visual aids intended for operations with a
          decision height not lower than 60 meters (200 feet) and either a
          visibility not less than 800 meters or a runway visual range not less
          than 550 meters. This runway type has a 60-meter strip length and a
          75-meter strip width on either side of the runway
          centerline.PRECISION_APPROACH_CATEGORY_I_CODE_NUMBER_3_4-An instrument
          runway
          served by ILS and MLS and visual aids intended for operations with a
          decision height not lower than 60 meters (200 feet) and either a
          visibility not less than 800 meters or a runway visual range not less
          than 550 meters. This runway type has a 60-meter strip length and a
          150-meter strip width on either side of the runway
          centerline.PRECISION_APPROACH_CATEGORY_II_III_CODE_NUMBER_3_4-An
          instrument
          runway served by ILS and MLS and visual aids intended for operations
          with a decision height lower than 60 meters (200 feet) but not lower
          than 30 meters (100 feet) and a runway visual range not less than 350
          meters. This runway type has a 60-meter strip length and a 150-meter
          strip width on either side of the runway centerline.
      highend_clear_way_length {Double}:
          The length of the area at the high end of the runway. The unit of
          measurement is based on the input runway features.
      lowend_clear_way_length {Double}:
          The length of the area at the low end of the runway. The unit of
          measurement is based on the input runway features.
      airport_elevation {Double}:
          The highest elevation on any of the runways of the airport. The value
          must be in the vertical coordinate system linear units of the target
          feature class. If no value is provided, the highest point from the
          in_features dataset will be used.
      runway_direction {String}:
          Specifies at which end of the runway the approach surface will be
          created.HIGH_END_TO_LOW_END-The approach surface will be created at
          the high
          end of the runway to the low end. If a displaced threshold point
          exists at the high end of the runway, that point will be honored when
          creating the OIS.LOW_END_TO_HIGH_END-The approach surface will be
          created at the low
          end of the runway to the high end. If a displaced threshold point
          exists at the low end of the runway, that point will be honored when
          creating the OIS.BOTH_END-The approach surface will be created at both
          the low end and
          high end of the runway.
      include_merged_surface {Boolean}:
          Specifies whether merged surfaces will be
          generated.INCLUDE_MERGED_SURFACE-All the surfaces will be generated
          for the
          merged surfaces, as well as merged conical and horizontal surfaces.
          This is the default.NOT_INCLUDE_MERGED_SURFACE-Surfaces will not be
          generated for the
          merged surfaces.
      custom_json_file {File}:
          The import configuration, in JSON format, that will be used to create
          the custom OIS.
      airport_control_point_feature_class {Feature Layer}:
          The point features containing anfeature, displaced threshold
          features, or both. Values provided for theparameter will take
          precedence over these point features. Airport ElevationAirport
          Elevation

        """