from PIL import Image, ImageChops, ImageEnhance
import io
import numpy as np

def run_ela(image_bytes, resave_quality=90):
    """
    Perform Error Level Analysis on image bytes.
    Returns: (heatmap_png_bytes, ela_score_float)
    """
    # load original
    orig = Image.open(io.BytesIO(image_bytes)).convert("RGB")

    # resave to JPEG in memory
    buf = io.BytesIO()
    orig.save(buf, format='JPEG', quality=resave_quality)
    buf.seek(0)
    recompressed = Image.open(buf).convert("RGB")

    # compute absolute difference
    diff = ImageChops.difference(orig, recompressed)

    # amplify differences for visualization
    extrema = diff.getextrema()
    # compute simple score: mean of grayscale diff
    diff_gray = diff.convert("L")
    arr = np.array(diff_gray).astype('float32')
    ela_score = float(arr.mean() / 255.0)

    # enhance contrast to make heatmap visible
    enhancer = ImageEnhance.Brightness(diff)
    diff = enhancer.enhance(2.0)
    enhancer_c = ImageEnhance.Contrast(diff)
    diff = enhancer_c.enhance(2.0)

    out_buf = io.BytesIO()
    diff.save(out_buf, format='PNG')
    out_buf.seek(0)
    return out_buf.read(), ela_score
