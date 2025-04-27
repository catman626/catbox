#!/bin/bash
echo "[Ascend310B1] Generating MselossCustom_73ca3925e3e9120293f07c3b303b4a41 ..."
opc $1 --main_func=mseloss_custom --input_param=/root/catman/prepared/from_scratch/mseloss/gen/build_out/op_kernel/binary/ascend310b/gen/MselossCustom_73ca3925e3e9120293f07c3b303b4a41_param.json --soc_version=Ascend310B1 --output=$2 --impl_mode="" --simplified_key_mode=0 --op_mode=dynamic

if ! test -f $2/MselossCustom_73ca3925e3e9120293f07c3b303b4a41.json ; then
  echo "$2/MselossCustom_73ca3925e3e9120293f07c3b303b4a41.json not generated!"
  exit 1
fi

if ! test -f $2/MselossCustom_73ca3925e3e9120293f07c3b303b4a41.o ; then
  echo "$2/MselossCustom_73ca3925e3e9120293f07c3b303b4a41.o not generated!"
  exit 1
fi
echo "[Ascend310B1] Generating MselossCustom_73ca3925e3e9120293f07c3b303b4a41 Done"
