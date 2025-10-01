from oocana import Context
import os
import PyPDF2

#region generated meta
import typing
class Inputs(typing.TypedDict):
    file: str
class Outputs(typing.TypedDict):
    file: typing.NotRequired[str]
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
    
    # If validation passes, return the file path
    return {"file": file_path}
