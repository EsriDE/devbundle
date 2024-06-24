# Generated documentation for module arcpy.ia.Functions


class ExtractVideoFramesToImages(object):
    """
    Extracts video frame images and associated metadata from an FMV- compliant video stream. The extracted images can be added to a mosaic dataset or other tools and functions for further analysis.
    """

    @property
    def description(self) -> str:
        return """

        ExtractVideoFramesToImages_ia(in_video, out_folder, {image_type}, {image_overlap}, {require_fresh_metadata}, {min_time})

        Extracts video frame images and associated metadata from an FMV-
        compliant video stream. The extracted images can be added to a mosaic
        dataset or other tools and functions for further analysis.

     INPUTS:
      in_video (File):
          The input video file in any of the supported video file formats,
          including PS, TS, MPG, MPEG, MP2, MPG2, MPEG2, MP4, MPG4, MPEG4, H264,
          H265, VOB, and M2TS.
      image_type {String}:
          Specifies the output image format.JPEG-The output will be in JPEG
          image format.TIFF-The output will be
          in TIFF image format. This is the default.NITF-The output will be in
          NITF image format.PNG-The output will be in PNG image format.
      image_overlap {Double}:
          The maximum overlap percentage between two images. If the overlap
          between a candidate image and the last image written to disk is
          greater than this value, the candidate image will be ignored. The
          default percentage is 100 percent, which writes all images to disk.
      require_fresh_metadata {Boolean}:
          Specifies whether video frames with associated metadata will be
          extracted and saved.REQUIRE_FRESH_METADATA-Only video frames with
          associated metadata will
          be saved.NO_REQUIRE_FRESH_METADATA-All video frames will be saved.
          This is the
          default.
      min_time {Time Unit}:
          The minimum time interval between video frames to be saved. If no
          value is specified, all video frames will be saved as images.

     OUTPUTS:
      out_folder (Folder):
          The file directory where the output images and metadata will be saved.

        """