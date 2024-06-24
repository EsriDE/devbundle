# Generated documentation for module arcpy.topographic


class CalculateMetrics(object):
    """
    Populates metrics for features in a geodatabase. Metrics include length, width, area, and elevation attributes.
    """

    @property
    def description(self) -> str:
        return """

        CalculateMetrics_topographic(in_features;in_features..., in_metric_types;in_metric_types..., {in_length_attributes}, {in_width_attributes}, {in_area_attributes}, {in_angle_attributes}, {in_elevation_attributes}, {in_precision}, {mgrs_attributes}, {mgrs_precision}, {elevation_raster})

        Populates metrics for features in a geodatabase. Metrics include
        length, width, area, and elevation attributes.

     INPUTS:
      in_features (Feature Layer):
          The features for which metrics will be calculated.
      in_metric_types (String):
          Specifies the types of metrics that will be calculated.The Spatial
          Analyst extension is required when using an elevation
          raster and the ANGLE_OF_ORIENTATION option to rotate point features so
          that they face downhill.ANGLE_OF_ORIENTATION-Angle of orientation
          metrics will be
          calculatedAREA-Area metrics will be calculated.ELEVATION-Elevation
          metrics will be calculated.LENGTH-Length metrics will be
          calculated.MGRS-Military Grid Reference System coordinates will be
          calculated.WIDTH-Width metrics will be calculated.
      in_length_attributes {String}:
          A comma-delimited string of field names from which the length metrics
          will be calculated. The default is LEG,LEN,LEN_,LGN,LZN. You can add
          the names of other length metric fields; if the fields exist in the
          in_features value, they will be computed.
      in_width_attributes {String}:
          A comma-delimited string of field names from which the width metrics
          will be calculated. The default is WID,WID_,WGP. You can add the names
          of other width metric fields; if the fields exist in the in_features
          value, they will be computed.
      in_area_attributes {String}:
          A comma-delimited string of field names from which the area metrics
          will be calculated. The default is ARA,ARE,ARE_. You can add the names
          of other area metric fields; if the fields exist in the in_features
          value, they will be computed.
      in_angle_attributes {String}:
          A comma-delimited string of field names from which the angle of
          orientation metrics will be calculated. The default is AOO,DOF,FEO.
          You can add the names of other angle of orientation metric fields; if
          the fields exist in the in_features value, they will be computed.
      in_elevation_attributes {String}:
          A comma-delimited string of field names from which the elevation
          metrics will be calculated. The default is ZV2,ZVH. You can add the
          names of other elevation metric fields; if the fields exist in the
          in_features value, they will be computed.
      in_precision {Long}:
          The precision of the metrics written to the target attributes.
      mgrs_attributes {String}:
          A comma-delimited string of field names from which the MGRS
          coordinates will be calculated. The default is MGRSValue,MGRS. You can
          add the names of other MGRS fields; if the fields exist in the
          in_features value, they will be computed. The fields must have a
          String field type and a field length greater than the largest possible
          MGRS coordinate value.
      mgrs_precision {String}:
          Specifies the precision of the coordinates that will be calculated for
          the target attributes.6x8 (4Q)-The precision will be calculated at
          grid-level precision,
          typically the polygon formed by a 6-degree wide UTM zone and 8-degree
          high latitude bands.100km (4QFJ)-The precision will be calculated at
          100,000 meters
          squared.10km (4QFJ16)-The precision will be calculated at 10,000
          meters
          squared.1km (4QFJ1267)-The precision will be calculated at 1,000
          meters
          squared.100m (4QFJ123678)-The precision will be calculated at 100
          meters
          squared.10m (4QFJ12346789)-The precision will be calculated at 10
          meters
          squared.1m (4QFJ1234567890)-The precision will be calculated at 1
          meter
          squared.Image City Map (1234)-The precision will be calculated at the
          level of
          an Image City Map (ICM). This is the default.
      elevation_raster {Raster Layer / Mosaic Layer}:
          The raster file from which the elevation metrics will be derived.
          Elevation metrics derived from a raster file specified here will
          overwrite existing elevation data.The Spatial Analyst extension is
          required when using an elevation
          raster and the angle of orientation to rotate point features so that
          they face downhill.

        """