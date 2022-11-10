import argparse

parser = argparse.ArgumentParser(description="Flower Simulation with PyTorch")

parser.add_argument("--num_rounds", type=int, default=4)
parser.add_argument("--num_clients", type=int, default=2)
parser.add_argument("--cl_lr", type=float, default=0.01)
parser.add_argument("--cl_momentum", type=float, default=0.9)
parser.add_argument("--feature_maps", type=int, default=16)
parser.add_argument("--cl_epochs", type=int, default=1)
parser.add_argument("--cl_bs", type=int, default=20)
parser.add_argument("--alpha",type=int, default=1000)
parser.add_argument("--alpha_inf",action="store_true") # uniform
parser.add_argument("--val_ratio", type=float, default=0.1)
parser.add_argument("--only_cpu", action="store_true")
parser.add_argument("--only_cpu_eval", action="store_true")
parser.add_argument("--model", type = str, default='resnet12')
parser.add_argument("--wbits", type=int,default=0)
parser.add_argument("--dataset", type = str, default='cifar10')
parser.add_argument("--bnn", action="store_true")
parser.add_argument("--tnn", action="store_true")
parser.add_argument("--prune", action="store_true")
parser.add_argument("--prune_srv", action="store_true")
parser.add_argument("--prate", type=float, default=0.1)
parser.add_argument("--samp_rate", type=float, default=1.0)
parser.add_argument("--layer_sparsity",action="store_true")

# parse input arguments
args = parser.parse_args()
