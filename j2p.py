import argparse
from PIL import Image
from pathlib import Path

def jpg_to_png(inp_path:Path, out_path:Path, *args, **kwargs):
    'Converts jpeg or jpg to png'
    alowed_types = {'.jpg', '.jpeg'}
    if not inp_path.suffix.lower() in alowed_types:
        raise TypeError('Only jpegs and jpgs allowed..')
    if out_path.is_dir():
        out_path = out_path/(inp_path.stem+'.png')
    
    img = Image.open(inp_path)
    img.save(out_path)

if __name__ == "__main__":
    out_ext = '.png'
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file',
                        type=str,
                        required=True,
                        help='Input JPG')

    parser.add_argument('-o', '--output',
                        type=str,
                        default='',                        
                        help='Output png path')
    args = parser.parse_args()
    inp_path = Path(args.file)
    if not inp_path.exists():
        raise FileNotFoundError(f'{inp_path} doesnt exist')
    out_path = Path(args.output) if args.output else  Path.cwd()
    out_path = Path.cwd()
    jpg_to_png(inp_path, out_path)


