# Generated documentation for module arcpy.ia.Functions


class TrainDeepLearningModel(object):
    """
    Trains a deep learning model using the output from the Export Training Data For Deep Learning tool.
    """

    @property
    def description(self) -> str:
        return """

        TrainDeepLearningModel_ia(in_folder;in_folder..., out_folder, {max_epochs}, {model_type}, {batch_size}, {arguments;arguments...}, {learning_rate}, {backbone_model}, {pretrained_model}, {validation_percentage}, {stop_training}, {freeze}, {augmentation}, {augmentation_parameters;augmentation_parameters...}, {chip_size}, {resize_to}, {weight_init_scheme}, {monitor})

        Trains a deep learning model using the output from the Export Training
        Data For Deep Learning tool.

     INPUTS:
      in_folder (Folder):
          The folders containing the image chips, labels, and statistics
          required to train the model. This is the output from the Export
          Training Data For Deep Learning tool. Multiple input folders
          are supported when the following
          conditions are met:        The metadata format type must be classified
          tiles, labeled tiles,
          multilabeled tiles, Pascal Visual Object Classes, or RCNN masks.All
          training data must have the same metadata format.All training data
          must have the same number of bands.All training data must have the
          same tile size.
      max_epochs {Long}:
          The maximum number of epochs for which the model will be trained. A
          maximum epoch of one means the dataset will be passed forward and
          backward through the neural network one time. The default value is 20.
      model_type {String}:
          Specifies the model type that will be used to train the deep learning
          model.BDCN_EDGEDETECTOR-The Bi-Directional Cascade Network (BDCN)
          architecture will be used to train the model. BDCN Edge Detector is
          used for pixel classification. This approach is useful to improve edge
          detection for objects at different scales.CHANGEDETECTOR-The Change
          detector architecture will be used to train
          the model. Change detector is used for pixel classification. This
          approach creates a model object that uses two spatial-temporal images
          to create a classified raster of the change. The input training data
          for this model type uses the Classified Tiles metadata
          format.CONNECTNET-The ConnectNet architecture will be used to train
          the
          model. ConnectNet is used for pixel classification. This approach is
          useful for road network extraction from satellite imagery.CYCLEGAN-The
          CycleGAN architecture will be used to train the model.
          CycleGAN is used for image-to-image translation. This approach creates
          a model object that generates images of one type to another. This
          approach is unique in that the images to be trained do not need to
          overlap. The input training data for this model type uses the CycleGAN
          metadata format.DEEPLAB-The DeepLabV3 architecture will be used to
          train the model.
          DeepLab is used for pixel classification.DEEPSORT-The Deep Sort
          architecture will be used to train the model.
          Deep Sort is used for object detection in videos. The model is trained
          using frames of the video and detects the classes and bounding boxes
          of the objects in each frame. The input training data for this model
          type uses the Imagenet metadata format. While Siam Mask is useful for
          tracking an object, Deep Sort is useful in training a model to track
          multiple objects.DETREG-The DETReg architecture will be used to train
          the model. DETReg
          is used for object detection. The input training data for this model
          type uses the Pascal Visual Object Classes. This model type is GPU
          intensive; it requires a dedicated GPU with at least 16 GB of memory
          to run properly.FASTERRCNN-The FasterRCNN architecture will be used to
          train the
          model. FasterRCNN is used for object detection.FEATURE_CLASSIFIER-The
          Feature classifier architecture will be used to
          train the model. Feature Classifier is used for object or image
          classification.HED_EDGEDETECTOR-The Holistically-Nested Edge
          Detection (HED)
          architecture will be used to train the model. HED Edge Detector is
          used for pixel classification. This approach is useful for edge and
          object boundary detection.IMAGECAPTIONER-The Image captioner
          architecture will be used to train
          the model. Image captioner is used for image-to-text translation. This
          approach creates a model that generates text captions for an
          image.MASKRCNN-The MaskRCNN architecture will be used to train the
          model.
          MaskRCNN is used for object detection. This approach is used for
          instance segmentation, which is precise delineation of objects in an
          image. This model type can be used to detect building footprints. It
          uses the MaskRCNN metadata format for training data as input. Class
          values for input training data must start at 1. This model type can
          only be trained using a CUDA-enabled GPU.MAXDEEPLAB-The MaX-DeepLab
          architecture will be used to train the
          model. MaX-DeepLab is used for panoptic segmentation. This approach
          creates a model object that generates images and features. The input
          training data for this model type uses the Panoptic segmentation
          metadata format.MMDETECTION-The MMDetection architecture will be used
          to train the
          model. MMDetection is used for object detection. The supported
          metadata formats are Pascal Visual Object Class rectangles and KITTI
          rectangles.MMSEGMENTATION-The MMSegmentation architecture will be used
          to train
          the model. MMSegmentation is used for pixel classification. The
          supported metadata format is Classified Tiles.MULTITASK_ROADEXTRACTOR-
          The Multi Task Road Extractor architecture
          will be used to train the model. Multi Task Road Extractor is used for
          pixel classification. This approach is useful for road network
          extraction from satellite imagery.PIX2PIX-The Pix2Pix architecture
          will be used to train the model.
          Pix2Pix is used for image-to-image translation. This approach creates
          a model object that generates images of one type to another. The input
          training data for this model type uses the Export Tiles metadata
          format.PIX2PIXHD-The Pix2PixHD architecture will be used to train the
          model.
          Pix2PixHD is used for image-to-image translation. This approach
          creates a model object that generates images of one type to another.
          The input training data for this model type uses the Export Tiles
          metadata format.PSETAE-The Pixel-Set Encoders and Temporal Self-
          Attention (PSETAE)
          architecture will be used to train the model for time series
          classification. PSETAE is used for pixel classification. The
          preliminary data used for this method is multidimensional
          data.PSPNET-The Pyramid Scene Parsing Network (PSPNET) architecture
          will be
          used to train the model. PSPNET is used for pixel
          classification.RETINANET-The RetinaNet architecture will be used to
          train the model.
          RetinaNet is used for object detection. The input training data for
          this model type uses the Pascal Visual Object Classes metadata
          format.SAMLORA-The Segment anything model (SAM) with Low Rank Adaption
          (LoRA)
          will be used to train the model. This model type uses the Segment
          anything model (SAM) as a foundational model and will fine-tune to a
          specific task with relatively low computing requirements and a smaller
          dataset.SIAMMASK-The Siam Mask architecture will be used to train the
          model.
          Siam Mask is used for object detection in videos. The model is trained
          using frames of the video and detects the classes and bounding boxes
          of the objects in each frame. The input training data for this model
          type uses the MaskRCNN metadata format.SSD-The Single Shot Detector
          (SSD) architecture will be used to train
          the model. SSD is used for object detection. The input training data
          for this model type uses the Pascal Visual Object Classes metadata
          format.SUPERRESOLUTION-The Super-resolution architecture will be used
          to
          train the model. Super-resolution is used for image-to-image
          translation. This approach creates a model object that increases the
          resolution and improves the quality of images. The input training data
          for this model type uses the Export Tiles metadata format.UNET-The
          U-Net architecture will be used to train the model. U-Net is
          used for pixel classification.YOLOV3-The YOLOv3 architecture will be
          used to train the model. YOLOv3
          is used for object detection.
      batch_size {Long}:
          The number of training samples to be processed for training at one
          time.Increasing the batch size can improve tool performance; however,
          as
          the batch size increases, more memory is used.When not enough GPU
          memory is available for the batch size set, the
          tool tries to estimate and use an optimum batch size. If an out of
          memory error occurs, use a smaller batch size.
      arguments {Value Table}:
          The information from the model_type parameter will be used to set the
          default values for this parameter. These arguments vary, depending on
          the model architecture. The supported model arguments for models
          trained in ArcGIS are described below. ArcGIS pretrained models and
          custom deep learning models may have additional arguments that the
          tool supports.For more information about which arguments are available
          for each
          model type, see Deep learning arguments.attention_type-Specifies the
          module type. The module options are PAM
          (Pyramid Attention Module) or BAM (Basic Attention Module). The
          default is PAM.attn_res-The number of attentions in residual blocks.
          This is an
          optional integer value. The default is 16. This argument is only
          supported when the backbone_model parameter value is
          SR3.channel_mults-Optional depth multipliers for subsequent
          resolutions in
          U-Net. The default is 1, 2, 4, 4, 8, 8. This argument is only
          supported when the backbone_model parameter value is
          SR3.CLASS_BALANCING-Specifies whether the cross-entropy loss inverse
          will
          be balanced to the frequency of pixels per class. The default is
          False. decode_params-A dictionary that controls how the Image
          captioner will run. The default value is {'embed_size':100,
          'hidden_size':100, 'attention_size':100, 'teacher_forcing':1,
          'dropout':0.1, 'pretrained_emb':False}. The decode_params argument is
          composed of the following parameters:. embed_size-The
          embedding size. The default is 100 layers in the neural
          network.hidden_size-The hidden layer size. The default is 100 layers
          in the
          neural network.attention_size-The intermediate attention layer size.
          The default is
          100 layers in the neural network.teacher_forcing-The probability of
          teacher forcing. Teacher forcing is
          a strategy for training recurrent neural networks. It uses model
          output from a prior time step as an input, instead of the previous
          output, during back propagation. The valid range is 0.0 to 1.0. The
          default is 1.dropout-The dropout probability. The valid range is 0.0
          to 1.0. The
          default is 0.1.pretrained_emb-Specifies whether pretrained text
          embedding will be
          used. If True, it will use fast text embedding. If False, it will not
          use pretrained text embedding. The default is False.dropout-An
          optional floating point value for dropout. The default is
          0. This argument is only supported when the backbone_model parameter
          value is SR3.FOCAL_LOSS-Specifies whether focal loss will be used. The
          default is
          False.gaussian_thresh-The Gaussian threshold, which sets the required
          road
          width. The valid range is 0.0 to 1.0. The default is 0.76.grids-The
          number of grids the image will be divided into for
          processing. For example, setting this argument to 4 means the image
          will be divided into 4 x 4 or 16 grid cells. If no value is specified,
          the optimal grid value will be calculated based on the input
          imagery.IGNORE_CLASSES-The list of class values on which the model
          will not
          incur loss.inner_channel  -The inner_channel is the dimension of the
          first U-net
          layer. This is an optional integer value. The default is 64. This
          argument is only supported when the backbone_model parameter value is
          SR3.linear_start-An optional integer to schedule the start. The
          default is
          1e-02. This argument is only supported when the backbone_model
          parameter value is SR3.linear_end-An optional integer to schedule the
          end. The default is
          1e-06. This argument is only supported when the backbone_model
          parameter value is SR3.MIXUP-Specifies whether mixup augmentation and
          mixup loss will be
          used. The default is False.model-The backbone model used to train the
          model. The available
          options depend on the model_type parameter value. The default for
          MMDETECTION is cascade_rcnn. The default for MMSegmentation is
          deeplabv3.model_weight-Specifies whether pretrained model weights will
          be used.
          The default is False. The value can also be a path to a configuration
          file containing the weights of a model from the MMDetection repository
          or the MMSegmentation repositorymonitor-Specifies the metric to
          monitor while checkpointing and early
          stopping. The available metrics depend on the model_type parameter
          value. The default is valid_loss.mtl_model-Specifies the architecture
          type that will be used to create
          the model. The options are linknet or hourglass for linknet-based or
          hourglass-based, respectively, neural architectures. The default is
          hourglass.n_timestep-An optional value for the number of diffusion
          time steps.
          The default is 1000. This argument is only supported when the
          backbone_model parameter value is SR3.norm_groups  -The number of
          groups for group normalization. This is
          an optional integer value. The default is 32. This argument is only
          supported when the backbone_model parameter value is
          SR3.orient_bin_size-The bin size for orientation angles. The default
          is
          20.orient_theta-The width of orientation mask. The default is
          8.PYRAMID_SIZES-The number and size of convolution layers to be
          applied
          to the different subregions. The default is [1,2,3,6]. This argument
          is specific to the PSPNET model.ratios-The list of aspect ratios to
          use for the anchor boxes. In
          object detection, an anchor box represents the ideal location, shape,
          and size of the object being predicted. For example, setting this
          argument to [1.0,1.0], [1.0, 0.5] means the anchor box is a square
          (1:1) or a rectangle in which the horizontal side is half the size of
          the vertical side (1:0.5). The default for RETINANET is [0.5,1,2]. The
          default for SSD is [1.0, 1.0].res_blocks-The number of residual
          blocks. This is an optional integer
          value. The default is 3. This argument is only supported when the
          backbone_model parameter value is SR3.SCALES-The number of scale
          levels each cell will be scaled up or down.
          The default is [1, 0.8, 0.63].schedule-Optionally set the type of
          schedule to use. Available options
          are linear, warmup10, warmup50, const, jsd, cosine. The default is
          linear. This argument is only supported when the backbone_model
          parameter value is SR3.USE_UNET-Specifies whether the U-Net decoder
          will be used to recover
          data once the pyramid pooling is complete. The default is True. This
          argument is specific to the PSPNET model.zooms-The number of zoom
          levels each grid cell will be scaled up or
          down. Setting this argument to 1 means all the grid cells will remain
          at the same size or zoom level. A zoom level of 2 means all the grid
          cells will become twice as large (zoomed in 100 percent). Providing a
          list of zoom levels means all the grid cells will be scaled using all
          the numbers in the list. The default is 1.
      learning_rate {Double}:
          The rate at which existing information will be overwritten with newly
          acquired information throughout the training process. If no value is
          specified, the optimal learning rate will be extracted from the
          learning curve during the training process.
      backbone_model {String}:
          Specifies the preconfigured neural network that will be used as the
          architecture for training the new model. This method is known as
          Transfer Learning.DENSENET121-The preconfigured model will be a dense
          network trained on
          the Imagenet Dataset that contains more than 1 million images and is
          121 layers deep. Unlike ResNET, which combines the layer using
          summation, DenseNet combines the layers using
          concatenation.DENSENET161-The preconfigured model will be a dense
          network trained on
          the Imagenet Dataset that contains more than 1 million images and is
          161 layers deep. Unlike ResNET, which combines the layer using
          summation, DenseNet combines the layers using
          concatenation.DENSENET169-The preconfigured model will be a dense
          network trained on
          the Imagenet Dataset that contains more than 1 million images and is
          169 layers deep. Unlike ResNET, which combines the layer using
          summation, DenseNet combines the layers using
          concatenation.DENSENET201-The preconfigured model will be a dense
          network trained on
          the Imagenet Dataset that contains more than 1 million images and is
          201 layers deep. Unlike ResNET, which combines the layer using
          summation, DenseNet combines the layers using
          concatenation.MOBILENET_V2-The preconfigured model will be trained on
          the Imagenet
          Database and is 54 layers deep and intended for Edge device computing,
          since it uses less memory.RESNET18-The preconfigured model will be a
          residual network trained on
          the Imagenet Dataset that contains more than million images and is 18
          layers deep.RESNET34-The preconfigured model will be a residual
          network trained on
          the Imagenet Dataset that contains more than 1 million images and is
          34 layers deep. This is the default.RESNET50-The preconfigured model
          will be a residual network trained on
          the Imagenet Dataset that contains more than 1 million images and is
          50 layers deep.RESNET101-The preconfigured model will be a residual
          network trained
          on the Imagenet Dataset that contains more than 1 million images and
          is 101 layers deep.RESNET152-The preconfigured model will be a
          residual network trained
          on the Imagenet Dataset that contains more than 1 million images and
          is 152 layers deep.VGG11-The preconfigured model will be a convolution
          neural network
          trained on the Imagenet Dataset that contains more than 1 million
          images to classify images into 1,000 object categories and is 11
          layers deep.VGG11_BN-The preconfigured model will be based on the VGG
          network but
          with batch normalization, which means each layer in the network is
          normalized. It trained on the Imagenet dataset and has 11
          layers.VGG13-The preconfigured model will be a convolution neural
          network
          trained on the Imagenet Dataset that contains more than 1 million
          images to classify images into 1,000 object categories and is 13
          layers deep.VGG13_BN-The preconfigured model will be based on the VGG
          network but
          with batch normalization, which means each layer in the network is
          normalized. It trained on the Imagenet dataset and has 13
          layers.VGG16-The preconfigured model will be a convolution neural
          network
          trained on the Imagenet Dataset that contains more than 1 million
          images to classify images into 1,000 object categories and is 16
          layers deep.VGG16_BN-The preconfigured model will be based on the VGG
          network but
          with batch normalization, which means each layer in the network is
          normalized. It trained on the Imagenet dataset and has 16
          layers.VGG19-The preconfigured model will be a convolution neural
          network
          trained on the Imagenet Dataset that contains more than 1 million
          images to classify images into 1,000 object categories and is 19
          layers deep.VGG19_BN-The preconfigured model will be based on the VGG
          network but
          with batch normalization, which means each layer in the network is
          normalized. It trained on the Imagenet dataset and has 19
          layers.DARKNET53-The preconfigured model will be a convolution neural
          network
          trained on the Imagenet Dataset that contains more than 1 million
          images and is 53 layers deep.REID_V1-The preconfigured model will be a
          convolution neural network
          trained on the Imagenet Dataset that is used for object
          tracking.REID_V2-The preconfigured model will be a convolution neural
          network
          trained on the Imagenet Dataset that is used for object
          tracking.RESNEXT50-The preconfigured model will be a convolution
          neural network
          trained on the Imagenet Dataset and is 50 layers deep. It is a
          homogeneous neural network, which reduces the number of
          hyperparameters required by conventional ResNet.WIDE_RESNET50-The
          preconfigured model will be a convolution neural
          network trained on the Imagenet Dataset and is 50 layers deep. It has
          the same architecture as ResNET but with more channels.SR3-The
          preconfigured model will use the Super Resolution via Repeated
          Refinement (SR3) model. SR3 adapts denoising diffusion probabilistic
          models to conditional image generation and performs super-resolution
          through a stochastic denoising process. For more information, see
          Image Super-Resolution via Iterative Refinement.VIT_B-The
          preconfigured Segment Anything Model (SAM) will be used with
          a base neural network size. This is the smallest size. For more
          information, see Segment Anything.VIT_L-The preconfigured Segment
          Anything Model (SAM) will be used with
          a large neural network size. For more information, see Segment
          Anything.VIT_H-The preconfigured Segment Anything Model (SAM) will be
          used with
          a huge neural network size. This is the largest size. For more
          information, see Segment Anything.Additionally, supported convolution
          neural networks from the PyTorch
          Image Models (timm) can be specified using timm as a prefix, for
          example, timm:resnet31 , timm:inception_v4 , timm:efficientnet_b3, and
          so on.
      pretrained_model {File}:
          A pretrained model that will be used to fine-tune the new model. The
          input is an Esri model definition file (.emd) or a deep learning
          package file (.dlpk).A pretrained model with similar classes can be
          fine-tuned to fit the
          new model. The pretrained model must have been trained with the same
          model type and backbone model that will be used to train the new
          model.
      validation_percentage {Double}:
          The percentage of training samples that will be used for validating
          the model. The default value is 10.
      stop_training {Boolean}:
          Specifies whether early stopping will be
          implemented.STOP_TRAINING-Early stopping will be implemented, and the
          model
          training will stop when the model is no longer improving, regardless
          of the max_epochs parameter value specified. This is the
          default.CONTINUE_TRAINING-Early stopping will not be implemented, and
          the
          model training will continue until the max_epochs parameter value is
          reached.
      freeze {Boolean}:
          Specifies whether the backbone layers in the pretrained model will be
          frozen, so that the weights and biases remain as originally
          designed.FREEZE_MODEL-The backbone layers will be frozen, and the
          predefined
          weights and biases will not be altered in the backbone_model
          parameter. This is the default.UNFREEZE_MODEL-The backbone layers will
          not be frozen, and the weights
          and biases of the backbone_model parameter can be altered to fit the
          training samples. This takes more time to process but typically
          produces better results.
      augmentation {String}:
          Specifies the type of data augmentation that will be used.Data
          augmentation is a technique of artificially increasing the
          training set by creating modified copies of a dataset using existing
          data. DEFAULT-The default data augmentation methods and values
          will
          be used. The default data augmentation methods included are
          crop,
          dihedral_affine, brightness, contrast, and zoom. These default values
          typically work well for satellite imagery.NONE-No data augmentation
          will be used.CUSTOM-Data augmentation values will be specified using
          the
          augmentation_parameters parameter. FILE-Fastai transforms for
          data augmentation of training and
          validation datasets will be specified using the transforms.json file,
          which is in the same folder as the training data         For more
          information about the various transformations, see vision
          transforms on the fastai website.
      augmentation_parameters {Value Table}:
          Specifies the value for each transform in the augmentation
          parameter. rotate-The image will be randomly rotated (in
          degrees) by a
          probability (p). If degrees is a range (a,b), a value will be
          uniformly assigned from a to b. The default value is 30.0;
          0.5.brightness-The brightness of the image will be randomly adjusted
          depending on the value of change, with a probability (p). A change of
          0 will transform the image to darkest, and a change of 1 will
          transform the image to lightest. A change of 0.5 will not adjust the
          brightness. If change is a range (a,b), the augmentation will
          uniformly assign a value from a to b. The default value is (0.4,0.6);
          1.0.contrast-The contrast of the image will be randomly adjusted
          depending
          on the value of scale with probability (p). A scale of 0 will
          transform the image to gray scale, and a scale greater than 1 will
          transform the image to super contrast. A scale of 1 doesn't adjust the
          contrast. If scale is a range (a,b), the augmentation will uniformly
          assign a value from a to b. The default value is (0.75, 1.5);
          1.0.zoom-The image will be randomly zoomed in depending on the value
          of
          scale. The zoom value is in the form scale(a,b); p. The default value
          is (1.0, 1.2); 1.0 in which p is the probability. Only a scale of
          greater than 1.0 will zoom in on the image. If scale is a range (a,b),
          it will uniformly assign a value from a to b.crop-The image will be
          randomly cropped. The crop value is in the form
          size;p;row_pct;col_pct in which p is probability. The position is
          given by (col_pct, row_pct), with col_pct and row_pct being normalized
          between 0 and 1. If col_pct or row_pct is a range (a,b), it will
          uniformly assign a value from a to b. The default value is
          chip_size;1.0; (0, 1); (0, 1) in which 224 is the default chip size.
      chip_size {Long}:
          The size of the image that will be used to train the model. Images
          will be cropped to the specified chip size. If the image size is less
          than the parameter value, the image size will be used.The default chip
          size will be the same as the tile size of the
          training data. If the x- and y- tile size are not the same, the larger
          value will be used.
      resize_to {String}:
          Resizes the image chips. Once a chip is resized, pixel blocks of chip
          size will be cropped and used for training. This parameter applies to
          object detection (PASCAL VOC), object classification (labeled tiles),
          and super-resolution data only.The resize value is often half the chip
          size value. If this resize
          value is less than the chip size value, the resize value is used to
          create the pixel blocks for training.
      weight_init_scheme {String}:
          Specifies the scheme in which the weights will be initialized for the
          layer.To train a model with multispectral data, the model must
          accommodate
          the various types of bands available. This is done by reinitializing
          the first layer in the model.RANDOM-Random weights will be initialized
          for non-RGB bands, while
          pretrained weights will be preserved for RGB bands. This is the
          default.RED_BAND-Weights corresponding to the red band from the
          pretrained
          model's layer will be cloned for non-RGB bands, while pretrained
          weights will be preserved for RGB bands.ALL_RANDOM-Random weights
          will be initialized for RGB bands as well
          as non-RGB bands. This option applies only to multispectral
          imagery.This parameter is only applicable when multispectral imagery
          is used
          in the model.
      monitor {String}:
          Specifies the metric that will be monitored while checkpointing and
          early stopping.VALID_LOSS-The validation loss will be monitored. When
          the validation
          loss no longer changes significantly, the model will stop. This is the
          default.AVERAGE_PRECISION-The weighted mean of precision at each
          threshold
          will be monitored. When this value no longer changes significantly,
          the model will stop.ACCURACY-The ratio between the number of correct
          predictions to the
          total number of predictions will be monitored. When this value no
          longer changes significantly, the model will stop.F1_SCORE-The
          combination of the precision and recall scores of a model
          will be monitored. When this value no longer changes significantly,
          the model will stop.MIOU-The average between the intersection over
          union (IoU) of the
          segmented objects over all the images of the test dataset will be
          monitored. When this value no longer changes significantly, the model
          will stop. DICE-Model performance will be monitored using the
          Dice
          metric. When this value no longer changes significantly, the model
          will stop. This value can range from 0 to 1. The value 1
          corresponds to a pixel
          perfect match between the validation data and training data.
          PRECISION-The precision, which measures the model's accuracy
          in classifying a sample as positive, will be monitored. When this
          value no longer changes significantly, the model will stop.
          The precision is the ratio between the number of positive samples
          correctly classified and the total number of samples classified
          (either correctly or incorrectly). RECALL-The recall, which
          measures the model's ability to
          detect positive samples, will be monitored. When this value no longer
          changes significantly, the model will stop. The higher the
          recall, the more positive samples are detected. The
          recall value is the ratio between the number of positive samples
          correctly classified as positive and the total number of positive
          samples. CORPUS_BLEU-The Corpus blue score will be monitored.
          When
          this value no longer changes significantly, the model will stop.
          This score is used to calculate accuracy for multiple sentences, such
          as a paragraph or a document. MULTI_LABEL_FBETA-The weighted
          harmonic mean of precision and
          recall will be monitored. When this value no longer changes
          significantly, the model will stop. This is often referred to
          as the F-beta score.

     OUTPUTS:
      out_folder (Folder):
          The output folder location where the trained model will be stored.

        """