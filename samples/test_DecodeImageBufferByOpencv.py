import os
import sys
from typing import List
from dbr import *
import cv2


# you can change the following variables' value to your own value.
license_key = "Input your own license"
json_file = r"Please input your own template path"
original_image = r"Please input your own image path"

image = cv2.imread(original_image)

reader = BarcodeReader()

# Apply for a trial license: https://www.dynamsoft.com/customer/license/trialLicense
reader.init_license(license_key)

## The code snippet below shows how to use the full license in DBR 8.x:
# connection_paras = BarcodeReader.init_lts_connection_parameters()
## If DBR service is already built on your server, you can fill in the address of your server, or leave this property's default value.
# connection_paras.main_server_url = "Input your own server url"
# connection_paras.handshake_code = "Input your own handshake"
# connection_paras.deployment_type = EnumDMDeploymentType.DM_DT_DESKTOP
# connection_paras.uuid_generation_method = EnumDMUUIDGenerationMethod.DM_UUIDGM_RANDOM
# try:
#     error = BarcodeReader.init_license_from_lts(connection_paras)
#     if error[0] != EnumErrorCode.DBR_OK:
#         print(error[1])
# except BarcodeReaderError as bre:
#     print(bre)

error = reader.init_runtime_settings_with_file(json_file)
if error[0] != EnumErrorCode.DBR_OK:
    print(error[1])


try:
    text_results = reader.decode_buffer(image)
    # buffer = image.tobytes()
    # height = image.shape[0]
    # width = image.shape[1]
    # stride = image.strides[0]
    # text_results = reader.decode_buffer_manually(buffer, width, height, stride, EnumImagePixelFormat.IPF_RGB_888, "")
# if your python version is equal to or higher than python3.6, you can use the following code to replace the above code
    # text_results:List[TextResult] = reader.decode_buffer(image)

    if text_results != None:
        for text_result in text_results:
            print("Barcode Format : ")
            print(text_result.barcode_format_string)
            print("Barcode Text : ")
            print(text_result.barcode_text)
            print("Localization Points : ")
            print(text_result.localization_result.localization_points)
            print("Exception : ")
            print(text_result.exception)
            print("-------------")
except BarcodeReaderError as bre:
    print(bre)