# Demo for a nix flake python project

This project is based on uv2nix.

Before we can build for nix we should lock uv.

The `nix develop .#impure` is needed to run `uv lock` in nixos

```bash
nix develop .#impure
uv lock
```

now you can build for nix

```bash
nix build
```


```bash
nix build
```


Run the script you'll need a model that supports edgetpu. you can take this base `.tflite model` and the labels that belong to it:


```bash
wget https://github.com/google-coral/edgetpu/raw/master/test_data/ssd_mobilenet_v2_coco_quant_postprocess.tflite

wget https://github.com/google-coral/edgetpu/raw/master/test_data/coco_labels.txt
```

To get this model working for coral you'll need to parse it first. Below is a shell with the requirements.

```bash
nix shell nixpkgs#edgetpu-compiler
```

then run this command

```bash
edgetpu_compiler ssd_mobilenet_v2_coco_quant_postprocess.tflite
```

Now you have a model that can be used.


Run the result with the model and the labels.

FOr example here we have the modes under `./models` and the test file under `./data`


```bash
sudo ./result/bin/coral_demo -m ./models/ssd_mobilenet_v2_coco_quant_postprocess_edgetpu.tflite -i ../coral/data/example.jpg -l ../coral/models/coco_labels.txt
```

