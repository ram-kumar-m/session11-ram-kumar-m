# Assignment 11
**Create these modules**:
1. jpg/jpeg to png conversion (use PIL library) j2p
2. png to jpg conversion (use PIL library) p2j
3. image resizer that can resize bulk images with these features:
   1. resize by user determined percentage (say 50% for height and width) (proportional) res_p
    2. resize by user determined width (proportional) res_w
    3. resize by user determined height (proportional) res_h
4. image cropper that can crop bulk images with these features:
    1. center square/rectangle crop by user-determined pixels crp_px
    1. centre square/rectangle crop by user-determined percentage (crop to 50%/70%) crp_p
    1.  it let's user know which all images were not cropped due to size mismatches
    1.  a __main__ module that exposes all these features (using argparse)
    1. finally create an zipped app, that exposes all of these features**

# __Tiny Image App in Python__
A small command image manipulator app written in python,
It can manipulate images one at a time or in bulk.
 ## Resize by
 - Height
 - Width
 - percentage like 0.5 etc..
## Centre/Rectangular Crop by
 -  given dimensions, keeps  
 -  percentage like 0.5 etc..
## Change file types:
 - jpg, jpeg to png
 - png to jpg
  
## Invocation:
>Copy the standalone file `app` and use it from anywhere.

```python app -m module_name -i input_path -o output_path --args ```

>where module_name is the name of the module and args arguments based on module name.

> All paths can be file or folder, uses original name for file if none specified

> Makes output_path if it does not exist

## __Modules__
> Saves in  a directory called `ouput` in current working directory if no output path is specified.

  ##  `j2p`
  Coverts given jpg/jepg image into png image.
  eg.

  `python app -m j2p -i ./a/b/c.jpg -o ./f/j/k.png`
  
or

`python app -m j2p -i ./a/b/ -o ./f/j/`

finds all jpg/jpeg images in b and saves them in j using original file names

 ## `p2j`
  Coverts given png image into jpg image.
  eg.

  `python app -m p2j -i ./a/b/c.png -o ./f/j/k.jpg`
  
or

`python app -m p2j -i ./a/b/ -o ./f/j/`

finds all png images in b and saves them in j as jpg using original file names

 ## `res_h`

Resizes images to have given height while keeping the aspect ratio.

`python app -m res_h -i ./a/b/c.jpg -o ./f/g.jpg --new_height height`
>where height is the new height in pixels

eg:

`python app -m res_h -i ./a/b/ -o ./f/ --new_height 200`

> Resizes all images in directory `b` and saves into directory `f` to have height 200 pixels

  ## `res_w`

Resizes images to have given width while keeping the aspect ratio.

`python app -m res_w -i ./a/b/c.jpg -o ./f/g.jpg --new_width width`
>where height is the new height in pixels

eg:

`python app -m res_w -i ./a/b/ -o ./f/ --new_width 224`

> Resizes all images in directory `b` and saves into directory `f`  to have width of 224 pixels.

  ## `res_p`

Resizes images by a given factor while keeping the aspect ratio.
>Reduce image to 70% -> factor=.7

>factor can be greater than 1 

`python app -m res_p -i ./a/b/c.jpg -o ./f/g.jpg --factor value`

eg:

`python app -m res_p -i ./a/b/ -o ./f/ --factor 2`

> Doubles the size of  all images in directory `b` and saves into directory `f`.

  ## `crp_p`

Cenre/Rectangular Crops images by a given factor while keeping the aspect ratio.
>factor can't be greater than 1 

`python app -m crp_p -i ./a/b/c.jpg -o ./f/g.jpg --factor value`

eg:

`python app -m crp_p -i ./a/b/ -o ./f/ --factor .5`

> Crops of  all images in directory `b` by a factor and saves into directory `f`.

  ## `crp_px`

Cenre/Rectangular Crops images by a given to have a given dimension from the centre.
> given dimensions can't be greater than the images dimensions.

`python app -m crp_px -i ./a/b/c.jpg -o ./f/g.jpg --new_size val1 val2`
>where val1 and val2 are the new width and height respectively.

> more than 2 values will give an error.
eg:

`python app -m crp_px -i ./a/b/ -o ./f/ --new_size 224 224`

> Crops of  all images in directory `b` by a factor and saves into directory `f` to be 224x224.

## **Test Cases (Pytest)**
>The names of the tests are so that `'test_'` prefix is added to the function it tests, suffied by the what the test does.

### `test_readme_exists`
   Checks if there is a README.md file in the same folder.

### `test_readme_contents`
   Checks if the README.md file has alteast 500 words.

### `test_readme_proper_description`
   Checks if the required functions are present in the README.md file.

### `test_readme_file_for_formatting`
   Checks if there are adequete headings present in the README.md file.

### `test_indentations`
   Checks if proper indentations are present throughout the python file.
   using the rule of 4 spaces equals 1 Tab.

### `test_function_name_had_cap_letter`
   Checks if any one the functions have capital letters used in their names, which breaks the PEP8 conventions.
   
### _Annotation and Docstring tests_
tests if any of the functions in function list don't have annotations or docstrings

### `test_j2p`
   Checks if given 20 images in test_images get converted into png via the command line.

### `test_p2j`
   Checks if given 20 newly made png images from the test above get converted back into jpg via the command line.

### `test_res_h`
  Tests to see all the images in test_images are resized to have height 500 via the command line. Also verifies the new height of new images.

### `test_res_w`
  Tests to see all the images in test_images are resized to have width 500 via the command line. Also verifies the new width of final images.

### `test_res_p`
  Tests to see all the images in test_images are resized to 50 percent of their original size via the command line. Also verifies the new dimension of final images.

### `test_crp_p`
  Tests to see all the images in test_images are centre cropped to 80 percent of their original size via the command line. Also verifies the new dimension of final images.

### `test_crp_px`
  Tests to see all the images in test_images are centre cropped to 224x224 via the command line. Also verifies the new dimension of final images.

### `test_crp_px_invalid_width`
 Tests if a negative width to the module crp_px raises a `ValueError`


### `test_crp_px_invalid_height`
 Tests if a negative height to the module crp_px raises a `ValueError`

### `test_crp_px_invalid_dim`
 Tests if a size greter than original image size to the module crp_px raises a `ValueError`.

### `test_res_w_invalid_width`
 Tests if a negative width to the module res_w raises a `ValueError`

### `test_res_h_invalid_width`
 Tests if a negative height to the module res_h raises a `ValueError`

### `test_res_p_invalid_factor`
 Tests if a negative factor to the module res_p raises a `ValueError`

### `test_j2p_invalid_ext`
 Tests if an invalid extension like png in  this case raises a `ValueError`

### `test_p2j_invalid_ext`
 Tests if an invalid extension like jpg in  this case raises a `ValueError`