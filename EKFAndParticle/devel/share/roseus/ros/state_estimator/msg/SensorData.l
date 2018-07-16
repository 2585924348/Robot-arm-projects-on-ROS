;; Auto-generated. Do not edit!


(when (boundp 'state_estimator::SensorData)
  (if (not (find-package "STATE_ESTIMATOR"))
    (make-package "STATE_ESTIMATOR"))
  (shadow 'SensorData (find-package "STATE_ESTIMATOR")))
(unless (find-package "STATE_ESTIMATOR::SENSORDATA")
  (make-package "STATE_ESTIMATOR::SENSORDATA"))

(in-package "ROS")
;;//! \htmlinclude SensorData.msg.html


(defclass state_estimator::SensorData
  :super ros::object
  :slots (_vel_trans _vel_ang _readings ))

(defmethod state_estimator::SensorData
  (:init
   (&key
    ((:vel_trans __vel_trans) 0.0)
    ((:vel_ang __vel_ang) 0.0)
    ((:readings __readings) (let (r) (dotimes (i 0) (push (instance state_estimator::LandmarkReading :init) r)) r))
    )
   (send-super :init)
   (setq _vel_trans (float __vel_trans))
   (setq _vel_ang (float __vel_ang))
   (setq _readings __readings)
   self)
  (:vel_trans
   (&optional __vel_trans)
   (if __vel_trans (setq _vel_trans __vel_trans)) _vel_trans)
  (:vel_ang
   (&optional __vel_ang)
   (if __vel_ang (setq _vel_ang __vel_ang)) _vel_ang)
  (:readings
   (&rest __readings)
   (if (keywordp (car __readings))
       (send* _readings __readings)
     (progn
       (if __readings (setq _readings (car __readings)))
       _readings)))
  (:serialization-length
   ()
   (+
    ;; float64 _vel_trans
    8
    ;; float64 _vel_ang
    8
    ;; state_estimator/LandmarkReading[] _readings
    (apply #'+ (send-all _readings :serialization-length)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _vel_trans
       (sys::poke _vel_trans (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _vel_ang
       (sys::poke _vel_ang (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; state_estimator/LandmarkReading[] _readings
     (write-long (length _readings) s)
     (dolist (elem _readings)
       (send elem :serialize s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _vel_trans
     (setq _vel_trans (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _vel_ang
     (setq _vel_ang (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; state_estimator/LandmarkReading[] _readings
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _readings (let (r) (dotimes (i n) (push (instance state_estimator::LandmarkReading :init) r)) r))
     (dolist (elem- _readings)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;;
   self)
  )

(setf (get state_estimator::SensorData :md5sum-) "71af189c7d826d776a3face61f3225db")
(setf (get state_estimator::SensorData :datatype-) "state_estimator/SensorData")
(setf (get state_estimator::SensorData :definition-)
      "# The forward translational velocity commanded to the robot
float64 vel_trans

# The rotational velocity commanded to the robot
float64 vel_ang

# The readings of landmarks with the range of the robot's sensors
# Can be empty, if no landmarks are nearby
state_estimator/LandmarkReading[] readings

================================================================================
MSG: state_estimator/LandmarkReading
# The landmark for which this reading was created
state_estimator/Landmark landmark

# The range from the robot's location to the landmark above
float64 range

# The bearing of this landmark relative to the robot's orientation
float64 bearing

================================================================================
MSG: state_estimator/Landmark
# The x coordinate of this landmark
float64 x

# The y coordinate of this landmark
float64 y


")



(provide :state_estimator/SensorData "71af189c7d826d776a3face61f3225db")


