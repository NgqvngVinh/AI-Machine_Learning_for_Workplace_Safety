########################################################################
#
# Copyright (c) 2022, STEREOLABS.
#
# All rights reserved.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
########################################################################

"""
    This sample shows how to detect objects and draw 3D bounding boxes around them
    in an OpenGL window
"""
# import sys
# import ogl_viewer.viewer as gl
# import pyzed.sl as sl
# import argparse




# def parse_args(init):
#     if len(opt.input_svo_file)>0 and opt.input_svo_file.endswith(".svo"):
#         init.set_from_svo_file(opt.input_svo_file)
#         print("[Sample] Using SVO File input: {0}".format(opt.input_svo_file))
#     elif len(opt.ip_address)>0 :
#         ip_str = opt.ip_address
#         if ip_str.replace(':','').replace('.','').isdigit() and len(ip_str.split('.'))==4 and len(ip_str.split(':'))==2:
#             init.set_from_stream(ip_str.split(':')[0],int(ip_str.split(':')[1]))
#             print("[Sample] Using Stream input, IP : ",ip_str)
#         elif ip_str.replace(':','').replace('.','').isdigit() and len(ip_str.split('.'))==4:
#             init.set_from_stream(ip_str)
#             print("[Sample] Using Stream input, IP : ",ip_str)
#         else :
#             print("Unvalid IP format. Using live stream")
#     if ("HD2K" in opt.resolution):
#         init.camera_resolution = sl.RESOLUTION.HD2K
#         print("[Sample] Using Camera in resolution HD2K")
#     elif ("HD1200" in opt.resolution):
#         init.camera_resolution = sl.RESOLUTION.HD1200
#         print("[Sample] Using Camera in resolution HD1200")
#     elif ("HD1080" in opt.resolution):
#         init.camera_resolution = sl.RESOLUTION.HD1080
#         print("[Sample] Using Camera in resolution HD1080")
#     elif ("HD720" in opt.resolution):
#         init.camera_resolution = sl.RESOLUTION.HD720
#         print("[Sample] Using Camera in resolution HD720")
#     elif ("SVGA" in opt.resolution):
#         init.camera_resolution = sl.RESOLUTION.SVGA
#         print("[Sample] Using Camera in resolution SVGA")
#     elif ("VGA" in opt.resolution):
#         init.camera_resolution = sl.RESOLUTION.VGA
#         print("[Sample] Using Camera in resolution VGA")
#     elif len(opt.resolution)>0: 
#         print("[Sample] No valid resolution entered. Using default")
#     else : 
#         print("[Sample] Using default resolution")


# def main():
#     # Create a Camera object
#     zed = sl.Camera()

#     # Create a InitParameters object and set configuration parameters
#     init_params = sl.InitParameters()
#     init_params.coordinate_units = sl.UNIT.METER
#     init_params.coordinate_system = sl.COORDINATE_SYSTEM.RIGHT_HANDED_Y_UP

#     parse_args(init_params)


#     # Open the camera
#     err = zed.open(init_params)
#     if err != sl.ERROR_CODE.SUCCESS:
#         exit(1)

#     # Enable object detection module
#     obj_param = sl.ObjectDetectionParameters()
#     # Defines if the object detection will track objects across images flow.
#     obj_param.enable_tracking = True       # if True, enable positional tracking

#     obj_param.detection_model = sl.OBJECT_DETECTION_MODEL.MULTI_CLASS_BOX_MEDIUM

#     if obj_param.enable_tracking:
#         zed.enable_positional_tracking()
        
#     zed.enable_object_detection(obj_param)

#     camera_info = zed.get_camera_information()
#     # Create OpenGL viewer
#     viewer = gl.GLViewer()

#     if not viewer.init(camera_info.camera_configuration.calibration_parameters.left_cam, obj_param.enable_tracking):
#         print("Failed to initialize the viewer.")
#         return
#     print("Viewer initialized.")




#     viewer.init(camera_info.camera_configuration.calibration_parameters.left_cam, obj_param.enable_tracking)

#     # Configure object detection runtime parameters
#     obj_runtime_param = sl.ObjectDetectionRuntimeParameters()
#     obj_runtime_param.detection_confidence_threshold = 60
#     obj_runtime_param.object_class_filter = [sl.OBJECT_CLASS.PERSON]    # Only detect Persons

#     # Create ZED objects filled in the main loop
#     objects = sl.Objects()
#     image = sl.Mat()

#     # Set runtime parameters
#     runtime_parameters = sl.RuntimeParameters()
    
#     while viewer.is_available():
#         # Grab an image, a RuntimeParameters object must be given to grab()
#         if zed.grab(runtime_parameters) == sl.ERROR_CODE.SUCCESS:
#             print("Frame grabbed successfully.")
#             # Retrieve left image
#             zed.retrieve_image(image, sl.VIEW.LEFT)
#             # Retrieve objects
#             zed.retrieve_objects(objects, obj_runtime_param)
#             if objects.is_new:
#                 print("New objects detected.")
#             # Update GL view
#             viewer.update_view(image, objects)

#         else:
#             print("Failed to grab frame.")

#     viewer.exit()

#     image.free(memory_type=sl.MEM.CPU)
#     # Disable modules and close camera
#     zed.disable_object_detection()
#     zed.disable_positional_tracking()

#     zed.close()


# if __name__ == "__main__":
#     parser = argparse.ArgumentParser()
#     parser.add_argument('--input_svo_file', type=str, help='Path to an .svo file, if you want to replay it',default = '')
#     parser.add_argument('--ip_address', type=str, help='IP Adress, in format a.b.c.d:port or a.b.c.d, if you have a streaming setup', default = '')
#     parser.add_argument('--resolution', type=str, help='Resolution, can be either HD2K, HD1200, HD1080, HD720, SVGA or VGA', default = '')
#     opt = parser.parse_args()
#     if len(opt.input_svo_file)>0 and len(opt.ip_address)>0:
#         print("Specify only input_svo_file or ip_address, or none to use wired camera, not both. Exit program")
#         exit()
#     main() 


import sys
import ogl_viewer.viewer as gl
import pyzed.sl as sl
import argparse
from ogl_viewer.viewer import generate_color_id
from ogl_viewer.viewer import Simple3DObject
from datetime import datetime
import cv2
import numpy as np






def parse_args(init):
    if len(opt.input_svo_file)>0 and opt.input_svo_file.endswith(".svo"):
        init.set_from_svo_file(opt.input_svo_file)
        print("Using SVO File input: {0}".format(opt.input_svo_file))
    elif len(opt.ip_address)>0 :
        ip_str = opt.ip_address
        if ip_str.replace(':','').replace('.','').isdigit() and len(ip_str.split('.'))==4 and len(ip_str.split(':'))==2:
            init.set_from_stream(ip_str.split(':')[0],int(ip_str.split(':')[1]))
            print("[Sample] Using Stream input, IP : ",ip_str)
        elif ip_str.replace(':','').replace('.','').isdigit() and len(ip_str.split('.'))==4:
            init.set_from_stream(ip_str)
            print("[Sample] Using Stream input, IP : ",ip_str)
        else :
            print("Unvalid IP format. Using live stream")
    if ("HD2K" in opt.resolution):
        init.camera_resolution = sl.RESOLUTION.HD2K
        print("[Sample] Using Camera in resolution HD2K")
    elif ("HD1200" in opt.resolution):
        init.camera_resolution = sl.RESOLUTION.HD1200
        print("[Sample] Using Camera in resolution HD1200")
    elif ("HD1080" in opt.resolution):
        init.camera_resolution = sl.RESOLUTION.HD1080
        print("Using Camera in resolution HD1080")
    elif ("HD720" in opt.resolution):
        init.camera_resolution = sl.RESOLUTION.HD720
        print("[Sample] Using Camera in resolution HD720")
    elif ("SVGA" in opt.resolution):
        init.camera_resolution = sl.RESOLUTION.SVGA
        print("[Sample] Using Camera in resolution SVGA")
    elif ("VGA" in opt.resolution):
        init.camera_resolution = sl.RESOLUTION.VGA
        print("[Sample] Using Camera in resolution VGA")
    elif len(opt.resolution)>0: 
        print("[Sample] No valid resolution entered. Using default")
    else : 
        print("[Sample] Using default resolution")




def main():




    ###################################################################################

    # metadata_by_id = {
    #     0: ("Nguyen Le Thanh Duc", "Mechanical Engineer", "20",  "27-09-2004"),
    #     1: ("Nguyen Viet Hung", "Chief Engineer", "20", "10-09-2004"),
    #     2: ("Nguyen Phuoc Bao", "Customer Engineer", "20", "15-07-2004")
    # }
    metadata_by_id = {
        2: ("Pham Nguyen Minh Hieu", "Chief Engineer", "20", "10-09-2004"),
        1: ("Tran My Quyen", "Mechanical Engineer", "20", "18-10-2004"),
        0: ("Nguyen Phuoc Bao", "Customer Engineer", "20", "15-07-2004"),
        4: ("Nguyen Quang Vinh", "Customer Engineer", "20", "15-07-2004")
    }


    # Create a Camera object
    zed = sl.Camera()

    # Create a InitParameters object and set configuration parameters
    init_params = sl.InitParameters()
    init_params.coordinate_units = sl.UNIT.METER
    init_params.coordinate_system = sl.COORDINATE_SYSTEM.RIGHT_HANDED_Y_UP

    parse_args(init_params)

    # Open the camera
    err = zed.open(init_params)
    if err != sl.ERROR_CODE.SUCCESS:
        exit(1)


    # Generate a unique SVO filename with timestamp
    # current_time =  datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    # # svo_output_path = f"D:\ZED_SVO_Recording\Result\\Result_{current_time}.svo" #unique filename for each session
    # svo_output_path = f"D:\ZED_SVO_Recording\Result\\Result_{current_time}.avi" #unique filename for each session
    # fourcc = cv2.VideoWriter_fourcc(*'XVID')
    # out = cv2.VideoWriter(svo_output_path, fourcc, 20.0, (1280,720))

    #Setup SVO recording parameters
    # recording_params = sl.RecordingParameters(svo_output_path, sl.SVO_COMPRESSION_MODE.H264)
    # #Start recording
    # zed.enable_recording(recording_params)


    # Enable object detection module
    obj_param = sl.ObjectDetectionParameters()

    # Defines if the object detection will track objects across images flow.
    obj_param.enable_tracking = True       # if True, enable positional tracking

    obj_param.detection_model = sl.OBJECT_DETECTION_MODEL.MULTI_CLASS_BOX_MEDIUM

    if obj_param.enable_tracking:
        zed.enable_positional_tracking()
        
    zed.enable_object_detection(obj_param)

    camera_info = zed.get_camera_information()


    
    # Create OpenGL viewer
    viewer = gl.GLViewer()
    draw = gl.Simple3DObject(0)
    viewer.init(camera_info.camera_configuration.calibration_parameters.left_cam, obj_param.enable_tracking)

    # Configure object detection runtime parameters
    obj_runtime_param = sl.ObjectDetectionRuntimeParameters()
    obj_runtime_param.detection_confidence_threshold = 60
    obj_runtime_param.object_class_filter = [sl.OBJECT_CLASS.PERSON]    # Only detect Persons

    # Create ZED objects filled in the main loop
    objects = sl.Objects()
    image = sl.Mat()

    # Set runtime parameters
    runtime_parameters = sl.RuntimeParameters()
    
    while viewer.is_available():

        
        # Grab an image, a RuntimeParameters object must be given to grab()
        if zed.grab(runtime_parameters) == sl.ERROR_CODE.SUCCESS:

          
            # Retrieve left image
            zed.retrieve_image(image, sl.VIEW.LEFT)
            # Retrieve objects
            zed.retrieve_objects(objects, obj_runtime_param)
            
           



        ################################
            for obj in objects.object_list:
            # for i, obj in enumerate(objects.object_list):
                pos = [obj.position[0], obj.position[1], obj.position[2]]
                color_id = generate_color_id(obj.id)  # Ensure you have this function to set color
                real_name, occupation, age, birthday = metadata_by_id.get(obj.id, ("Unknown", "Unknown", "Unknown", "Unknown"))

                # Update view with additional metadata
                viewer.create_id_rendering(pos, color_id, obj.id, real_name, occupation, age, birthday)

            
            # Update GL view
            viewer.update_view(image, objects, metadata_by_id)
            




    #     # Tạo tên file video AVI dựa trên thời gian hiện tại
    # current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    # video_filename = f'D:\\ZED_SVO_Recording\\Result\\Zones_Detection_{current_time}.avi'

    # Tạo VideoWriter của OpenCV với định dạng AVI
    # fourcc = cv2.VideoWriter_fourcc(*'XVID')
    # out = cv2.VideoWriter(video_filename, fourcc, 30.0, (1280,720))

    while viewer.is_available():
        # Grab an image, a RuntimeParameters object must be given to grab()
        if zed.grab(runtime_parameters) == sl.ERROR_CODE.SUCCESS:
            # Retrieve left image
            zed.retrieve_image(image, sl.VIEW.LEFT)
            frame = image.get_data()
            # Retrieve objects
            zed.retrieve_objects(objects, obj_runtime_param)
            
    #         # Xử lý khung hình ở đây
            
    #         # Ghi khung hình đã xử lý vào video
    #         # out.write(image.get_data())
    #         out.write(frame)

    #         # Hiển thị khung hình và đối tượng đã phát hiện lên màn hình OpenGL
    #         viewer.update_view(image, objects, metadata_by_id)

    # # Giải phóng tài nguyên và kết thúc chương trình
    # out.release()
    viewer.exit()

    image.free(memory_type=sl.MEM.CPU)
    # Disable modules and close camera
    zed.disable_object_detection()
    zed.disable_positional_tracking()
    zed.close()


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('--input_svo_file', type=str, help='Path to an .svo file, if you want to replay it',default = 'D:\ZED_SVO_Recording\zones.svo')
    parser.add_argument('--ip_address', type=str, help='IP Adress, in format a.b.c.d:port or a.b.c.d, if you have a streaming setup', default = '')
    parser.add_argument('--resolution', type=str, help='Resolution, can be either HD2K, HD1200, HD1080, HD720, SVGA or VGA', default = 'HD108')
    opt = parser.parse_args()
    if len(opt.input_svo_file)>0 and len(opt.ip_address)>0:
        print("Specify only input_svo_file or ip_address, or none to use wired camera, not both. Exit program")
        exit()
    main() 


