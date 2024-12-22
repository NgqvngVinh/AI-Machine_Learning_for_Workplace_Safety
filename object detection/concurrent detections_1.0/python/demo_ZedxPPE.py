# # import pyzed.sl as sl
# # import cv2
# # from ultralytics import YOLO
# # from ultralytics.utils.plotting import Annotator

# # def main():
# #     # Initialize ZED camera
# #     zed = sl.Camera()
# #     init_params = sl.InitParameters()
# #     init_params.camera_resolution = sl.RESOLUTION.HD720  # Set resolution
# #     init_params.camera_fps = 30  # Set FPS
# #     err = zed.open(init_params)
# #     if err != sl.ERROR_CODE.SUCCESS:
# #         exit(1)

# #     # Load YOLO models
# #     model = YOLO('yolov8s_custom.pt')
# #     model_1 = YOLO('ppe.pt')

# #     # Create a Mat to store images
# #     image_zed = sl.Mat()

# #     # Capture loop
# #     while True:
# #         # Grab an image
# #         if zed.grab() == sl.ERROR_CODE.SUCCESS:
# #             # Retrieve the left image
# #             zed.retrieve_image(image_zed, sl.VIEW.LEFT)
# #             # Get the image data
# #             frame = image_zed.get_data()

# #             # Resize frame if necessary
# #             frame_resized = cv2.resize(frame, (640, 360))

# #             # Process with YOLO models (example with one model)
# #             results = model.predict(frame_resized, conf=0.8)

# #             # Example of drawing boxes
# #             for r in results:
# #                 annotator = Annotator(frame_resized, line_width=2)
# #                 boxes = r.boxes
# #                 for box in boxes:
# #                     b = box.xyxy[0]
# #                     c = box.cls
# #                     annotator.box_label(b, model.names[int(c)])
# #             frame_resized = annotator.result()

# #             # Display the image
# #             cv2.imshow("PPE Detection", frame_resized)
# #             key = cv2.waitKey(1)
# #             if key == 27:  # Press 'ESC' to quit
# #                 break

# #     # Close the camera
# #     zed.close()

# # if __name__ == "__main__":
# #     main()



#chay dc nhma bị sai màu
# import pyzed.sl as sl
# import cv2
# from ultralytics import YOLO
# from ultralytics.utils.plotting import Annotator

# def main():
#     zed = sl.Camera()
#     init_params = sl.InitParameters()
#     init_params.camera_resolution = sl.RESOLUTION.HD720
#     init_params.camera_fps = 60
#     if zed.open(init_params) != sl.ERROR_CODE.SUCCESS:
#         exit(1)

#     # Cập nhật đường dẫn đến mô hình của bạn ở đây
#     model = YOLO(r'C:\Program Files (x86)\ZED SDK\samples\object detection\custom detector\python\pytorch_yolov8\yolov8s_custom.pt', task="detect")  # Sử dụng raw string hoặc thay `\` bằng `/`
#     ppe_model = YOLO(r'C:\Program Files (x86)\ZED SDK\samples\object detection\custom detector\python\pytorch_yolov8\ppe.pt', task="detect")  # Sử dụng raw string hoặc thay `\` bằng `/`
#     model.to('cuda:0')
#     ppe_model.to('cuda:0')
#     image_zed = sl.Mat()

    

#     while True:
#         if zed.grab() == sl.ERROR_CODE.SUCCESS:
#             zed.retrieve_image(image_zed, sl.VIEW.LEFT)
#             frame = image_zed.get_data()
            
            
#             frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGRA2RGB)  # Chuyển từ BGRA sang RGB
#             frame_resized = cv2.resize(frame_rgb, (640, 360))  # Tiếp tục với việc resize nếu cần

            
#             results = model.predict(frame_resized, conf=0.8)
#             ppe_results = ppe_model.predict(frame_resized, conf=0.8)
            
#             annotator = Annotator(frame_resized, line_width=2)
#             for result in [results, ppe_results]:
#                 for r in result:
#                     boxes = r.boxes
#                     for box in boxes:
#                         b = box.xyxy[0]
#                         c = box.cls
#                         annotator.box_label(b, r.names[int(c)])
#             frame_annotated = annotator.result()

            
            
#             cv2.imshow("PPE Detection", frame_annotated)
#             if cv2.waitKey(1) & 0xFF == 27:  # ESC key
#                 break

#     zed.close()

# if __name__ == "__main__":
#     main()





# mo cam :)))
###
# import pyzed.sl as sl
# import cv2
# from ultralytics import YOLO
# import ogl_viewer.viewer as gl
# import numpy as np

# def main():
#     zed = sl.Camera()

#     # Initialize ZED camera
#     init_params = sl.InitParameters()
#     init_params.camera_resolution = sl.RESOLUTION.HD1080
#     init_params.camera_fps = 30
#     init_params.coordinate_units = sl.UNIT.METER
#     init_params.coordinate_system = sl.COORDINATE_SYSTEM.RIGHT_HANDED_Y_UP
#     init_params.depth_mode = sl.DEPTH_MODE.ULTRA

#     if zed.open(init_params) != sl.ERROR_CODE.SUCCESS:
#         print("Failed to open ZED camera")
#         exit(1)

#     # Load YOLO models
#     model = YOLO(r'C:\Program Files (x86)\ZED SDK\samples\object detection\custom detector\python\pytorch_yolov8\yolov8s_custom.pt', task="detect").to('cuda')
#     ppe_model = YOLO(r'C:\Program Files (x86)\ZED SDK\samples\object detection\custom detector\python\pytorch_yolov8\ppe.pt', task="detect").to('cuda')

#     camera_info = zed.get_camera_information()
#     viewer = gl.GLViewer()
#     point_cloud_res = sl.Resolution(min(camera_info.camera_configuration.resolution.width, 720),
#                                     min(camera_info.camera_configuration.resolution.height, 404))
#     viewer.init(camera_info.camera_model, point_cloud_res, zed.enable_object_detection(sl.ObjectDetectionParameters()))

#     while viewer.is_available():
#         if zed.grab() == sl.ERROR_CODE.SUCCESS:
#             image_zed = sl.Mat()
#             zed.retrieve_image(image_zed, sl.VIEW.LEFT)
#             frame = image_zed.get_data()

#             rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2RGB)
#             results = model.predict(rgb_frame, conf=0.4)
#             ppe_results = ppe_model.predict(rgb_frame, conf=0.4)

#             if isinstance(results, list):
#                 print("Unexpected output format (list). Expected 'Results' object.")
#             else:
#                 results.plot(frame, line_thickness=2)
#                 ppe_results.plot(frame, line_thickness=2)

#             cv2.imshow("ZED | YOLO Detection", frame)

#             if cv2.waitKey(10) == 27:  # ESC
#                 break

#     viewer.exit()
#     zed.close()

# if __name__ == "__main__":
#     main()

##########

import pyzed.sl as sl
import cv2
from ultralytics import YOLO
from ultralytics.utils.plotting import Annotator
import ogl_viewer.viewer as gl
import numpy as np

def main():
    zed = sl.Camera()

    # Initialize ZED camera
    init_params = sl.InitParameters()
    init_params.camera_resolution = sl.RESOLUTION.HD1080
    init_params.camera_fps = 30
    init_params.coordinate_units = sl.UNIT.METER
    init_params.coordinate_system = sl.COORDINATE_SYSTEM.RIGHT_HANDED_Y_UP
    init_params.depth_mode = sl.DEPTH_MODE.ULTRA

    if zed.open(init_params) != sl.ERROR_CODE.SUCCESS:
        print("Failed to open ZED camera")
        exit(1)

    # Load YOLO models
    model = YOLO(r'C:\Program Files (x86)\ZED SDK\samples\object detection\custom detector\python\pytorch_yolov8\yolov8s_custom.pt', task="predict").to('cuda')
    ppe_model = YOLO(r'C:\Program Files (x86)\ZED SDK\samples\object detection\custom detector\python\pytorch_yolov8\ppe.pt', task="predict").to('cuda')

    camera_info = zed.get_camera_information()
    viewer = gl.GLViewer()
    point_cloud_res = sl.Resolution(min(camera_info.camera_configuration.resolution.width, 720),
                                    min(camera_info.camera_configuration.resolution.height, 404))
    viewer.init(camera_info.camera_model, point_cloud_res, zed.enable_object_detection(sl.ObjectDetectionParameters()))

    while viewer.is_available():
        if zed.grab() == sl.ERROR_CODE.SUCCESS:
            image_zed = sl.Mat()
            zed.retrieve_image(image_zed, sl.VIEW.LEFT)
            frame = image_zed.get_data()

            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2RGB)
            results = model.predict(rgb_frame, conf=0.4)
            ppe_results = ppe_model.predict(rgb_frame, conf=0.4)

            # Use Annotator for both results and ppe_results
            annotator = Annotator(frame, line_width=2)
            for result_set in [results, ppe_results]:
                if hasattr(result_set, 'xyxy'):
                    for det in result_set.xyxy[0]:
                        annotator.box_label(det[:4], f"{result_set.names[int(det[5])]} {det[4]:.2f}")
                elif isinstance(result_set, list) and all(isinstance(item, np.ndarray) for item in result_set):
                    for det in result_set:
                        if det.shape[1] == 6:
                            x1, y1, x2, y2, conf, cls_id = det[:, :6].T
                            annotator.box_label([x1, y1, x2, y2], f"{model.names[int(cls_id)]} {conf:.2f}")

            annotated_frame = annotator.result()

            cv2.imshow("ZED | YOLO Detection", annotated_frame)

            if cv2.waitKey(10) == 27:  # ESC
                break

    viewer.exit()
    zed.close()

if __name__ == "__main__":
    main()



































# import threading
# import cv2
# import numpy as np
# from ultralytics import YOLO

# import pyzed.sl as sl
# import ogl_viewer.viewer as gl
# from ultralytics.utils.plotting import Annotator


# def detection_thread(zed, runtime_parameters, lock, display_flag, model, ppe_model):
#     while display_flag[0]:
#         if zed.grab(runtime_parameters) == sl.ERROR_CODE.SUCCESS:
#             image_zed = sl.Mat()
#             zed.retrieve_image(image_zed, sl.VIEW.LEFT)
#             frame = image_zed.get_data()
#             frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGRA2RGB)
#             frame_resized = cv2.resize(frame_rgb, (640, 360))

#             with lock:
#                 results = model.predict(frame_resized, conf=0.8)
#                 ppe_results = ppe_model.predict(frame_resized, conf=0.8)

#             frame_annotated = frame_resized.copy()
#             for result in [results, ppe_results]:
#                 if len(result):
#                     for r in result:
#                         if len(r.boxes):
#                             b = r.boxes.xyxy[0]  # Ensure this is correct according to the data structure
#                             c = r.cls
#                             cv2.rectangle(frame_annotated, (int(b[0]), int(b[1])), (int(b[2]), int(b[3])), (0, 255, 0), 2)
#                             cv2.putText(frame_annotated, f'{r.names[int(c)]}', (int(b[0]), int(b[1])-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)

#             cv2.imshow("PPE Detection", frame_annotated)
#             cv2.waitKey(1)

# def main():
#     zed = sl.Camera()
#     init_params = sl.InitParameters()
#     init_params.camera_resolution = sl.RESOLUTION.HD720
#     init_params.camera_fps = 60
#     init_params.coordinate_units = sl.UNIT.METER
#     init_params.coordinate_system = sl.COORDINATE_SYSTEM.RIGHT_HANDED_Y_UP

#     if zed.open(init_params) != sl.ERROR_CODE.SUCCESS:
#         exit(1)

#     obj_param = sl.ObjectDetectionParameters()
#     obj_param.enable_tracking = True  # Enable tracking
#     obj_param.detection_model = sl.OBJECT_DETECTION_MODEL.MULTI_CLASS_BOX_MEDIUM

#     zed.enable_positional_tracking()  # Based on obj_param.enable_tracking
#     zed.enable_object_detection(obj_param)

#     camera_info = zed.get_camera_information()
#     viewer = gl.GLViewer()
#     viewer.init(camera_info.camera_configuration.calibration_parameters.left_cam,
#                 camera_info.camera_configuration.resolution,
#                 obj_param.enable_tracking)  # Ensure tracking is enabled as per your detection settings

#     obj_runtime_param = sl.ObjectDetectionRuntimeParameters()
#     obj_runtime_param.detection_confidence_threshold = 60
#     obj_runtime_param.object_class_filter = [sl.OBJECT_CLASS.PERSON]

#     model = YOLO(r'C:\Program Files (x86)\ZED SDK\samples\object detection\custom detector\python\pytorch_yolov8\yolov8s_custom.pt', task="detect").to('cuda:0')
#     ppe_model = YOLO(r'C:\Program Files (x86)\ZED SDK\samples\object detection\custom detector\python\pytorch_yolov8\ppe.pt', task="detect").to('cuda:0')

#     objects = sl.Objects()
#     image_zed = sl.Mat()
#     point_cloud = sl.Mat()  # To store point cloud data

#     runtime_parameters = sl.RuntimeParameters()

#     while viewer.is_available:
#         if zed.grab(runtime_parameters) == sl.ERROR_CODE.SUCCESS:
#             zed.retrieve_image(image_zed, sl.VIEW.LEFT)

#             zed.retrieve_objects(objects, obj_runtime_param)

#             viewer.updateData(image_zed, objects)

#             frame = image_zed.get_data()
#             frame_bgr = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)  # Corrected color space conversion
#             frame_resized = cv2.resize(frame_bgr, (640, 360))

#             results = model.predict(frame_resized, conf=0.8)
#             ppe_results = ppe_model.predict(frame_resized, conf=0.8)

#             annotator = Annotator(frame_resized, line_width=2)
#             for result in [results, ppe_results]:
#                 for r in result:
#                     if r.boxes:
#                         b = r.boxes.xyxy[0]  # Assuming r.boxes returns a tensor with boxes
#                         c = r.cls
#                         annotator.box_label(b, r.names[int(c)])

#             frame_annotated = annotator.result()

#             cv2.imshow("PPE Detection", frame_annotated)
#             if cv2.waitKey(1) & 0xFF == 27:  # ESC key
#                 break

#     viewer.exit()
#     image_zed.free(memory_type=sl.MEM.CPU)
#     zed.disable_object_detection()
#     zed.disable_positional_tracking()
#     zed.close()

# if __name__ == "__main__":
#     main()







# #Run ma ko hien len gi
# import pyzed.sl as sl
# import cv2
# from ultralytics import YOLO
# from ultralytics.utils.plotting import Annotator
# import ogl_viewer.viewer as gl

# def main():
#     zed = sl.Camera()
#     init_params = sl.InitParameters()
#     init_params.camera_resolution = sl.RESOLUTION.HD720
#     init_params.camera_fps = 60
#     init_params.coordinate_units = sl.UNIT.METER
#     init_params.coordinate_system = sl.COORDINATE_SYSTEM.RIGHT_HANDED_Y_UP
#     if zed.open(init_params) != sl.ERROR_CODE.SUCCESS:
#         exit(1)

#     obj_param = sl.ObjectDetectionParameters()
#     obj_param.enable_tracking = True
#     obj_param.detection_model = sl.OBJECT_DETECTION_MODEL.MULTI_CLASS_BOX_MEDIUM
#     if obj_param.enable_tracking:
#         zed.enable_positional_tracking()
#     zed.enable_object_detection(obj_param)

#     model = YOLO(r'C:\Program Files (x86)\ZED SDK\samples\object detection\custom detector\python\pytorch_yolov8\yolov8s_custom.pt', task="detect").to('cuda:0')
#     ppe_model = YOLO(r'C:\Program Files (x86)\ZED SDK\samples\object detection\custom detector\python\pytorch_yolov8\ppe.pt', task="detect").to('cuda:0')

#     runtime_parameters = sl.RuntimeParameters()


#     image_zed = sl.Mat()


#     point_cloud = sl.Mat()
#     objects = sl.Objects()

#     while True:
#         if zed.grab(runtime_parameters) == sl.ERROR_CODE.SUCCESS:


#             zed.retrieve_image(image_zed, sl.VIEW.LEFT)
#             zed.retrieve_objects(objects, obj_param)
#             zed.retrieve_measure(point_cloud, sl.MEASURE.XYZRGBA)




#             frame = image_zed.get_data()
#             frame_bgr = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
#             frame_resized = cv2.resize(frame_bgr, (640, 360))

#             zed.retrieve_measure(point_cloud, sl.MEASURE.XYZRGBA)
#             results = model.predict(frame_resized, conf=0.8)
#             ppe_results = ppe_model.predict(frame_resized, conf=0.8)


            
#             annotator = Annotator(frame_resized, line_width=2)
#             all_results = results + ppe_results



#             for result in all_results:
#                 for det in result:
#                     b = det.box
#                     c = det.cls
#                     annotator.box_label(b, result.names[int(c)])

#                     x_center = int((b[0] + b[2]) / 2)
#                     y_center = int((b[1] + b[3]) / 2)
#                     err, point3D = point_cloud.get_value(x_center, y_center)
#                     if err == sl.ERROR_CODE.SUCCESS: # and point3D[3] != 0:
#                         # print(f"3D Coordinates of {result.names[int(c)]}: {point3D[:3]}")
#                         size = (det.box[2] - det.box[0], det.box[3] - det.box[1], point3D[2]) 
#                         draw_3d_box(point3D[:3], size)
            
#             frame_annotated = annotator.result()
#             cv2.imshow("Detection Output", frame_annotated)
#             if cv2.waitKey(1) & 0xFF == 27:  # ESC key
#                 break

#     zed.close()

# if __name__ == "__main__":
#     main()


#####
# #Chay nhung ko len gi ca
# import pyzed.sl as sl
# import cv2
# from ultralytics import YOLO
# from ultralytics.utils.plotting import Annotator
# import ogl_viewer.viewer as gl

# def main():
#     zed = sl.Camera()
#     init_params = sl.InitParameters()
#     init_params.camera_resolution = sl.RESOLUTION.HD720
#     init_params.camera_fps = 60
#     init_params.coordinate_units = sl.UNIT.METER
#     init_params.coordinate_system = sl.COORDINATE_SYSTEM.RIGHT_HANDED_Y_UP
#     if zed.open(init_params) != sl.ERROR_CODE.SUCCESS:
#         exit(1)


#     # Set initialization parameters
#     detection_parameters = sl.ObjectDetectionParameters()
#     detection_parameters.enable_tracking = True # Objects will keep the same ID between frames
#     detection_parameters.enable_segmentation = True # Outputs 2D masks over detected objects

# # Set runtime parameters
#     detection_parameters_rt = sl.ObjectDetectionRuntimeParameters()
#     detection_parameters_rt.detection_confidence_threshold = 25
#     detection_parameters.detection_model = sl.OBJECT_DETECTION_MODEL.MULTI_CLASS_BOX_MEDIUM


#     # Enable object detection with initialization parameters
#     zed_error = zed.enable_object_detection(detection_parameters)
#     if zed_error != sl.ERROR_CODE.SUCCESS:
#         print("enable_object_detection", zed_error, "\nExit program.")
#         zed.close()
#         exit(-1)


#     objects = sl.Objects() # Structure containing all the detected objects
#     if zed.grab() == sl.ERROR_CODE.SUCCESS:
#         zed.retrieve_objects(objects, obj_runtime_param) # Retrieve the detected objects
#     for object in objects.object_list:
#         print("{} {}".format(object.id, object.position))

#     object_id = object.id # Get the object id
#     object_position = object.position # Get the object position
#     object_velocity = object.velocity # Get the object velocity
#     object_tracking_state = object.tracking_state # Get the tracking state of the object
#     if object_tracking_state == sl.OBJECT_TRACKING_STATE.OK:
#         print("Object {0} is tracked\n".format(object_id))
#     for object in objects.object_list:
#         if object.confidence < 0.1 :
#             continue
#   # Work with other objects

#     object_3Dbbox = object.bounding_box; # Get the 3D Bounding Box of the object
################################################################



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

# import pyzed.sl as sl
# import cv2
# import numpy as np
# import ogl_viewer.viewer as gl
# import argparse



# def main():
#     # Create a Camera object
#     zed = sl.Camera()

#     # Create a InitParameters object and set configuration parameters
#     init_params = sl.InitParameters()
#     init_params.depth_mode = sl.DEPTH_MODE.PERFORMANCE
#     init_params.coordinate_units = sl.UNIT.METER
#     init_params.sdk_verbose = 1
#     init_params.coordinate_system = sl.COORDINATE_SYSTEM.RIGHT_HANDED_Y_UP


#     # Open the camera
#     err = zed.open(init_params)
#     if err != sl.ERROR_CODE.SUCCESS:
#         print("Camera Open : "+repr(err)+". Exit program.")
#         exit()

#     obj_param = sl.ObjectDetectionParameters()
#     obj_param.enable_tracking=True
#     obj_param.enable_segmentation=True
#     obj_param.detection_model = sl.OBJECT_DETECTION_MODEL.MULTI_CLASS_BOX_MEDIUM

#     if obj_param.enable_tracking :
#         positional_tracking_param = sl.PositionalTrackingParameters()
#         #positional_tracking_param.set_as_static = True
#         zed.enable_positional_tracking(positional_tracking_param)

#     print("Object Detection: Loading Module...")

#     err = zed.enable_object_detection(obj_param)
#     if err != sl.ERROR_CODE.SUCCESS :
#         print("Enable object detection : "+repr(err)+". Exit program.")
#         zed.close()
#         exit()

#     objects = sl.Objects()
#     obj_runtime_param = sl.ObjectDetectionRuntimeParameters()
#     obj_runtime_param.detection_confidence_threshold = 40

#     iter = 0
#     while iter < 100:
#         zed.grab()
#         zed.retrieve_objects(objects, obj_runtime_param)
#         if objects.is_new :
#             obj_array = objects.object_list
#             print(str(len(obj_array))+" Object(s) detected\n")
#             if len(obj_array) > 0 :
#                 first_object = obj_array[0]
#                 print("First object attributes:")
#                 print(" Label '"+repr(first_object.label)+"' (conf. "+str(int(first_object.confidence))+"/100)")
#                 if obj_param.enable_tracking :
#                     print(" Tracking ID: "+str(int(first_object.id))+" tracking state: "+repr(first_object.tracking_state)+" / "+repr(first_object.action_state))
#                 position = first_object.position
#                 velocity = first_object.velocity
#                 dimensions = first_object.dimensions
#                 print(" 3D position: [{0},{1},{2}]\n Velocity: [{3},{4},{5}]\n 3D dimentions: [{6},{7},{8}]".format(position[0],position[1],position[2],velocity[0],velocity[1],velocity[2],dimensions[0],dimensions[1],dimensions[2]))
#                 if first_object.mask.is_init():
#                     print(" 2D mask available")

#                 print(" Bounding Box 2D ")
#                 bounding_box_2d = first_object.bounding_box_2d
#                 for it in bounding_box_2d :
#                     print("    "+str(it),end='')
#                 print("\n Bounding Box 3D ")
#                 bounding_box = first_object.bounding_box
#                 for it in bounding_box :
#                     print("    "+str(it),end='')

#         iter = iter +1
    
#     # After retrieving objects from a frame
#     # if objects.is_new:  # Check if new objects are detected
#     #     obj_array = objects.object_list
#     #     for obj in obj_array:
#     #         position = obj.position  # 3D position (X, Y, Z) in meters
#     #         velocity = obj.velocity  # 3D velocity vector
#     #         dimensions = obj.dimensions  # Width, height, and depth of the bounding box

#     #     # Print the 3D position
#     #         print(f"3D position: [{position[0]:.2f}, {position[1]:.2f}, {position[2]:.2f}] meters")

    

#     # Close the camera
#     zed.disable_object_detection()
#     zed.close()

# if __name__ == "__main__":
#     main()

