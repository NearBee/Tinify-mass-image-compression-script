<!-- # Compression Script (Using tinify (TinyPNG))

In this small script the user would provide the directory in which they would want their images compressed from, as well as using their API key provided by [TinyPNG.com](https://tinypng.com/developers) (First 500 compressions of the month are free!), the result would be that the script would mass compress the image files within the directory (provided the files are .jpg/.png/.jpeg file types) and overwrite the current image files with the new compressed versions. -->

# Tinify Image Compressor
This Python script compresses mass amounts of images using the Tinify API.

## Requirements
- `Python` 3.x
- `pathlib` library
- `os` library
- `sys` library
- `datetime` library
- `tinify` library

## Installation
1. Clone the repository or download the script.
2. Install the required libraries with pip:

```python
pip install pathlib os sys datetime tinify
```  

3. Get an API key from [TinyPNG](https://tinypng.com/developers) and add it as a command-line argument when 
running the script replace `[directory]` with the path to the directory containing the images you want to compress, and `[API_key]` with your Tinify API key.


```python
python tinify_compress.py [directory] [API_key]
```

## Usage
1. Open your terminal and navigate to the directory where the script is located.
2. Run the script with the required command-line arguments:
```python
python tinify_compress.py [directory] [API_key]
```
3. The script will validate the directory and API key, and then begin compressing all .jpg, .jpeg, and .png files in the specified directory using the Tinify API.
4. Once compression is complete, the script will output a message indicating that all images in the directory have been compressed.


## Contact
If you have any questions or comments, please feel free to contact the project author at Nathaniel.t.berube@gmail.com .