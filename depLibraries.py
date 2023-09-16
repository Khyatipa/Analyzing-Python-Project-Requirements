import pkg_resources
import subprocess

def check_dependencies(library_name):
    # To give library name manually-
    # library_name = input("Enter the name of the library: ")

    try:
        # Checking if the library is already installed
        dist = pkg_resources.get_distribution(library_name.lower())

    except pkg_resources.DistributionNotFound:
        # If not installed, installing the library
        subprocess.call(['pip', 'install', library_name])

    # Getting the distribution object for the specified library
    dist = pkg_resources.get_distribution(library_name.lower())

    # Getting the dependencies of the library
    dependencies = dist.requires()

    # Printing the dependencies
    print(f"Dependencies of {library_name}:")
    for dependency in dependencies:
        print(dependency)

# While giving library manually
# check_dependencies()

# Specificed library name for example 
library = 'pandas'
check_dependencies(library)
