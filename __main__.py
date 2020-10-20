import argparse
import importlib
from pathlib import Path
import os
from tqdm import tqdm
from pprint import pprint

func_dict = {
    'j2p': 'jpg_to_png',
    'p2j': 'png_to_jpg',
    'crp_p': 'crop_by_factor',
    'crp_px': 'crop_by_dim',
    'res_h': 'resize_by_height',
    'res_p': 'resize_by_factor',
    'res_w': 'resize_by_width'
}

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('-m',
                         '--module',
                        type=str,
                        required=True,
                        help='module name, one of j2p, p2j, res_h, res_p, res_w, crp_p, crp_px, ')

    parser.add_argument('-i',
                         '--input',
                        type=str,
                        required=True,
                        help='Input folder or image')

    parser.add_argument('-o', 
                        '--output',
                        type=str,
                        default='',                        
                        help='Output image path or folder')
    parser.add_argument('--factor',
                        type=float,
                        default=0,                        
                        help='Factor by which to crop or resize')
    parser.add_argument('--new_size',
                        nargs=2,                        
                        type=int,                                               
                        help='New size of image file')
    parser.add_argument('--new_width',
                        type=int,                                               
                        help='New Width of image')
    parser.add_argument('--new_height',
                        type=int,                                               
                        help='New Height of image')
    args = parser.parse_args()
    mod = importlib.import_module(args.module)
    func = getattr(mod, func_dict.get(args.module))
    inp_path = Path(args.input)
    kwargs = vars(args)
    print('Given input')
    pprint({key:value for key, value in kwargs.items() if value})
    out_path = Path(args.output) if args.output else Path.cwd()/'output'
    print('Input path ', inp_path)
    print('Outpath ', out_path)
    if not out_path.exists():
        os.makedirs(out_path)
    if not inp_path.exists():
        raise FileNotFoundError(f'{inp_path} doesnt exist')
    elif inp_path.is_file():
        try:
            func(inp_path, out_path, **kwargs)
        except Exception as e:
            print(f'{e}, {inp_path}')
        finally:
            print('Done')
        
    elif inp_path.is_dir():
        for file in tqdm(inp_path.iterdir()):            
            try:
                func(file, out_path, **kwargs)
                
            except Exception as e:
                print(f'{e}, {file}')
        print('Done')

    else:
        print('Nothing to do')
            
