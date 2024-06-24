# Generated documentation for module arcpy.ia.Functions


class VideoMultiplexer(object):
    """
    Creates a video file that combines an archived video stream file and an associated metadata file synchronized by a time stamp.
    """

    @property
    def description(self) -> str:
        return """

        VideoMultiplexer_ia(in_video_file, metadata_file, out_video_file, {metadata_mapping_file}, {timeshift_file}, {elevation_layer})

        Creates a video file that combines an archived video stream file and
        an associated metadata file synchronized by a time stamp.

     INPUTS:
      in_video_file (File):
          The input video file that will be converted to a FMV-compliant video
          file.The following video file types are supported: .avi, .h264, .h265,
          .mp2, .mp4, .m2ts, .mpeg, .mpeg2, .mpeg4, .mpg, .mpg2, .mpg4, .ps,
          .ts, and vob.
      metadata_file (File):
          A comma-separated values (CSV) file containing metadata about the
          video frames for specific times.Each column represents one metadata
          field, and one of the columns must
          be a time reference. The time reference is Unix Time Stamp (seconds
          past 1970) multiplied by one million, which is stored as an integer.
          The time is stored as such so that any instant in time (down to one
          millionth of a second) can be referenced with an integer.
          Consequently, a time difference between two entries of 500,000
          represents one half of a second in elapsed time.The first row contains
          the field names for the metadata columns. These
          field names can be matched to their corresponding field names using
          the FMV_Multiplexer_Field_Mapping_Template.csv file if needed. Each
          subsequent row contains the metadata values for the time indicated in
          the time field. The FMV_Multiplexer_Field_Mapping_Template.csv
          template is in C:\Program Files\ArcGIS\Pro\Resources\FullMotionVideo.
      metadata_mapping_file {File}:
          A CSV file that contains 5 columns and 87 rows and is based on the
          FMV_Multiplexer_Field_Mapping_Template.csv template file obtained from
          C:\Program Files\ArcGIS\Pro\Resources\FullMotionVideo.Each row
          represents one of the standard MISB metadata tags, such as
          sensor latitude. The first two columns contain the MISB index and MISB
          tag name. The third column contains the field name as it appears in
          the in_metadata_file parameter if present. When the third column is
          populated, the tool can match the metadata field names to the proper
          FMV metadata tags. The fourth and fifth columns represent the units
          and notes associated with the tag, respectively.
      timeshift_file {File}:
          A file containing defined time shift intervals.Ideally, the video
          images and the metadata are synchronized in time.
          In this case, the image footprint in full motion video surrounds
          features that can be seen in the video image. Sometimes there is a
          mismatch between the timing of the video and the timing in the
          metadata. This leads to an apparent time delay between when a ground
          feature is surrounded by the image footprint and when that ground
          feature is visible in the video image. If this time shift is
          observable and consistent, the multiplexer can adjust the timing of
          the metadata to match the video. If there is a mismatch between
          the timing of the video and
          metadata, specify the time shift in the
          FMV_Multiplexer_TimeShift_Template.csv template in C:\Program
          Files\ArcGIS\Pro\Resources\FullMotionVideo. The time shift
          observations file is a CSV file containing two columns (and) and one
          or more data rows. A row for column names is optional. elapsed
          timetime shiftFor example, if the video image has a 5-second lag for
          the entire
          time, the time shift observation file will have one line: 0:00, -5.
          The entire video is shifted 5 seconds.If there is a 5-second lag at
          the 0:18 mark of the video, and a
          9-second lag at the 2:21 mark of the video, the time shift observation
          file will have the following two lines:0:18, -5 2:21, -9In this case,
          the video is shifted differently at the beginning of the
          video and at the end of the video.You can define any number of time
          shift intervals in the time shift
          observation file.
      elevation_layer {Raster Layer / Image Service / Linear Unit}:
          The source of the elevation needed for calculating the video frame
          corner coordinates. The source can be a layer, image service, or an
          average ground elevation or ocean depth. The average elevation value
          must include the units of measurement such as meters or feet or other
          measure of length.The accuracy of the video footprint and frame center
          depend on the
          accuracy of the DEM data source provided. It is recommended that you
          provide a DEM layer or image service. If you do not have access to DEM
          data, you can enter an average elevation and unit relative to sea
          level, such as 15 feet or 10 meters. In the case of a submersible, you
          can enter -15 feet or -10 meters. Using an average elevation or ocean
          depth is not as accurate as providing a DEM or bathymetric data.
          To calculate frame corner coordinates, the average elevation
          value must always be less than the sensor's altitude or depth as
          recorded in the metadata. For example, if the video was filmed at a
          sensor altitude of 10 meters and higher, a valid average elevation
          could be 9 meters or less. If a video was filmed underwater at a depth
          of -10 meters and deeper, the valid average elevation (relative to sea
          level) could be -11 or deeper. If thevalue is less than the average
          elevation value, the four corner coordinates will not be calculated
          for that record. If you do not know the average elevation of the
          project area, use a DEM. Sensor Altitude

     OUTPUTS:
      out_video_file (File):
          The name of the output video file, including the file extension.The
          supported output video file is .ts only.

        """