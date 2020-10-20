import argparse
from PIL import Image
from pathlib import Path

def crop_by_factor(inp_path:Path, out_path:Path, *args, factor=0, **kwrags):
    'Centre crops Image by a given factor'
    alowed_types = {'.png', '.jpg', '.jpeg'}
    if not inp_path.suffix.lower() in alowed_types:
        raise TypeError('Only imgs allowed..')
    elif factor <= 0:
        raise ValueError('Factor cant be <= 0')

    else:
        if out_path.is_dir():
            out_path = out_path/inp_path.name
        img = Image.open(inp_path)
        if img.mode != 'RGB':
            img = img.convert('RGB')
        width, height = img.size
        new_width, new_height = int(width*factor), int(height*factor)
        if new_width > width:
            raise ValueError('Cant crop more than current image width') 
        elif new_height > height:
            raise ValueError('Cant crop more than current image height')
        else:            
            left = int(width/2 - new_width/2)
            upper = int(height/2 - new_height/2)
            right = left + new_width
            lower = upper + new_height
            img = img.crop((left, upper, right, lower))
            img.save(out_path.absolute())

if __name__ == "__main__":
    crop_by_factor(Path.cwd()/'027a5fee.jpg', Path.cwd()/'crp_p.jpg', .7 )