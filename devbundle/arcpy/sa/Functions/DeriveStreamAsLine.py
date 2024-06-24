# Generated documentation for module arcpy.sa.Functions


class DeriveStreamAsLine(object):
    """
    Generates stream line features from an input surface raster with no prior sink or depression filling required.
    """

    @property
    def description(self) -> str:
        return """

        DeriveStreamAsLine_sa(in_surface_raster, out_stream_features, {in_depressions_data}, {in_weight_raster}, {accumulation_threshold}, {stream_designation_method}, {simplify})

        Generates stream line features from an input surface raster with no
        prior sink or depression filling required.

     INPUTS:
      in_surface_raster (Composite Geodataset):
          The input surface raster.
      in_depressions_data {Composite Geodataset}:
          An optional dataset that defines real depressions.The depressions can
          be defined either through a raster or a feature
          layer.If input is a raster, the depression cells must take a valid
          value,
          including zero, and the areas that are not depressions must be NoData.
      in_weight_raster {Composite Geodataset}:
          An optional input raster dataset that defines the fraction of flow
          that contributes to flow accumulation at each cell.The weight is only
          applied to the accumulation of flow.If no accumulation weight raster
          is specified, a default weight of 1
          will be applied to each cell.
      accumulation_threshold {Areal Unit}:
          The threshold for determining whether a given cell is part of a stream
          in terms of the total area that flows into such cell.
      stream_designation_method {String}:
          Specifies the unique value or order of the streams in the output
          attribute table.CONSTANT-The output stream segments will all equal 1.
          This is the
          default.UNIQUE-Each stream will have a unique ID between intersections
          in the
          output.STRAHLER-The Strahler method, in which stream order only
          increases
          when streams of the same order intersect, will be used. The
          intersection of a first-order and second-order link will remain a
          second-order link, rather than creating a third-order link.SHREVE-The
          Shreve method, in which stream order is assigned by
          magnitude, will be used. All links with no tributaries are assigned a
          magnitude (order) of one. Magnitudes are additive downslope. When two
          links intersect, their magnitudes are added and assigned to the
          downslope link.HACK-The Hack method, in which each stream segment is
          assigned an
          order greater than the stream or river to which it discharges, will be
          used. For example, the main river channel is assigned an order of 1,
          all stream segments discharging to it are assigned an order of 2, any
          stream discharging to an order 2 stream is assigned an order of 3, and
          so on.ALL-The output attribute table will show each stream segment
          designation based on all methods.
      simplify {Boolean}:
          Specifies whether the output stream lines will be smoothed into
          simpler shapes.NO_SIMPLIFY-The stream feature lines will not be
          smoothed.SIMPLIFY-The
          stream feature lines will be simplified using the
          Douglas-Peucker algorithm with a tolerance of sqrt(0.5) * cell size.
          This is the default.

     OUTPUTS:
      out_stream_features (Feature Class):
          The output feature class that will contain the identified streams.

        """