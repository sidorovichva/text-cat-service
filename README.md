Service does zero-shot classification on provided through API text

By default, service uses valhalla model, but can be easily enhanced with other models

Install docker locally, with tag = 1.0.0 as an example:
- make build_image_with_tag_no_cache tag=1.0.0
- make run_container tag=1.0.0

Install with qdrant db:
- make build
- make up

API: 
- /classifier/zero_shot

Method: 
- GET

Params:
- text: string
- transformer_name: string (optional, default = valhalla)

Returns:
- category: string (Categories are defined in src/python/enum/Category.py)