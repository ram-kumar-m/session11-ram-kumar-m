import argparse
from PIL import Image
from pathlib import Path

def crop_by_dim(inp_path:Path, out_path:Path, *args, new_size=tuple(), **kwargs):
    'Centre Crops image by given dimensions '
    alowed_types = {'.png', '.jpg', '.jpeg'}
    new_width, new_height = new_size
    if not inp_path.suffix.lower() in alowed_types:
        raise TypeError('Only imgs allowed..')
    elif new_width <= 0:
        raise ValueError('Width must be greater than zero')
    elif new_height <= 0:
        raise ValueError('Height must be greater than zero')
    else:
        img = Image.open(inp_path)
        if img.mode != 'RGB':
            img = img.convert('RGB')
        width, height = img.size
        
        if new_width > width:
            raise ValueError(f'Cant crop more than current image width {width}') 
        elif new_height > height:
            raise ValueError(f'Cant crop more than current image height {height}')
        else:
            if out_path.is_dir():
                out_path = out_path/inp_path.name                   
            left = int(width/2 - new_width/2)
            upper = int(height/2 - new_height/2)
            right = left + new_width
            lower = upper + new_height
            img = img.crop((left, upper, right, lower))
            img.save(out_path.absolute())

if __name__ == "__main__":
    crop_by_dim(Path.cwd()/'027a5fee.jpg', Path.cwd()/'crp_px.jpg', (130,100) )