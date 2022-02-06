# -*- coding: utf-8 -*-
"""json_to_csv.ipynb

This script generates two csv files:
annotation_data.csv - containing bounding box and image category.
image_data.csv - containing width and height of image.

Required arguments
annotation json file and output directory to create csv's.
"""

import numpy as np
import pandas as pd
import json
import csv
import argparse
import os

def create_image_csv(data, output_file_dir):
  image_data = data['images']
  img_data_file = open(output_file_dir + '/image_data.csv', 'w')
  csv_writer = csv.writer(img_data_file)
  csv_writer.writerow(['img_id', 'filename', 'width', 'height'])

  for img_data in image_data:
      width = img_data['width']
      height = img_data['height']
      img_id = img_data['id']
      file_name = img_data['file_name']
      csv_writer.writerow([img_id, file_name, width, height])
  img_data_file.close()

def create_annotation_csv(data, output_file_dir):
  ann_data_file = open(output_file_dir + '/annotation_data.csv', 'w')
  csv_writer = csv.writer(ann_data_file)
  csv_writer.writerow(['img_id', 'img_label', 'xmin', 'ymin', 'xmax', 'ymax'])
  annotations_data = data["annotations"]

  for ann_data in annotations_data:
      img_id = ann_data['image_id']
      img_label = ann_data['category_id']
      xmin, ymin, bb_width, bb_height = ann_data['bbox']
    # xmax will be xmin + boundingbox width
    # ymax will be ymin + boundingbox height
      xmax = xmin + bb_width
      ymax = ymin + bb_height
      csv_writer.writerow([img_id, img_label, xmin, ymin, xmax, ymax])
  ann_data_file.close()

  create_image_csv(data, output_file_dir)

def convert_to_csv(json_file_path, output_file_dir):
  with open(json_file_path) as json_file:
    data = json.load(json_file)

  create_annotation_csv(data, output_file_dir)

def main():
  parser = argparse.ArgumentParser(description="Tensorflow JSON to CSV converter")
  parser.add_argument("-i", "--jsonFilePath",
                      help="Path to folder where json file is stored, including file name with extension",
                      type=str)
  parser.add_argument("-o", "--outputFileDir",
                      help="Output folder path to export csv files",
                      type=str)
  args = parser.parse_args()

  if(args.jsonFilePath is None):
    args.jsonFilePath = os.getcwd()
  if(args.outputFileDir is None):
    args.outputFileDir = args.jsonFilePath

  convert_to_csv(args.jsonFilePath, args.outputFileDir)
  print("JSON to CSV conversion successful")

if __name__ == '__main__':
  main()

