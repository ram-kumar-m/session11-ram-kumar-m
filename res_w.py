import argparse
from PIL import Image
from pathlib import Path

def resize_by_width(inp_path:Path, out_path:Path, *args, new_width = 0, **kwargs):
    'Converts png to jpg'
    alowed_types = {'.png', '.jpg', '.jpeg'}
    if not inp_path.suffix.lower() in alowed_types:
        raise TypeError(f'Only imgs allowed {inp_path}')
    elif new_width <= 0:
        raise ValueError('Width must be greater than zero')
    else:
        if out_path.is_dir():
            out_path = out_path/inp_path.name
        img = Image.open(inp_path)
        if img.mode != 'RGB':
            img = img.convert('RGB')
        width, height = img.size
        factor = new_width/width
        img = img.resize((int(width*factor), int(height*factor)))
        img.save(out_path.absolute())
if __name__ == "__main__":
    resize_by_width(Path.cwd()/'027a5fee.jpg', Path.cwd()/'res_w.jpg', 100 )