# Author: Mauro Faccin 2014
# -------------------------
# |   This is dotinstall  |
# -------------------------
# |    License: GPL3      |
# |   see LICENSE.txt     |
# -------------------------
import sys
import os
import argparse
import string
import numpy as np

import dotinstall

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='QuEBApp: Quantum\
                                     Community Detection' )
    parser.add_argument('--edgelist', action='store_true',\
                        help='Read Hamiltonian as list of edges [i j\
                        weight(optional)]')
    parser.add_argument('network',\
                        help='Network file [default=Hamiltonian matrix]')
    parser.add_argument('-0','--time0',action='store_true',\
                        help='Closeness measure with short-time limit\
                        [default: long-time limit]')
    parser.add_argument('-t','--type',type=str,choices=['fidelity','transport','purity'],\
                        default='fidelity',\
                        help='Use a specific closeness measure\
                        [default: fidelity]')
    parser.add_argument('-d','--dendrogram',action='store_true',\
                        help='Outputs the resulting dendrogram\
                        and modularity')
    args = parser.parse_args()

    # read the Hamiltonian
    if args.edgelist:
        H = read_edgelist(args.network)
    else:
        try:
            H = np.loadtxt(args.network)
        except:
            raise TypeError('Unreadable file: {}'.format(args.network))

    system = physics.System (H)

    # 
    T = 'zero' if args.time0 else 'infty'

    # find communities
    dendrogram = physics.find_communities(system,distance=args.type,T=T)

    if args.dendrogram:
        commands.print_best_community(dendrogram)
        commands.print_dendrogram(dendrogram)
    else:
        commands.print_best_community(dendrogram)
        



