#! /usr/bin/python3
installation_complete = True

try:
    import networkx
except:
    installation_complete = False
    print("python module 'networkx' not installed. ")
    print("If you're not using anaconda (if you have no idea what anaconda is, you're probably not using it xD), run one of the following commands:")
    print("Linux/MacOS:")
    print("\n python3 -m pip install networkx \n")
    print("Windows:")
    print("\n py -m pip install networkx \n")
    print("If you are using anaconda, try:")
    print("\n conda install -c conda-forge networkx \n ")
    print("if that runs without any errors, rerun this script.")
try:
    import matplotlib.pyplot
except:
    installation_complete = False
    print("python module 'matplotlib' not installed. ")
    print("If you're not using anaconda (if you have no idea what anaconda is, you're probably not using it xD), run one of the following commands:")
    print("Linux/MacOS:")
    print("\n python3 -m pip install matplotlib \n")
    print("Windows:")
    print("\n py -m pip install matplotlib \n")
    print("If you are using anaconda, try:")
    print("\n conda install -c conda-forge matplotlib \n")
    print("if that runs without any errors, rerun this script.")


try:
    import tsplib95
except:
    installation_complete = False
    print("python module 'tsplib95' not installed.")
    print("If you're not using anaconda (if you have no idea what anaconda is, you're probably not using it xD), run one of the following commands:")
    print("Linux/MacOS:")
    print("\n python3 -m pip install tsplib95 \n")
    print("Windows:")
    print("py -m pip install tsplib95")
    print("if that runs without any errors, rerun this script.")
    print("if you are using anaconda, it is a little bit more difficult to get this package.")
    print("you need to have git installed to run the following command:")
    print("\n git clone https://github.com/rhgrant10/tsplib95.git \n")
    print("now go into that directory by entering")
    print("\n cd tsplib95 \n")
    print("and install it with the following command")
    print("\n python setup.py install\n")
    print("if that runs without any errors, rerun this script.")

if installation_complete:
    print("you have all required modules installed, congratulations!")