from PIL import Image
import glob

# filepaths
fp_in = "./output/*.jpg"
fp_out = "ga.gif"

img, *imgs = [Image.open(f) for f in sorted(glob.glob(fp_in))]
img.save(fp=fp_out, format='GIF', append_images=imgs,
         save_all=True, duration=200, loop=0)