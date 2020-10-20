import __main__ as main
import pytest
import random
import os
import inspect
import re
import subprocess
from pathlib import Path
import os
import shutil
import math
from PIL import Image
random_list = random.choices(range(1000), k=5)

test_folder = Path('./test_images/')
test_out = Path('./test_out')

def test_j2p():
    test_out = './test_out'
    subprocess.run(['python', 'app', '-m', 'j2p', '-i', test_folder, '-o', test_out])
    test_out = Path(test_out)
    for file in test_out.iterdir():
        assert file.suffix =='.png', f'Error at file {file}'
    
def test_p2j():
    test_in = Path('./test_out')
    test_out = Path('./test_jpg')
    subprocess.run(['python', 'app', '-m', 'p2j', '-i', test_in, '-o', test_out])
    
    for file in test_out.iterdir():
        assert file.suffix =='.jpg', f'Error at file {file}'
    shutil.rmtree(test_in)
    shutil.rmtree(test_out)

def test_res_h():
    new_height = 500
    subprocess.run(['python', 'app', '-m', 'res_h', '-i', test_folder, '-o', test_out, '--new_height', str(new_height)])
    
    for file in test_out.iterdir():
        img = Image.open(file)
        assert math.isclose(img.height, new_height, abs_tol=3), \
        f'Error at file {file} with found height {img.height} and new height {new_height}'
        del img
    shutil.rmtree(test_out)

def test_res_w():
    new_width = 500
    subprocess.run(['python', 'app', '-m', 'res_w', '-i', test_folder, '-o', test_out, '--new_width', str(new_width)])
    
    for file in test_out.iterdir():
        img = Image.open(file)
        assert math.isclose(img.width, new_width, abs_tol=3), \
        f'Error at file {file} with found width {img.width} and new width {new_width}'
        del img
    shutil.rmtree(test_out)

def test_res_p():
    # factor = round(random.random(),1)
    factor = .8
    subprocess.run(['python', 'app', '-m', 'res_p', '-i', test_folder, '-o', test_out, '--factor', str(factor)])
    
    for file in test_out.iterdir():
        img = Image.open(file)
        orig_img = Image.open(test_folder/file.name)
        assert math.isclose(img.width, orig_img.width*factor, abs_tol=1) and \
        math.isclose(img.height, orig_img.height*factor, abs_tol=1), \
        f'Error at file {file}, factor = {factor} found dimension ({img.width},{img.height}), original dimension ({orig_img.width},{orig_img.height})'
        del img
        del orig_img
    shutil.rmtree(test_out)    

def test_crp_p():
    # factor = round(random.random(),1)
    factor = .8
    subprocess.run(['python', 'app', '-m', 'crp_p', '-i', test_folder, '-o', test_out, '--factor', str(factor)])
    
    for file in test_out.iterdir():
        img = Image.open(file)
        orig_img = Image.open(test_folder/file.name)
        assert math.isclose(img.width, orig_img.width*factor, abs_tol=1) and \
        math.isclose(img.height, orig_img.height*factor, abs_tol=1), \
        f'Error at file {file}, factor = {factor} found dimension ({img.width},{img.height}), original dimension ({orig_img.width},{orig_img.height})'
        del img
        del orig_img
    shutil.rmtree(test_out) 

def test_crp_px():

    new_size = 224, 224
    subprocess.run(['python', 'app', '-m', 'crp_px', '-i', test_folder, '-o', test_out, '--new_size', str(new_size[0]), str(new_size[1])])
    
    for file in test_out.iterdir():
        img = Image.open(file)
        orig_img = Image.open(test_folder/file.name)
        assert math.isclose(img.width, new_size[0], abs_tol=1) and \
        math.isclose(img.height, new_size[1], abs_tol=1), \
        f'Error at file {file}, found dimension ({img.width},{img.height}), original dimension ({orig_img.width},{orig_img.height})'
        del img
        del orig_img
    shutil.rmtree(test_out) 

def test_crp_px_invalid_width():
    file = next(test_folder.iterdir())
    import crp_px
    with pytest.raises(ValueError):
        crp_px.crop_by_dim(file, Path.cwd(), new_size=(-1,200)), "Invalid Width"

def test_crp_px_invalid_height():
    file = next(test_folder.iterdir())
    import crp_px
    with pytest.raises(ValueError):
        crp_px.crop_by_dim(file, Path.cwd(), new_size=(200,-5)), 'Invalid Height'

def test_crp_px_invalid_dim():
    file = next(test_folder.iterdir())
    img = Image.open(file)
    import crp_px
    with pytest.raises(ValueError):
        crp_px.crop_by_dim(file, Path.cwd(), new_size=(img.width+5, img.height+5)), 'Invalid Dimensions'

def test_res_w_invalid_width():
    file = next(test_folder.iterdir())
    import res_w
    with pytest.raises(ValueError):
        res_w.resize_by_width(file, Path.cwd(), new_width=-100), 'Invalid Width'

def test_res_h_invalid_height():
    file = next(test_folder.iterdir())
    import res_h
    with pytest.raises(ValueError):
        res_h.resize_by_height(file, Path.cwd(), new_height=-100), 'Invalid height'

def test_res_p_invalid_factor():
    file = next(test_folder.iterdir())
    import res_p
    with pytest.raises(ValueError):
        res_p.resize_by_factor(file, Path.cwd(), factor=-100), 'Factor must be positive'

def test_j2p_invalid_ext():
    file = next(test_folder.iterdir())
    import j2p
    with pytest.raises(TypeError):
        j2p.jpg_to_png(file.stem/'.png', Path.cwd()), 'Only jpg and jpegs allowed'

def test_p2j_invalid_ext():
    file = next(test_folder.iterdir())
    import p2j
    with pytest.raises(TypeError):
        p2j.png_to_jpg(file.stem/'.jpg', Path.cwd()), 'Only png allowed'

main_funcs = [func for func in inspect.getmembers(main) if inspect.isfunction(func[1])]

README_CONTENT_CHECK_FOR = ['j2p', 'p2j', 'res_h', 'res_w', 'res_p', 'crp_p', 'crp_px']

CHECK_FOR_THINGS_NOT_ALLOWED = []

def test_for_docstrings():
    for func in main_funcs:
        assert func[1].__doc__ , f'Function {func[0]} has no doc string'

def test_for_annotations():
    for func in main_funcs:
        assert func[1].__annotations__ , f'Function {func[0]} has no annotations'

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"


def test_readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(
        readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"


def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"


def test_readme_file_for_formatting():
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 10


def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(main)
    spaces = re.findall('\n +.', lines)
    for count, space in enumerate(spaces):
        assert len(space) % 4 == 2, f"Your script contains misplaced indentations at \
n'th postion {count+1} starting \n with {space}"
        assert len(re.sub(
            r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"


def test_function_name_had_cap_letter():
    functions = inspect.getmembers(main, inspect.isfunction)
    for function in functions:
        assert len(re.findall(
            '([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

