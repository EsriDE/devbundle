# Generated documentation for module arcpy.management


class ExtractSubDataset(object):
    """
    Creates a new raster dataset from a selection of an HDF or NITF dataset.
    """

    @property
    def description(self) -> str:
        return """

        ExtractSubDataset_management(in_raster, out_raster, {subdataset_index;subdataset_index...})

        Creates a new raster dataset from a selection of an HDF or NITF
        dataset.

     INPUTS:
      in_raster (Raster Layer):
          The HDF or NITF dataset that has the layers you want to extract.
      subdataset_index {Value Table}:
          The subdatasets that you want to extract.

     OUTPUTS:
      out_raster (Raster Dataset):
          The name, location, and format for the dataset you are creating.When
          storing the raster dataset in a file format, you need to specify
          the file extension:.bil-Esri BIL.bip-Esri BIP.bmp-BMP.bsq-Esri
          BSQ.dat-ENVI
          DAT.gif-GIF.img-ERDAS IMAGINE file.jpg-JPEG.jp2-JPEG
          2000.png-PNG.tif-TIFFno extension-Esri GRIDWhen storing a raster
          dataset in a geodatabase, do not add a file
          extension to the name of the raster dataset. When storing your
          raster dataset to a JPEG file, a JPEG 2000
          file, or a geodatabase, you can specify atype andwithin the
          Environment Settings. CompressionCompression Quality

        """