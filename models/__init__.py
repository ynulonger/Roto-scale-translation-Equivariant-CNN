# MNIST
from .mnist_ss import mnist_ss_28, mnist_ss_56
from .mnist_sevf import mnist_sevf_scalar_28, mnist_sevf_scalar_56, mnist_sevf_vector_28, mnist_sevf_vector_56
from .mnist_cnn import mnist_cnn_28, mnist_cnn_56, mnist_cnn_96
from .mnist_kanazawa import mnist_kanazawa_28, mnist_kanazawa_56
from .mnist_xu import mnist_xu_28, mnist_xu_56
from .mnist_dss import mnist_dss_vector_28, mnist_dss_vector_56, mnist_dss_scalar_28, mnist_dss_scalar_56
#from .mnist_ses import mnist_ses_scalar_28, mnist_ses_scalar_56, mnist_ses_vector_28, mnist_ses_vector_56
#from .mnist_ses importf mnist_ses_scalar_28p, mnist_ses_scalar_56p, mnist_ses_vector_28p, mnist_ses_vector_56p
from .mnist_ses import mnist_ses_scalar_28_rot_1, mnist_ses_scalar_28_rot_4, mnist_ses_scalar_28_rot_8
from .mnist_res import mnist_res_scalar_28_rot_1, mnist_res_scalar_28_rot_4, mnist_res_scalar_28_rot_8
from .mnist_ses import mnist_ses_scalar_56_rot_1, mnist_ses_scalar_56_rot_4, mnist_ses_scalar_56_rot_8
from .mnist_res import mnist_res_scalar_56_rot_1, mnist_res_scalar_56_rot_4, mnist_res_scalar_56_rot_8
from .mnist_ses import mnist_ses_vector_28_rot_4_interrot_2, mnist_ses_vector_28_rot_8_interrot_1, mnist_ses_vector_28_rot_8_interrot_4, mnist_ses_vector_28_rot_8_interrot_8

from .cifar_ses import cifar_ses_scalar_28_rot_1, cifar_ses_scalar_28_rot_4, cifar_ses_scalar_28_rot_8
from .cifar_ses import cifar_ses_scalar_56_rot_1, cifar_ses_scalar_56_rot_4, cifar_ses_scalar_56_rot_8
from .cifar_ses import cifar_ses_vector_28_rot_4_interrot_2, cifar_ses_vector_28_rot_8_interrot_1, cifar_ses_vector_28_rot_8_interrot_4, cifar_ses_vector_28_rot_8_interrot_8
from .cifar_ses import cifar_ses_vector_56_rot_4_interrot_2, cifar_ses_vector_56_rot_4_interrot_4, cifar_ses_vector_56_rot_8_interrot_1, cifar_ses_vector_56_rot_8_interrot_4, cifar_ses_vector_56_rot_8_interrot_8

from .mnist_res import mnist_res_vector_28_rot_8_interrot_1, mnist_res_vector_28_rot_8_interrot_4, mnist_res_vector_28_rot_8_interrot_8
from .mnist_ses import mnist_ses_vector_56_rot_4_interrot_2, mnist_ses_vector_56_rot_4_interrot_4, mnist_ses_vector_56_rot_8_interrot_1, mnist_ses_vector_56_rot_8_interrot_4, mnist_ses_vector_56_rot_8_interrot_8
from .mnist_res import mnist_res_vector_56_rot_8_interrot_1, mnist_res_vector_56_rot_8_interrot_4, mnist_res_vector_56_rot_8_interrot_8

from .sim2mnist_ses import mnist_ses_scalar_96_rot_1, mnist_ses_scalar_96_rot_4, mnist_ses_scalar_96_rot_8
from .sim2mnist_ses import mnist_ses_vector_96_rot_8_interrot_4

from .sim2mnist_res import mnist_res_scalar_96_rot_1, mnist_res_scalar_96_rot_4, mnist_res_scalar_96_rot_8

from .mnistrts_ses import mnist_ses_scalar_42_rot_1, mnist_ses_scalar_42_rot_4, mnist_ses_scalar_42_rot_8
from .mnistrts_ses import mnist_ses_vector_42_rot_8_interrot_4

# # STL 10
from .stl_wrn import wrn_16_8
from .stl_kanazawa import wrn_16_8_kanazawa
from .stl_xu import wrn_16_8_xu
from .stl_ss import wrn_16_8_ss
from .stl_dss import wrn_16_8_dss
from .stl_ses import wrn_16_8_ses_a, wrn_16_8_ses_b, wrn_16_8_ses_c
