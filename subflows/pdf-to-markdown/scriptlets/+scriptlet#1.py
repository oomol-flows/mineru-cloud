from oocana import Context

#region generated meta
import typing
class Inputs(typing.TypedDict):
    response_data: dict
class Outputs(typing.TypedDict):
    full_zip_url: str
#endregion

def main(params: Inputs, context: Context) -> Outputs:
    response_data = params.get("response_data")
    
    # 从response_data中提取full_zip_url
    full_zip_url = response_data.get("full_zip_url", "") if response_data else ""

    return {
      "full_zip_url": full_zip_url
    }
