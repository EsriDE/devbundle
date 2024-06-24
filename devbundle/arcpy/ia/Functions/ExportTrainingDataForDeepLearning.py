# Generated documentation for module arcpy.ia.Functions


class ExportTrainingDataForDeepLearning(object):
    """
    Converts labeled vector or raster data into deep learning training datasets using a remote sensing image. The output will be a folder of image chips and a folder of metadata files in the specified format.
    """

    @property
    def description(self) -> str:
        return """

        ExportTrainingDataForDeepLearning_ia(in_raster, out_folder, {in_class_data}, {image_chip_format}, {tile_size_x}, {tile_size_y}, {stride_x}, {stride_y}, {output_nofeature_tiles}, {metadata_format}, {start_index}, {class_value_field}, {buffer_radius}, {in_mask_polygons}, {rotation_angle}, {reference_system}, {processing_mode}, {blacken_around_feature}, {crop_mode}, {in_raster2}, {in_instance_data}, {instance_class_value_field}, {min_polygon_overlap_ratio})

        Converts labeled vector or raster data into deep learning training
        datasets using a remote sensing image. The output will be a folder of
        image chips and a folder of metadata files in the specified format.

     INPUTS:
      in_raster (Raster Dataset / Raster Layer / Mosaic Layer / Image Service / Map Server / Map Server Layer / Internet Tiled Layer / Folder):
          The input source imagery, typically multispectral imagery.Examples of
          the types of input source imagery include multispectral
          satellite, drone, aerial, and National Agriculture Imagery Program
          (NAIP). The input can be a folder of images.
      in_class_data {Feature Class / Feature Layer / Raster Dataset / Raster Layer / Mosaic Layer / Image Service / Table / Folder}:
          The training sample data in either vector or raster form.
          Vector inputs should follow the training sample format generated using
          thepane. Raster inputs should follow a classified raster format
          generated by the Classify Raster tool. Training Samples Manager
          The raster input can also be from a folder of classified
          rasters. Classified raster inputs require a corresponding raster
          attribute table. Input tables should follow a training sample format
          generated by thebutton in thepane. Following the proper training
          sample format will produce optimal results with the statistical
          information; however, the input can also be a point feature class
          without a class value field or an integer raster without class
          information. Label Objects for Deep LearningTraining Samples
          Manager
      image_chip_format {String}:
          Specifies the raster format that will be used for the image chip
          outputs.The PNG and JPEG formats support up to three bands.TIFF-TIFF
          format will be used.PNG-PNG format will be used.JPEG-JPEG
          format will be used.MRF-Meta Raster Format (MRF) will be used.
      tile_size_x {Long}:
          The size of the image chips for the x dimension.
      tile_size_y {Long}:
          The size of the image chips for the y dimension.
      stride_x {Long}:
          The distance to move in the x direction when creating the next image
          chips.When stride is equal to tile size, there will be no overlap.
          When
          stride is equal to half the tile size, there will be 50 percent
          overlap.
      stride_y {Long}:
          The distance to move in the y direction when creating the next image
          chips.When stride is equal to tile size, there will be no overlap.
          When
          stride is equal to half the tile size, there will be 50 percent
          overlap.
      output_nofeature_tiles {Boolean}:
          Specifies whether image chips that do not capture training samples
          will be exported.ALL_TILES-All image chips, including those that do
          not capture
          training samples, will be exported.ONLY_TILES_WITH_FEATURES-Only image
          chips that capture training
          samples will be exported. This is the default.
      metadata_format {String}:
          Specifies the format that will be used for the output metadata labels.
          If the input training sample data is a feature class layer,
          such as a building layer or a standard classification training sample
          file, use theoroption (KITTI_rectangles or PASCAL_VOC_rectangles in
          Python). The output metadata is a .txt file or an .xml file containing
          the training sample data contained in the minimum bounding rectangle.
          The name of the metadata file matches the input source image name. If
          the input training sample data is a class map, use theoption
          (Classified_Tiles in Python) as the output metadata format.
          KITTI LabelsPASCAL Visual Object ClassesClassified Tiles
          KITTI_rectangles-The metadata will follow the same format as
          the Karlsruhe Institute of Technology and Toyota Technological
          Institute (KITTI) Object Detection Evaluation dataset. The KITTI
          dataset is a vision benchmark suite. The label files are plain text
          files. All values, both numerical and strings, are separated by
          spaces, and each row corresponds to one object. This format is
          used for object detection. PASCAL_VOC_rectangles-The metadata
          will follow the same
          format as the Pattern Analysis, Statistical Modeling and Computational
          Learning, Visual Object Classes (PASCAL_VOC) dataset. The PASCAL VOC
          dataset is a standardized image dataset for object class recognition.
          The label files are in XML format and contain information about image
          name, class value, and bounding boxes. This format is used for
          object detection. This is the default. Classified_Tiles-The
          output will be one classified image chip
          per input image chip. No other metadata for each image chip is used.
          Only the statistics output has more information about the classes,
          such as class names, class values, and output statistics. This
          format is primarily used for pixel classification. This format is
          also used for change detection when the output is one classified image
          chip from two image chips. RCNN_Masks-The output will be image
          chips that have a mask on
          the areas where the sample exists. The model generates bounding boxes
          and segmentation masks for each instance of an object in the image.
          This format is based on Feature Pyramid Network (FPN) and a ResNet101
          backbone in the deep learning framework model. This format is
          used for object detection; however, it can also be used
          for object tracking when the Siam Mask model type is used during
          training, as well as time series pixel classification when the PSETAE
          architecture is used. Labeled_Tiles-Each output tile will be
          labeled with a
          specific class. This format is used for object classification.
          MultiLabeled_Tiles-Each output tile will be labeled with one
          or more classes. For example, a tile may be labeled agriculture and
          also cloudy. This format is used for object classification.
          Export_Tiles-The output will be image chips with no label.
          This format is used for image translation techniques, such as Pix2Pix
          and Super Resolution. CycleGAN-The output will be image chips
          with no label.
          This format is used for image translation technique CycleGAN, which is
          used to train images that do not overlap. Imagenet-Each output
          tile will be labeled with a specific
          class. This format is used for object classification; however,
          it can also be
          used for object tracking when the Deep Sort model type is used during
          training. Panoptic_Segmentation-The output will be one
          classified image
          chip and one instance per input image chip. The output will also have
          image chips that mask the areas where the sample exists; these image
          chips will be stored in a different folder. This format is
          used for both pixel classification and instance
          segmentation, so two output labels folders will be produced.For the
          KITTI metadata format, 15 columns are created, but only 5 of
          them are used in the tool. The first column is the class value. The
          next 3 columns are skipped. Columns 5 through 8 define the minimum
          bounding rectangle, which is composed of four image coordinate
          locations: left, top, right, and bottom pixels. The minimum bounding
          rectangle encompasses the training chip used in the deep learning
          classifier. The remaining columns are not used. The following
          is an example of the PASCAL_VOC_rectangles
          option:        <?xml version=”1.0”?> - <layout>
          <image>000000000</image>
          <object>1</object> - <part> <class>1</class> - <bndbox>
          <xmin>31.85</xmin> <ymin>101.52</ymin> <xmax>256.00</xmax>
          <ymax>256.00</ymax> </bndbox> </part> </layout>For more information,
          see the Microsoft PASCAL Visual Object Classes
          (VOC) Challenge paper.
      start_index {Long}:
          Start Index
      class_value_field {Field}:
          The field that contains the class values. If no field is
          specified, the system searches for aorfield. The field should be
          numeric, usually an integer. If the feature does not contain a class
          field, the system determines that all records belong to one class.
          valueclassvalue
      buffer_radius {Double}:
          The radius of a buffer around each training sample that will be used
          to delineate a training sample area. This allows you to create
          circular polygon training samples from points.The linear unit of the
          in_class_data parameter value's spatial
          reference is used.
      in_mask_polygons {Feature Layer}:
          A polygon feature class that delineates the area where image chips
          will be created.Only image chips that fall completely within the
          polygons will be
          created.
      rotation_angle {Double}:
          The rotation angle that will be used to generate image chips.An image
          chip will first be generated with no rotation. It will then
          be rotated at the specified angle to create additional image chips.
          The image will be rotated and have a chip created, until it has been
          fully rotated. For example, if you specify a rotation angle of 45
          degrees, the tool will create eight image chips. The eight image chips
          will be created at the following angles: 0, 45, 90, 135, 180, 25, 270,
          and 315.The default rotation angle is 0, which creates one default
          image chip.
      reference_system {String}:
          Specifies the type of reference system that will be used to interpret
          the input image. The reference system specified must match the
          reference system used to train the deep learning model.MAP_SPACE-A
          map-based coordinate system will be used. This is the
          default.PIXEL_SPACE-Image space will be used, with no rotation and no
          distortion.
      processing_mode {String}:
          Specifies how all raster items in a mosaic dataset or an image service
          will be processed. This parameter is applied when the input raster is
          a mosaic dataset or an image service.PROCESS_AS_MOSAICKED_IMAGE-All
          raster items in the mosaic dataset or
          image service will be mosaicked together and processed. This is the
          default.PROCESS_ITEMS_SEPARATELY-All raster items in the mosaic
          dataset or
          image service will be processed as separate images.
      blacken_around_feature {Boolean}:
          Specifies whether the pixels around each object or feature in each
          image tile will be masked out.This parameter only applies when the
          metadata_format parameter is set
          to Labeled_Tiles and an input feature class or classified raster has
          been specified.NO_BLACKEN-Pixels surrounding objects or features will
          not be masked
          out. This is the default.BLACKEN_AROUND_FEATURE-Pixels surrounding
          objects or features will be
          masked out.
      crop_mode {String}:
          Specifies whether the exported tiles will be cropped so that they are
          all the same size.This parameter only applies when the metadata_format
          parameter is set
          to either Labeled_Tiles or Imagenet, and an input feature class or
          classified raster has been specified.FIXED_SIZE-Exported tiles will be
          cropped to the same size and will
          center on the feature. This is the default.BOUNDING_BOX-Exported tiles
          will be cropped so that the bounding
          geometry surrounds only the feature in the tile.
      in_raster2 {Raster Dataset / Raster Layer / Mosaic Layer / Image Service / Map Server / Map Server Layer / Internet Tiled Layer / Folder}:
          An additional input imagery source that will be used for image
          translation methods.This parameter is valid when the metadata_format
          parameter is set to
          Classified_Tiles, Export_Tiles, or CycleGAN.
      in_instance_data {Feature Class / Feature Layer / Raster Dataset / Raster Layer / Mosaic Layer / Image Service / Table / Folder}:
          The training sample data collected that contains classes for instance
          segmentation.The input can also be a point feature class without a
          class value
          field or an integer raster without class information.This parameter is
          only valid when the metadata_format parameter is set
          to Panoptic_Segmentation.
      instance_class_value_field {Field}:
          The field that contains the class values for instance segmentation. If
          no field is specified, the tool will use a value or class value field
          if one is present. If the feature does not contain a class field, the
          tool will determine that all records belong to one class.This
          parameter is only valid when the metadata_format parameter is set
          to Panoptic_Segmentation.
      min_polygon_overlap_ratio {Double}:
          The minimum overlap percentage for a feature to be included in the
          training data. If the percentage overlap is less than the value
          specified, the feature will be excluded from the training chip, and
          will not be added to the label file.The percent value is expressed as
          a decimal. For example, to specify
          an overlap of 20 percent, use a value of 0.2. The default value is 0,
          which means that all features will be included.This parameter improves
          the performance of the tool and also improves
          inferencing. The speed is improved since less training chips are
          created. The inferencing is improved since the model is trained to
          only detect large patches of objects and ignores small corners of
          features. This means less false positives will be detected, and less
          false positives will be removed by the Non Maximum Suppression
          tool.This parameter is enabled when the in_class_data parameter value
          is a
          feature class.

     OUTPUTS:
      out_folder (Folder):
          The folder where the output image chips and metadata will be
          stored.The folder can also be a folder URL that uses a cloud storage
          connection file (*.acs).

        """