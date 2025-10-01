from oocana import Context

#region generated meta
import typing
class Inputs(typing.TypedDict):
    response_data: dict
class Outputs(typing.TypedDict):
    full_zip_url: typing.NotRequired[str]
#endregion

def main(params: Inputs, context: Context) -> Outputs:
    response_data = params.get("response_data")
    
    if not response_data:
        raise ValueError("response_data 参数不能为空")
    
    if not isinstance(response_data, dict):
        raise ValueError("response_data 必须是字典类型")
    
    # 从response_data中提取full_zip_url
    full_zip_url = response_data.get("full_zip_url", "")
    
    if not full_zip_url:
        raise ValueError("response_data 中未找到有效的 full_zip_url")

    return {
      "full_zip_url": full_zip_url
    }
