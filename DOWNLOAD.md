Dataset **ADE20K** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/H/k/HS/uDP9lAylNCHq8u0mNZzST5aZC2Zi9OzoCC9lvHev1Ld5UwoymEluFGziJgYuRFIO5ILgXRqcd9Err8mvpBOjhbB7sGiEMxVt63OgGOhj8ks81m8AtCrRwU8Ef54x.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='ADE20K', dst_dir='~/dataset-ninja/')
```
Make sure not to overlook the [python code example](https://developer.supervisely.com/getting-started/python-sdk-tutorials/iterate-over-a-local-project) available on the Supervisely Developer Portal. It will give you a clear idea of how to effortlessly work with the downloaded dataset.

The data in original format can be [downloaded here](https://groups.csail.mit.edu/vision/datasets/ADE20K/#Download).