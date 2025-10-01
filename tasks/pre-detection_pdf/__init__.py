from oocana import Context
import os
import PyPDF2
import fitz  # PyMuPDF for PDF to image conversion
from PIL import Image
import tempfile
import io

#region generated meta
import typing
class Inputs(typing.TypedDict):
    file: str
class Outputs(typing.TypedDict):
    file: typing.NotRequired[str]
    cover_image: typing.NotRequired[str | None]
#endregion

def main(params: Inputs, context: Context) -> Outputs:
    file_path = params["file"]
    
    # Check if file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"PDF file not found: {file_path}")
    
    # Check file size (200MB = 200 * 1024 * 1024 bytes)
    file_size = os.path.getsize(file_path)
    max_size = 200 * 1024 * 1024  # 200MB
    
    if file_size > max_size:
        raise ValueError(f"PDF file is too large: {file_size / (1024 * 1024):.1f}MB. Maximum allowed size is 200MB.")
    
    # Check page count
    try:
        with open(file_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            page_count = len(pdf_reader.pages)
            
            if page_count > 600:
                raise ValueError(f"PDF has too many pages: {page_count}. Maximum allowed pages is 600.")
                
    except Exception as e:
        if "too many pages" in str(e) or "too large" in str(e):
            raise e
        else:
            raise ValueError(f"Failed to read PDF file: {str(e)}")
    
    # Extract first page as cover image
    cover_image_path = None
    try:
        pdf_document = fitz.open(file_path)

        if len(pdf_document) > 0:
            # Get the first page
            first_page = pdf_document[0]

            # Convert page to image (pixmap)
            mat = fitz.Matrix(2.0, 2.0)  # 2x zoom for better quality
            pixmap = first_page.get_pixmap(matrix=mat)

            # Convert to PIL Image
            img_data = pixmap.tobytes("png")
            pil_image = Image.open(io.BytesIO(img_data))

            # Save cover image to oomol-storage
            os.makedirs("/oomol-driver/oomol-storage", exist_ok=True)

            # Generate unique filename for cover image
            import uuid
            cover_filename = f"cover_{uuid.uuid4().hex[:8]}.png"
            cover_image_path = os.path.join("/oomol-driver/oomol-storage", cover_filename)

            # Save the image
            pil_image.save(cover_image_path, "PNG", optimize=True)

        pdf_document.close()

    except Exception as e:
        # Log error but don't fail the entire process
        print(f"Warning: Failed to extract cover image: {str(e)}")
        cover_image_path = ""

    # If validation passes, return the file path and cover image
    return {
        "file": file_path,
        "cover_image": cover_image_path or ""
    }
