
# import pyzed.sl as sl
# import sys
# # Create a ZED camera object
# zed = sl.Camera()

# init_params = sl.InitParameters()
# init_params.camera_resolution = sl.RESOLUTION.HD1080
# init_params.camera_fps = 30

# # Mở camera
# err = zed.open(init_params)
# if err != sl.ERROR_CODE.SUCCESS:
#     exit(-1)


# # Enable recording with the filename specified in argument
# output_path = sys.argv[0]
# recordingParameters = sl.RecordingParameters()
# recordingParameters.compression_mode = sl.SVO_COMPRESSION_MODE.H264
# recordingParameters.video_filename = output_path
# err = zed.enable_recording(recordingParameters)

# exit_app = False
# while  not exit_app:
#     # Each new frame is added to the SVO file
#     zed.grab()

# # Disable recording
# zed.disable_recording()

# import sys
# import pyzed.sl as sl
# from signal import signal, SIGINT
# import argparse 
# import os 

# cam = sl.Camera()

# #Handler to deal with CTRL+C properly
# def handler(signal_received, frame):
#     cam.disable_recording()
#     cam.close()
#     sys.exit(0)

# signal(SIGINT, handler)

# def main():
    
#     init = sl.InitParameters()
#     init.depth_mode = sl.DEPTH_MODE.NONE # Set configuration parameters for the ZED

#     status = cam.open(init) 
#     if status != sl.ERROR_CODE.SUCCESS: 
#         print("Camera Open", status, "Exit program.")
#         exit(1)
        
#     recording_param = sl.RecordingParameters(opt.output_svo_file, sl.SVO_COMPRESSION_MODE.H264) # Enable recording with the filename specified in argument
#     err = cam.enable_recording(recording_param)
#     if err != sl.ERROR_CODE.SUCCESS:
#         print("Recording ZED : ", err)
#         exit(1)

#     runtime = sl.RuntimeParameters()
#     print("SVO is Recording, use Ctrl-C to stop.") # Start recording SVO, stop with Ctrl-C command
#     frames_recorded = 0

#     while frames_recorded < 100:
#         if cam.grab(runtime) == sl.ERROR_CODE.SUCCESS : # Check that a new image is successfully acquired
#             frames_recorded += 1
#             print("Frame count: " + str(frames_recorded), end="\r")
#             data = sl.SVOData()
#             data.key = "TEST"
#             data.set_string_content("Hello, SVO World >> " + str(cam.get_timestamp(sl.TIME_REFERENCE.IMAGE).data_ns))
#             data.timestamp_ns = cam.get_timestamp(sl.TIME_REFERENCE.IMAGE)
#             print('INGEST', cam.ingest_data_into_svo(data))
    
# if __name__ == "__main__":
#     parser = argparse.ArgumentParser()
#     parser.add_argument('--output_svo_file', type=str, help='C:/Users/vinhd/OneDrive/文档/ZED', required= True)
#     opt = parser.parse_args()
#     if not opt.output_svo_file.endswith(".svo") and not opt.output_svo_file.endswith(".svo2"): 
#         print("--output_svo_file parameter should be a .svo file but is not : ",opt.output_svo_file,"Exit program.")
#         exit()
#     main()


# import sys
# import pyzed.sl as sl
# from signal import signal, SIGINT
# import argparse 
# import os 

# cam = sl.Camera()

# #Handler to deal with CTRL+C properly
# def handler(signal_received, frame):
#     cam.disable_recording()
#     cam.close()
#     sys.exit(0)

# signal(SIGINT, handler)

# def main():
    
#     init = sl.InitParameters()
#     init.depth_mode = sl.DEPTH_MODE.NONE # Set configuration parameters for the ZED

#     status = cam.open(init) 
#     if status != sl.ERROR_CODE.SUCCESS: 
#         print("Camera Open", status, "Exit program.")
#         exit(1)
        
#     recording_param = sl.RecordingParameters(opt.output_svo_file, sl.SVO_COMPRESSION_MODE.H264) # Enable recording with the filename specified in argument
#     err = cam.enable_recording(recording_param)
#     if err != sl.ERROR_CODE.SUCCESS:
#         print("Recording ZED : ", err)
#         exit(1)

#     runtime = sl.RuntimeParameters()
#     print("SVO is Recording, use Ctrl-C to stop.") # Start recording SVO, stop with Ctrl-C command
#     frames_recorded = 0

#     while True:
#         if cam.grab(runtime) == sl.ERROR_CODE.SUCCESS : # Check that a new image is successfully acquired
#             frames_recorded += 1
#             print("Frame count: " + str(frames_recorded), end="\r")
    
# if __name__ == "__main__":
#     parser = argparse.ArgumentParser()
#     parser.add_argument('--output_svo_file', type=str, help='Path to the SVO file that will be written', required= True)
#     opt = parser.parse_args()
#     if not opt.output_svo_file.endswith(".svo") and not opt.output_svo_file.endswith(".svo2"): 
#         print("--output_svo_file parameter should be a .svo file but is not : ",opt.output_svo_file,"Exit program.")
#         exit()
#     main()

import pyzed.sl as sl
import sys

zed = sl.Camera()
# err = zed.open(init_params)
# if err != sl.ERROR_CODE.SUCCESS:
#     exit(-1)

def main():
    zed = sl.Camera()
    init_params = sl.InitParameters()
    init_params.camera_resolution = sl.RESOLUTION.HD720
    init_params.camera_fps = 30
    if zed.open(init_params) != sl.ERROR_CODE.SUCCESS:
        exit(1)

# Enable recording with the filename specified in argument
output_path = sys.argv[0]
recordingParameters = sl.RecordingParameters()
recordingParameters.compression_mode = sl.SVO_COMPRESSION_MODE.H264
recordingParameters.video_filename = output_path
err = zed.enable_recording(recordingParameters)


exit_app = False

while not exit_app:
    # Each new frame is added to the SVO file
    zed.grab()

# Disable recording
zed.disable_recording()