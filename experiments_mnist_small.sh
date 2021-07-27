# !/bin/bash
# MIT License. Copyright (c) 2020 Ivan Sosnovik, Michał Szmaja

MNIST_SCALE_DIR="${MNIST_SCALE_DIR:-./datasets}"


function train_scale_mnist() {
    # 1 model_name 
    # 2 extra_scaling
    # for seed in {0..5}
    for seed in {0..0}
    do 
        data_dir="$MNIST_SCALE_DIR/MNIST_scale/seed_$seed/scale_0.3_1.0"
        python train_scale_mnist.py \
            --batch_size 128 \
            --epochs 60 \
            --optim adam \
            --lr 0.01 \
            --lr_steps 20 40 \
            --model $1 \
            --save_model_path "./saved_models/mnist/$1_extra_scaling_$2.pt" \
            --cuda \
            --extra_scaling $2 \
            --tag "sesn_experiments" \
            --data_dir="$data_dir" \

    done               
}


#model_list=(
#    "mnist_ses_scalar_28"   # MNIST (28x28) 
#    "mnist_ses_vector_28"   # MNIST (28x28)
#    "mnist_ses_scalar_28p"  # MNIST (28x28) +
#    "mnist_ses_vector_28p"  # MNIST (28x28) +
#)

model_list=(
    "mnist_res_scalar_28_rot_8"              # scalar, 8 rotations
    "mnist_ses_scalar_28_rot_8"              # scalar, 8 rotations
    #"mnist_res_vector_28_rot_8_interrot_1"   # vector, 8 rotations
                                             # no rotation convolution
    #"mnist_res_vector_28_rot_8_interrot_4"   # vector, 8 rotations
                                             # 4 rotation convolution
    #"mnist_res_vector_28_rot_8_interrot_8"   # vector, 8 rotations
                                             # 8 rotation convolution
)

for model_name in "${model_list[@]}"
do
    for extra_scaling in 0.5
    do 
        train_scale_mnist "$model_name" "$extra_scaling" 
    done
done
