from pathlib import Path
from tdw.asset_bundle_creator.model_creator import ModelCreator
from tdw.backend.paths import EXAMPLE_CONTROLLER_OUTPUT_PATH
import os
import json

rewrite = True

file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)
root_dir = os.path.dirname(os.getcwd()).replace("\\", "/") + "/"

save_dir = os.path.join(root_dir, "assets")
if not os.path.exists(save_dir):
    os.mkdir(save_dir)

if os.path.exists(os.path.join(save_dir, "library.json")):
    library = json.load(open(os.path.join(save_dir, "library.json")))
else:
    library = {"records": {}}

objs_dir = "./../OBJs"
obj_names = os.listdir(objs_dir)
for object_name in obj_names:
    if ".obj" in object_name or ".OBJ" in object_name:
        object = object_name.split(".")[0]
        if object_name not in library["records"].keys() or rewrite == False:
            ModelCreator().source_file_to_asset_bundles(
                name=object,
                source_file=Path(os.path.join(objs_dir, object_name)).resolve(),
                output_directory=save_dir,
                library_path=os.path.join(save_dir, "library.json"),
                library_description="Centered Objs",
                internal_materials=False,
                cleanup=True,
                write_physics_quality=True,
            )