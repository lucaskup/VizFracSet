# VizFracSet 
This repository features a dataset of fractures for computer vision algorithms, machine learning with Geological rigor.

<p align="center">
<img src="https://github.com/lucaskup/VizFracSet/blob/master/sample/all.png" width="700" alt="Results"> 
</p>

## Project tree
This dataset provides three versions for every annotation. By doing this we preserve geological context and georeferencing needed for some types of studies.
For computational and statistical evaluation of ML algorithms we provide Coco Annotations and binary masks generated from the georreferenced images.


```
├── dataset
│   ├── vector              # QGIS project files, Georreferenced TIFF and Shape files were fractures are marked
│   ├── pixel               # PNG version of the TIFF files and coco annotations for the apperture of fractures 
│   └── mask                # Binary png file with fractures shown as white
├── sample                  # Sample images for README
└── scripts                 # usefull python 3.x scripts to handle the dataset
    ├── convTiff_To_PNG.py  # Converts TIFF to PNG
    └──createMasksCOCO.py   # Creates mask file from PNG + Coco Annotations
```
## Published articles 
Yet to be published.



# Table of contents 

- [Requirements](#requirements) 
- [Usage](#usage) 
- [How to cite](#how-to-cite) 
- [Credits](#credits) 
- [License](#license) 

## Requirements

``` 
numpy

``` 

## Usage

## How to cite

If you find our work useful in your research please consider citing our paper: 
```

  ```


## Credits
This work is credited to the [Vizlab | X-Reality and GeoInformatics Lab](http://www.vizlab.unisinos.br/) and the following authors and developers: [Lucas Silveira Kupssinskü](https://www.researchgate.net/profile/Lucas_Kupssinskue).


## License
``` 
MIT Licence (https://mit-license.org/) 
``` 


