;Findnig the Area of a Circle
;Takes input from keyboard

(defun AreaOfCircle())
(princ "Enter Radius: ")
(setq radius (read))
(setq area (* 3.1416 radius radius))
(princ "Area: ")
(write area)
(AreaOfCircle)
