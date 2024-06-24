# Generated documentation for module arcpy.ia.Functions


class VideoMetadataToFeatureClass(object):
    """
    Extracts the platform, frame center, frame outline, and attributes metadata from an FMV-compliant video. The output geometry and attributes are saved as feature classes.
    """

    @property
    def description(self) -> str:
        return """

        VideoMetadataToFeatureClass_ia(in_video, {csv_file}, {flightpath}, {flightpath_type}, {imagepath}, {imagepath_type}, {footprint}, {start_time}, {stop_time}, {min_distance}, {min_time}, {vmti})

        Extracts the platform, frame center, frame outline, and attributes
        metadata from an FMV-compliant video. The output geometry and
        attributes are saved as feature classes.

     INPUTS:
      in_video (File):
          The FMV-compliant input video file containing essential metadata for
          each frame of the video data. The supported video file types are PS,
          TS, MPG, MPEG, MP2, MPG2, MPEG2, MP4, MPG4, MPEG4, H264, H265, VOB,
          and M2TS.
      flightpath_type {String}:
          Specifies the feature class type that will be used for the flight
          path.POINT-A point feature class will be used.POLYLINE-A polyline
          feature
          class will be used. This is the default.
      imagepath_type {String}:
          Specifies the feature class type that will be used for the image path.
          If you're using a point output, the center of each video frame image
          will appear on the map.POINT-A point feature class will be
          used.POLYLINE-A polyline feature
          class will be used. This is the default.
      start_time {Time Unit / Date}:
          The metadata recording start time from the beginning of the video. The
          input format is d.hh:mm:ss, and the default start time is 0.00:00:00.
          Metadata time stamps are not used in this field; the time of the video
          file is used.
      stop_time {Time Unit / Date}:
          The metadata recording end time. The input format is d.hh:mm:ss. If
          not set, the value will default to the end of the video. Metadata time
          stamps are not used in this field.
      min_distance {Linear Unit}:
          The distance between the features in sequential video frames. If left
          blank, every metadata feature will be extracted and added to the
          feature class.
      min_time {Time Unit}:
          The time interval between the features in sequential video frames. If
          left blank, every metadata feature will be extracted and added to the
          feature class.

     OUTPUTS:
      csv_file {File}:
          A comma-separated values (CSV) file containing metadata about the
          video frames for specific times.This metadata file is in the same
          format used by the Video Multiplexer
          tool.
      flightpath {Feature Class}:
          The feature class containing the sensor's flight path information.
      imagepath {Feature Class}:
          The output feature class containing the image path information.
      footprint {Feature Class}:
          The output feature class containing the video image footprint
          information.
      vmti {Feature Dataset}:
          The output feature class containing the video VMTI information.

        """