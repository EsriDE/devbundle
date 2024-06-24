# Generated documentation for module arcpy.conversion


class KMLToLayer(object):
    """
    Converts a .kml or .kmz file into datasets in a geodatabase and a layer file. The layer file maintains the symbology of the input .kml or .kmz file.
    """

    @property
    def description(self) -> str:
        return """

        KMLToLayer_conversion(in_kml_file, output_folder, {output_data}, {include_groundoverlay}, {out_suffix})

        Converts a .kml or .kmz file into datasets in a geodatabase and a
        layer file. The layer file maintains the symbology of the input .kml
        or .kmz file.

     INPUTS:
      in_kml_file (File / KML Layer):
          The .kml or .kmz file that will be converted to geodatabase datasets.
      output_folder (Folder):
          The destination folder where the output geodatabase and layer file
          (.lyrx) will be created.
      output_data {String}:
          A name that will be used for both the output geodatabase and layer
          file (.lyrx). The default is the name of the input file.You can
          specify the name of an existing geodatabase in the target
          folder, and the conversion will write new datasets into the existing
          geodatabase. If the geodatabase with the specified name does not
          exist, it will be created in the target folder.
      include_groundoverlay {Boolean}:
          Specifies whether ground overlays from the KML will be included in the
          output.Use caution if the KMZ points to a service that serves imagery.
          The
          tool will attempt to convert the raster imagery at all available
          scales. This process may be lengthy and possibly overwhelm the server
          or time out.GROUNDOVERLAY-Ground overlays will be included in the
          output.NO_GROUNDOVERLAY-Ground overlays will not be included in the
          output.
          This is the default.
      out_suffix {String}:
          A suffix that will be added to the names of all output feature
          datasets, feature classes, mosaic datasets, and layer files. If no
          suffix is specified, the name of the feature dataset in the output
          geodatabase will be Placemarks.

        """