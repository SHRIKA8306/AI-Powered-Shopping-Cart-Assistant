from roboflow import Roboflow

rf = Roboflow(api_key="B8WYgL8xxOoBCk30IuW7")
project = rf.workspace("miniproject-qspoe").project("shopping-trolley-kn5tj-nisex")
dataset = project.version(2).download("yolov8")







