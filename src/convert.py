# https://groups.csail.mit.edu/vision/datasets/ADE20K/

import glob
import json
import os
import shutil
from urllib.parse import unquote, urlparse

import numpy as np
import supervisely as sly
from dataset_tools.convert import unpack_if_archive
from dotenv import load_dotenv
from supervisely.imaging.color import hex2rgb
from supervisely.io.fs import (
    file_exists,
    get_file_ext,
    get_file_name,
    get_file_name_with_ext,
    get_file_size,
)
from supervisely.io.json import load_json_file
from tqdm import tqdm

import src.settings as s


def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:
    # project_name = "ADE20K"
    dataset_path = "APP_DATA/ADE20K_2021_17_01/images/ADE"
    anns_ext = ".json"
    images_ext = ".jpg"
    batch_size = 30

    def create_ann(image_path):
        global meta
        labels = []

        ann_path = image_path.replace(images_ext, anns_ext)
        if file_exists(ann_path):
            with open(ann_path, encoding="ISO-8859-1") as f:
                ann_data = json.load(f)["annotation"]
            img_height = ann_data["imsize"][0]
            img_wight = ann_data["imsize"][1]
            scene_data = ann_data["scene"]
            scene_value = ", ".join(scene_data)
            scene = sly.Tag(tag_scene, value=scene_value)
            for curr_object in ann_data["object"]:
                class_name = curr_object["raw_name"]
                obj_class = meta.get_obj_class(class_name)
                if obj_class is None:
                    obj_class = sly.ObjClass(class_name, sly.Polygon)
                    meta = meta.add_obj_class(obj_class)
                    api.project.update_meta(project.id, meta.to_json())
                poly_data = curr_object["polygon"]
                exterior = list(zip(poly_data["y"], poly_data["x"]))
                if len(exterior) < 3:
                    continue
                polygon = sly.Polygon(exterior)
                label_poly = sly.Label(polygon, obj_class)
                labels.append(label_poly)

        return sly.Annotation(img_size=(img_height, img_wight), labels=labels, img_tags=[scene])

    obj_classes = []
    tag_scene = sly.TagMeta("scene", sly.TagValueType.ANY_STRING)

    project = api.project.create(workspace_id, project_name, change_name_if_conflict=True)
    meta = sly.ProjectMeta(obj_classes=obj_classes, tag_metas=[tag_scene])

    for ds_name in os.listdir(dataset_path):
        dataset = api.dataset.create(project.id, ds_name, change_name_if_conflict=True)

        ds_path = os.path.join(dataset_path, ds_name)

        images_pathes = glob.glob(ds_path + "/*/*/*.jpg")

        progress = sly.Progress("Create dataset {}".format(ds_name), len(images_pathes))

        for img_pathes_batch in sly.batched(images_pathes, batch_size=batch_size):
            img_names_batch = [
                get_file_name_with_ext(image_path) for image_path in img_pathes_batch
            ]

            img_infos = api.image.upload_paths(dataset.id, img_names_batch, img_pathes_batch)
            img_ids = [im_info.id for im_info in img_infos]

            anns = [create_ann(image_path) for image_path in img_pathes_batch]
            api.annotation.upload_anns(img_ids, anns)

            progress.iters_done_report(len(img_names_batch))
    return project
