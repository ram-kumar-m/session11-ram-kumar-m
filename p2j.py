import argparse
from PIL import Image
from pathlib import Path

def png_to_jpg(inp_path:Path, out_path:Path, *args, **kwargs):
    'Converts png to jpg'
    alowed_types = {'.png'}
    if not inp_path.suffix.lower() in alowed_types:
        raise TypeError('Only pngs allowed..')
    if out_path.is_dir():
        out_path = out_path/(inp_path.stem+'.jpg')

    img = Image.open(inp_path)
    if img.mode != 'RGB':
        img = img.convert('RGB')
    img.save(out_path.absolute())

if __name__ == "__main__":
    out_ext = '.jpg'
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file',
                        type=str,
                        required=True,
                        help='Input png')

    parser.add_argument('-o', '--output',
                        type=str,
                        default='',                        
                        help='Output jpg path')
    args = parser.parse_args()
    inp_path = Path(args.file)
    if not inp_path.exists():
        raise FileNotFoundError(f'{inp_path} doesnt exist')
    out_path = Path(args.output) if args.output else  Path.cwd()/(inp_path.stem+out_ext)
    png_to_jpg(inp_path, out_path)