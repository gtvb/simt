## Simple Image Manipulation Tool `simt`

Created to demonstrate how we can simply put together a simple Python
CLI to apply simple manipulations to images.

```
usage: sitm [-h] {resize,change-format,filter,crop} ...

A simple tool to execute fast image manipulations

positional arguments:
  {resize,change-format,filter,crop}
    resize              Resize an image
    change-format       Change the format of an image
    filter              Apply a filter to an image
    crop                Crop an image

options:
  -h, --help            show this help message and exit
```

To run the application you must:
- Create a virtual env: `python -m venv <your_venv_name>`
- Source it: `source <your_venv_name>/bin/activate`
- Install the dependencies with `pip install -r requirements.txt`
