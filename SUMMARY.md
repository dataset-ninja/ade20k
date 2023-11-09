**ADE20K** is a dataset for instance segmentation, semantic segmentation, and object detection tasks. It is applicable or relevant across various domains. Also, it is used in the robotics industry. 

The dataset consists of 27574 images with 712812 labeled objects belonging to 3579 different classes including *wall*, *sky*, *floor*, and other: *window*, *ceiling*, *building*, *door*, *person*, *tree*, *trees*, *road*, *chair*, *picture*, *plant*, *car*, *cabinet*, *sidewalk*, *table*, *sign*, *ground*, *grass*, *curtain*, *mountain*, *column*, *street light*, *table lamp*, *bed*, *mirror*, and 3551 more.

Images in the ADE20K dataset have pixel-level instance segmentation annotations. Due to the nature of the instance segmentation task, it can be automatically transformed into a semantic segmentation (only one mask for every class) or object detection (bounding boxes for every object) tasks. All images are labeled (i.e. with annotations). There are 2 splits in the dataset: *training* (25574 images) and *validation* (2000 images). Additionally, every image contains information about ***scene***. The dataset was released in 2019 by the Massachusetts Institute of Technology, USA and University of Toronto, Canada.

Here is the visualized example grid with animated annotations:

[animated grid](https://github.com/dataset-ninja/ade20k/raw/main/visualizations/horizontal_grid.webm)
