from roboflow import Roboflow

rf = Roboflow(api_key="B8WYgL8xxOoBCk30IuW7")

# 1) Download Shopping Trolley dataset
project_trolley = rf.workspace("miniproject-qspoe").project("shopping-trolley-kn5tj-nisex")
dataset_trolley = project_trolley.version(2).download("yolov8")

# 2) Download Groceries dataset (replace with actual workspace/project name from Roboflow)
project_groceries = rf.workspace("miniproject-qspoe").project("fruits-and-vegetables-yz9mm-bnudc")
dataset_groceries = project_groceries.version(1).download("yolov8")









